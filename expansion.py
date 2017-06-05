from google.cloud import storage
from pandas.io import gbq
import pandas as pd
import re

class PatentLandscapeExpander:
    seed_file = None
    # BigQuery must be enabled for this project
    bq_project = 'patent-landscape-165715'
    patent_dataset = 'patents-public-data:patents.publications_latest'
    #tmp_table = 'patents._tmp'
    l1_tmp_table = 'patents._l1_tmp'
    l2_tmp_table = 'patents._l2_tmp'
    antiseed_tmp_table = 'patents.antiseed_tmp'
    country_codes = set(['US'])
    num_anti_seed_patents = 15000

    # ratios and multipler for finding uniquely common CPC codes from seed set
    min_ratio_of_code_to_seed = 0.04
    min_seed_multiplier = 50.0

    def __init__(self, seed_file, bq_project=None, patent_dataset=None, num_antiseed=None):
        self.seed_file = seed_file
        if bq_project is not None:
            self.bq_project = bq_project
        if patent_dataset is not None:
            self.patent_dataset = patent_dataset
        #if tmp_table is not None:
        #    self.tmp_table = tmp_table
        if num_antiseed is not None:
            self.num_anti_seed_patents = num_antiseed


    def load_seeds_from_bq(self, seed_df):
        where_clause = ",".join("'" + seed_df.PubNum + "'")
        seed_patents_query = '''
        SELECT
          b.publication_number,
          'Seed' as ExpansionLevel,
          STRING_AGG(citations.publication_number) AS refs,
          STRING_AGG(cpcs.code) AS cpc_codes
        FROM
          `patent-landscape-165715.patents.publications_latest_copy` AS b,
          UNNEST(citation) AS citations,
          UNNEST(cpc) AS cpcs
        WHERE
        REGEXP_EXTRACT(b.publication_number, r'\w+-(\d+)-\w+') IN
        (
        {}
        )
        AND citations.publication_number != ''
        AND cpcs.code != ''
        GROUP BY b.publication_number
        ;
        '''.format(where_clause)

        seed_patents_df = gbq.read_gbq(
            query=seed_patents_query,
            project_id=self.bq_project,
            verbose=False,
            dialect='standard')

        return seed_patents_df

    def load_seed_pubs(self, seed_file=None):
        if seed_file is None:
            seed_file = self.seed_file

        seed_df = pd.read_csv(seed_file, header=None, names=['PubNum'], dtype={'PubNum': 'str'})

        return seed_df

    def bq_get_num_total_patents(self):
        num_patents_query = """
            SELECT
              COUNT(publication_number) AS num_patents
            FROM
              `patent-landscape-165715.patents.publications_latest_copy` AS b
            WHERE
              country_code = 'US'
        """
        num_patents_df = gbq.read_gbq(
            query=num_patents_query,
            project_id=self.bq_project,
            verbose=False,
            dialect='standard')
        return num_patents_df

    def get_cpc_counts(self, seed_publications=None):
        where_clause = '1=1'
        if seed_publications is not None:
            where_clause = """
            REGEXP_EXTRACT(b.publication_number, r'\w+-(\d+)-\w+') IN
                (
                {}
                )
            """.format(",".join("'" + seed_publications + "'"))

        cpc_counts_query = """
            SELECT
              cpcs.code,
              COUNT(cpcs.code) AS cpc_count
            FROM
              `patent-landscape-165715.patents.publications_latest_copy` AS b,
              UNNEST(cpc) AS cpcs
            WHERE
            {}
            AND cpcs.code != ''
            AND country_code = 'US'
            GROUP BY cpcs.code
            ORDER BY cpc_count DESC;
            """.format(where_clause)

        return gbq.read_gbq(
            query=cpc_counts_query,
            project_id=self.bq_project,
            verbose=False,
            dialect='standard')

    def compute_uniquely_common_cpc_codes_for_seed(self, seed_df):
        '''
        Queries for CPC counts across all US patents and all Seed patents, then finds the CPC codes
        that are 50x more common in the Seed set than the rest of the patent corpus (and also appear in
        at least 5% of Seed patents). This then returns a Pandas dataframe of uniquely common codes
        as well as the table of CPC counts for reference. Note that this function makes several
        BigQuery queries on multi-terabyte datasets, so expect it to take a couple minutes.
        
        You should call this method like:
        uniquely_common_cpc_codes, cpc_counts_df = \
            expander.compute_uniquely_common_cpc_codes_for_seed(seed_df)
            
        where seed_df is the result of calling load_seed_pubs() in this class.
        '''

        print('Querying for all US CPC Counts')
        us_cpc_counts_df = self.get_cpc_counts()
        print('Querying for Seed Set CPC Counts')
        seed_cpc_counts_df = self.get_cpc_counts(seed_df.PubNum)
        print("Querying to find total number of US patents")
        num_patents_df = self.bq_get_num_total_patents()

        num_seed_patents = seed_df.count().values[0]
        num_us_patents = num_patents_df['num_patents'].values[0]

        # Merge/join the dataframes on CPC code, suffixing them as appropriate
        cpc_counts_df = us_cpc_counts_df.merge(
            seed_cpc_counts_df, on='code', suffixes=('_us', '_seed')) \
            .sort_values(ascending=False, by=['cpc_count_seed'])

        # For each CPC code, calculate the ratio of how often the code appears
        #  in the seed set vs the number of total seed patents
        cpc_counts_df['cpc_count_to_num_seeds_ratio'] = cpc_counts_df.cpc_count_seed / num_seed_patents
        # Similarly, calculate the ratio of CPC document frequencies vs total number of US patents
        cpc_counts_df['cpc_count_to_num_us_ratio'] = cpc_counts_df.cpc_count_us / num_us_patents
        # Calculate how much more frequently a CPC code occurs in the seed set vs full corpus of US patents
        cpc_counts_df['seed_relative_freq_ratio'] = \
            cpc_counts_df.cpc_count_to_num_seeds_ratio / cpc_counts_df.cpc_count_to_num_us_ratio

        # We only care about codes that occur at least ~4% of the time in the seed set
        # AND are 50x more common in the seed set than the full corpus of US patents
        uniquely_common_cpc_codes = cpc_counts_df[
            (cpc_counts_df.cpc_count_to_num_seeds_ratio >= self.min_ratio_of_code_to_seed)
            &
            (cpc_counts_df.seed_relative_freq_ratio >= self.min_seed_multiplier)]

        return uniquely_common_cpc_codes, cpc_counts_df


    def get_set_of_refs_filtered_by_country(self, seed_refs_series, country_codes):
        '''
        Uses the refs column of the BigQuery on the seed set to compute the set of
        unique references out of the Seed set.
        '''

        all_relevant_refs = set()
        for refs in seed_refs_series:
            for ref in refs.split(','):
                country_code = re.sub(r'(\w+)-(\w+)-\w+', r'\1', ref)
                if country_code in country_codes:
                    all_relevant_refs.add(ref)

        return all_relevant_refs


    # Expansion Functions
    def load_df_to_bq_tmp(self, df, tmp_table):
        '''
        This function inserts the provided dataframe into a temp table in BigQuery, which
        is used in other parts of this class (e.g. L1 and L2 expansions) to join on by
        patent number.
        '''
        print('Loading dataframe with cols {}, shape {}, to {}'.format(
            df.columns, df.shape, tmp_table))
        gbq.to_gbq(
            dataframe=df,
            destination_table=tmp_table,
            project_id=self.bq_project,
            if_exists='replace',
            verbose=False)

        print('Completed loading temp table.')

    def expand_l2(self, refs_series):
        self.load_df_to_bq_tmp(pd.DataFrame(refs_series, columns=['pub_num']), self.l2_tmp_table)

        expansion_query = '''
            SELECT
              b.publication_number,
              'L2' AS ExpansionLevel,
              STRING_AGG(citations.publication_number) AS refs
            FROM
              `patent-landscape-165715.patents.publications_latest_copy` AS b,
              `{}` as tmp,
              UNNEST(citation) AS citations
            WHERE
            (
                b.publication_number = tmp.pub_num
            )
            AND citations.publication_number != ''
            GROUP BY b.publication_number
            ;
        '''.format(self.l2_tmp_table)

        #print(expansion_query)
        expansion_df = gbq.read_gbq(
            query=expansion_query,
            project_id=self.bq_project,
            verbose=False,
            dialect='standard')

        return expansion_df

    def expand_l1(self, cpc_codes_series, refs_series):
        self.load_df_to_bq_tmp(pd.DataFrame(refs_series, columns=['pub_num']), self.l1_tmp_table)

        cpc_where_clause = ",".join("'" + cpc_codes_series + "'")

        expansion_query = '''
            SELECT DISTINCT publication_number, ExpansionLevel, refs
            FROM
            (
            SELECT
              b.publication_number,
              'L1' as ExpansionLevel,
              STRING_AGG(citations.publication_number) AS refs
            FROM
              `patent-landscape-165715.patents.publications_latest_copy` AS b,
              UNNEST(citation) AS citations,
              UNNEST(cpc) AS cpcs
            WHERE
            (
                cpcs.code IN
                (
                {}
                )
            )
            AND citations.publication_number != ''
            AND country_code IN ('US')
            GROUP BY b.publication_number

            UNION ALL

            SELECT
              b.publication_number,
              'L1' as ExpansionLevel,
              STRING_AGG(citations.publication_number) AS refs
            FROM
              `patent-landscape-165715.patents.publications_latest_copy` AS b,
              `{}` as tmp,
              UNNEST(citation) AS citations
            WHERE
            (
                b.publication_number = tmp.pub_num
            )
            AND citations.publication_number != ''
            GROUP BY b.publication_number
            )
            ;
        '''.format(cpc_where_clause, self.l1_tmp_table)

        #print(expansion_query)
        expansion_df = gbq.read_gbq(
            query=expansion_query,
            project_id=self.bq_project,
            verbose=False,
            dialect='standard')

        return expansion_df

    def anti_seed(self, seed_expansion_series):
        self.load_df_to_bq_tmp(pd.DataFrame(seed_expansion_series, columns=['pub_num']), self.antiseed_tmp_table)

        anti_seed_query = '''
            SELECT DISTINCT
              b.publication_number,
              'AntiSeed' AS ExpansionLevel,
              rand() as random_num
            FROM
              `patent-landscape-165715.patents.publications_latest_copy` AS b
            LEFT OUTER JOIN `{}` AS tmp ON b.publication_number = tmp.pub_num
            WHERE
            tmp.pub_num IS NULL
            AND country_code = 'US'
            ORDER BY random_num
            LIMIT {}
            # TODO: randomize results
            ;
        '''.format(self.antiseed_tmp_table, self.num_anti_seed_patents)

        #print('Anti-seed query:\n{}'.format(anti_seed_query))
        anti_seed_df = gbq.read_gbq(
            query=anti_seed_query,
            project_id=self.bq_project,
            verbose=False,
            dialect='standard')

        return anti_seed_df

    def load_training_data_from_pubs(self, training_publications_df):
        tmp_table = 'patents._tmp_training'
        self.load_df_to_bq_tmp(df=training_publications_df, tmp_table=tmp_table)

        training_data_query = '''
            SELECT DISTINCT
                REGEXP_EXTRACT(LOWER(p.publication_number), r'[a-z]+-(\d+)-[a-z0-9]+') as pub_num,
                p.publication_number,
                p.family_id,
                p.priority_date,
                title.text as title_text,
                abstract.text as abstract_text,
                SUBSTR(claims.text, 0, 5000) as claims_text,
                SUBSTR(description.text, 0, 5000) as description_text,
                STRING_AGG(citations.publication_number) AS refs,
                STRING_AGG(cpcs.code) AS cpcs
            FROM
              `patent-landscape-165715.patents.publications_latest_copy` p,
              `{}` as tmp,
              UNNEST(p.title_localized) AS title,
              UNNEST(p.abstract_localized) AS abstract,
              UNNEST(p.claims_localized) AS claims,
              UNNEST(p.description_localized) AS description,
              UNNEST(p.title_localized) AS title_lang,
              UNNEST(p.abstract_localized) AS abstract_lang,
              UNNEST(p.claims_localized) AS claims_lang,
              UNNEST(p.description_localized) AS description_lang,
              UNNEST(citation) AS citations,
              UNNEST(cpc) AS cpcs
            WHERE
                p.publication_number = tmp.publication_number
                AND country_code = 'US'
                AND title_lang.language = 'en'
                AND abstract_lang.language = 'en'
                AND claims_lang.language = 'en'
                AND description_lang.language = 'en'
            GROUP BY p.publication_number, p.family_id, p.priority_date, title.text
            ;
        '''.format(tmp_table)

        print('Loading patent texts from provided publication numbers.')
        #print('Training data query:\n{}'.format(training_data_query))
        training_data_df = gbq.read_gbq(
            query=training_data_query,
            project_id=self.bq_project,
            verbose=False,
            dialect='standard',
            configuration = {'query': {'useQueryCache': True, 'allowLargeResults': False}})

        return training_data_df

    def do_full_expansion(self, seed_file):
        '''
        Does a full expansion on seed set as described in paper, using seed set
        to derive an anti-seed for use in supervised learning stage.
        
        Call this method like:
        seed_patents_df, l1_patents_df, l2_patents_df, anti_seed_patents = \
            expander.do_full_expansion(seed_file)
        '''
        seed_df = self.load_seed_pubs(seed_file)

        seed_patents_df = self.load_seeds_from_bq(seed_df)

        # Level 1 Expansion
        ## getting unique seed CPC codes
        uniquely_common_cpc_codes, cpc_counts_df = \
            self.compute_uniquely_common_cpc_codes_for_seed(seed_df)
        ## getting all the references out of the seed set
        all_relevant_refs = self.get_set_of_refs_filtered_by_country(
            seed_patents_df.refs, self.country_codes)
        print('Got {} relevant seed refs'.format(len(all_relevant_refs)))
        ## actually doing expansion with CPC and references
        l1_patents_df = self.expand_l1(
            uniquely_common_cpc_codes.code, pd.Series(list(all_relevant_refs)))
        print('Shape of L1 expansion: {}'.format(l1_patents_df.shape))

        # Level 2 Expansion
        l2_refs = self.get_set_of_refs_filtered_by_country(
            l1_patents_df.refs, self.country_codes)
        print('Got {} relevant L1->L2 refs'.format(len(l2_refs)))
        l2_patents_df = self.expand_l2(pd.Series(list(l2_refs)))
        print('Shape of L2 expansion: {}'.format(l2_patents_df.shape))

        # Get all publication numbers from Seed, L1, and L2
        ## for use in getting anti-seed
        all_pub_nums = pd.Series(seed_patents_df.publication_number) \
            .append(l1_patents_df.publication_number) \
            .append(l2_patents_df.publication_number)
        seed_and_expansion_pub_nums = set()
        for pub_num in all_pub_nums:
            seed_and_expansion_pub_nums.add(pub_num)
        print('Size of union of [Seed, L1, and L2]: {}'.format(len(seed_and_expansion_pub_nums)))

        # get the anti-seed set!
        anti_seed_df = self.anti_seed(pd.Series(list(seed_and_expansion_pub_nums)))

        return seed_patents_df, l1_patents_df, l2_patents_df, anti_seed_df


    def derive_training_data_from_seeds(self, seed_file):
        '''
        '''
        seed_patents_df, l1_patents_df, l2_patents_df, anti_seed_patents = \
            self.do_full_expansion(seed_file)
        training_publications_df = \
            seed_patents_df.append(anti_seed_patents)[['publication_number', 'ExpansionLevel']]

        print('Loading training data text from {} publication numbers'.format(training_publications_df.shape))
        training_data_df = self.load_training_data_from_pubs(training_publications_df[['publication_number']])

        print('Merging labels into training data.')
        training_data_full_df = training_data_df.merge(training_publications_df, on=['publication_number'])

        return training_data_full_df, seed_patents_df, l1_patents_df, l2_patents_df, anti_seed_patents
        

