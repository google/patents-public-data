# Copyright 2018 Google Inc. All Rights Reserved. Licensed under the Apache
# License, Version 2.0 (the "License"); you may not use this file except in
# compliance with the License. You may obtain a copy of the License at
# http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations under
# the License.
"""Preprocessing code for the patent claim breadth model."""
import argparse
import datetime
import logging
import os
import re
import sys
import apache_beam as beam
from apache_beam.metrics import Metrics
from apache_beam.options.pipeline_options import PipelineOptions
import tensorflow as tf

# Dictionary of Patterns we plan to count in the claim.
PATTERNS = {
    'element_cnt': ';',
    'atleastoneofand_cnt': r'(at\sleast\sone\sof).+(and)',
    'atleastoneofor_cnt': r'(at\sleast\sone\sof).+(or)',
    'adding_words_cnt': '(after|subsequent|\band\b|including|next)',
    'excluding_words_cnt': r'\b(or\b|not\b|only|exclu|except|without)',
    'limiting_words_cnt': '(wherein|consist|limit|never)',
    'counting_cnt': r'\b(second|third|fourth|fifth)\b',
    'groupconsistingof_cnt': r'group\sconsisting\sof',
    'digits_or_decimal_cnt': r'(\d+\.\d+|\.\d+|\d+)',
}

FEATURE_NAMES = [
    'word_cnt', 'word_cnt_unique', 'char_cnt', 'char_cnt_unique'
] + PATTERNS.keys()
NOW = datetime.datetime.now().strftime('%Y%m%d-%H%M%S')


def build_query_statement(min_priority_year, cpc_code_list, keep_pct):
  """Build a query to be run against the Google Patents Public Datasets.

  Args:
    min_priority_year: Integer noting the earliest year to include in results.
    cpc_code_list: A comma separated list of digits like 'A,B,C' which indicate
      the CPC groups to include in the results.
    keep_pct: A decimal between 0 and 1 indicating what percentage of records to
      return in the query. Useful for limiting the size of output during
      training with multiple CPC codes..

  Returns:
    Query: A string query in standardSQL syntax to run against BigQuery.
  """
  # Turn comma separated list of CPC code digits into SQL 'in' statement.
  cpc_codes = '(' + str(cpc_code_list.split(','))[1:-1] + ')'
  query = """
  #standardSQL
  with cpc4_quantiles as (
    SELECT
    cpc4, APPROX_QUANTILES(priority_yr, 4) as quantiles
    FROM (
      SELECT DISTINCT
      family_id,
      FLOOR(priority_date / 10000) as priority_yr,
      SUBSTR(cpc.code, 1, 4) cpc4 # Trim CPC Code to first 4 digits.
      FROM `patents-public-data.patents.publications`,
      UNNEST(cpc) as cpc
      WHERE country_code = 'US'
      AND FLOOR(priority_date / 10000) > {YEAR}
      AND substr(cpc.code, 1,1) in {CPCS}
    )
    GROUP BY 1
  )


  SELECT DISTINCT
    t1.publication_number,
    t1.fullclaim,
    t1.priority_yr,
    t1.cpc4,
    q.quantiles[offset(2)] as median_priority_yr
  FROM (
    SELECT
      p.publication_number,
      claims.text fullclaim,
      cast(priority_date/10000 as int64) priority_yr,
      substr(any_value(cpc.code),1,4) cpc4
    FROM `patents-public-data.patents.publications` p
    ,UNNEST(claims_localized) claims
    ,UNNEST(cpc) cpc
    WHERE claims.language = 'en'
    AND cpc.inventive = true
    AND cpc.first = true
    AND country_code = 'US'
    AND claims.text is not null
    AND substr(cpc.code, 1,1) in {CPCS}
    AND FLOOR(priority_date / 10000) > {YEAR}
    group by 1,2,3
  ) t1
  JOIN cpc4_quantiles q on t1.cpc4 = q.cpc4
  where rand() < {KEEP_PCT}
  """.format(CPCS=cpc_codes, YEAR=min_priority_year, KEEP_PCT=keep_pct)
  return query


def wordcount(text, unique=False):
  """Counts words in a string, optionally limiting to unique words."""
  words = re.findall(r'\w+', text.lower())
  if unique:
    words = set(words)
  return len(words)


def pattern_count(pattern, text):
  """Counts apperances of a Regex pattern in a string."""
  return len(re.findall(pattern, text))


def regex_first_claim(fullclaim, maxlen):
  """Attempts to extract the first patent claim from the full set of claims.

  Because patent claims have predictable strcuture, we can attempt to extract
  the first claim based on a few rules. If none of these work, we return all
  characters up to `maxlen`.

  Args:
    fullclaim: A string containing the full text of a patents claims.
    maxlen: An upper limit on the size of the result. This limit is only used if
      all previous extraction methods fail.
  Returns:
    A string containing the best estimate of the text of the first.
  """
  # First try the simplest - split on the text '2.' or '2 .'.
  split_on_2 = re.split(r'.\s+[2]\s*.', fullclaim)
  if len(split_on_2) > 1:
    return split_on_2[0]

  # Next split on the first reference to 'claim 1'.
  if 'claim 1' in fullclaim.lower():
    return fullclaim.split('claim 1')[0]

  # If none of the above worked, split on The (case sensistive). This word
  # should only appear in dependent claims by convention.
  if ' The ' in fullclaim:
    return fullclaim.split(' The ')[0]

  # Finally, just keep the first N chars based on maxlen input.
  return fullclaim[:maxlen]


class GetFirstClaim(beam.DoFn):
  """Beam DoFn to handle first claim extraction."""

  def __init__(self):
    self.fail_cnt = Metrics.counter('main', 'failed_to_parse_firstclaim')
    self.success_cnt = Metrics.counter('main', 'parse_firstclaim_success')

  def process(self, element, maxlen=2000):
    """If a claim can be extracted, yields the element with claim attached."""
    fullclaim = element.pop('fullclaim', None)
    first_claim = regex_first_claim(fullclaim, maxlen)
    if first_claim:
      element['first_claim'] = first_claim
      self.success_cnt.inc()
      yield element
    else:
      self.fail_cnt.inc()


class AddInferredClassLabel(beam.DoFn):
  """Beam DoFn to handle logic for applying class label to training examples."""

  def __init__(self):
    self.skipped_cnt = Metrics.counter('main', 'skipped_add_label')
    self.broad_cnt = Metrics.counter('main', 'add_label_broad')
    self.narrow_cnt = Metrics.counter('main', 'add_label_narrow')

  def process(self, element):
    """Adds a label to be used in training a classifier.

    Based on the publication type and priority date, we label some cases early
    and others late. This is based on a high level view of how innovation moves.
    Early inventions in a technology space tend to have broad claims relative
    to inventions which are later in their technology space.

    When an application is earlier than the median priority date for its main
    CPC code, the label 'broad' is assigned and when an issued patent is later
    than the median, the label 'narrow' is assigned.

    Args:
      element: The input pCollection which is a python dictionary.
    Yields:
      element: The output pCollection which is a python dictionary including one
        new key `label` added by this DoFn.
    """
    median_yr = element['median_priority_yr']
    if re.findall(r'-A\d$', element['publication_number'].strip()):
      pub_type = 'application'
    else:
      pub_type = 'issued_patent'

    if (element['priority_yr'] < median_yr) and (pub_type == 'application'):
      element['label'] = 'broad'
      self.broad_cnt.inc()
      yield element

    elif (element['priority_yr'] > median_yr) and (pub_type == 'issued_patent'):
      element['label'] = 'narrow'
      self.narrow_cnt.inc()
      yield element

    else:
      self.skipped_cnt.inc()


class TrainTestSplit(beam.DoFn):
  """Places input element into one of three output streams."""

  def __init__(self):
    self.train_cnt = Metrics.counter('main', 'train_cnt')
    self.test_cnt = Metrics.counter('main', 'test_cnt')
    self.eval_cnt = Metrics.counter('main', 'eval_cnt')

  def process(self, element):
    """Hashes the claim text to split into train/test streams."""
    hashed = hash(element['first_claim']) % 100
    if hashed < 20:
      self.test_cnt.inc()
      yield beam.pvalue.TaggedOutput('test', element)
    elif hashed < 40:
      self.eval_cnt.inc()
      yield beam.pvalue.TaggedOutput('eval', element)
    else:
      self.train_cnt.inc()
      yield element


class AddFeatures(beam.DoFn):
  """Adds features from the claim text to a pCollection."""

  def __init__(self):
    self.claim_length = Metrics.distribution('main', 'claim_length')
    self.success_cnt = Metrics.counter('main', 'create_features_success')
    self.failed_cnt = Metrics.counter('main', 'failed_to_create_features')

  def process(self, element, patterns):
    """Adds a set of count based features to our PCollection."""
    try:
      first_claim = element.get('first_claim')
      self.claim_length.update(len(first_claim))
      element['word_cnt'] = wordcount(first_claim)
      element['word_cnt_unique'] = wordcount(first_claim, unique=True)
      element['char_cnt'] = len(first_claim)
      element['char_cnt_unique'] = len(set(first_claim))
      for key in patterns.keys():
        element[key] = pattern_count(patterns[key], first_claim)
      self.success_cnt.inc()
      yield element
    except Exception as e:
      self.failed_cnt.inc()
      logging.warn('Error %s while adding features to element %s', e, element)


def bytes_feature(value):
  """Creates a Tensorflow Feature proto from a list of bytes."""
  value = str(value).encode('utf-8')
  return tf.train.Feature(bytes_list=tf.train.BytesList(value=[value]))


def float_feature(value):
  """Creates a Tensorflow Feature proto from a list of floats."""
  return tf.train.Feature(float_list=tf.train.FloatList(value=value))


def int_feature(value):
  """Creates a TensorFlow Feature proto from a list of integers."""
  return tf.train.Feature(int64_list=tf.train.Int64List(value=value))


class TfExampleFromDict(beam.DoFn):
  """Converts pCollection of dictionaries into TF Example protobuffers."""

  def __init__(self):
    self.failed_cnt = Metrics.counter('main', 'failed_to_create_proto')
    self.success_cnt = Metrics.counter('main', 'create_proto_success')

  def process(self, element, int_features, is_inference=False):
    try:
      # Add a few context items from the original query.
      feature_mapping = {
          'publication_number': bytes_feature(element['publication_number']),
          'cpc4': bytes_feature(element['cpc4']),
          'priority_yr': int_feature([element['priority_yr']]),
      }

      if not is_inference:
        feature_mapping['label'] = bytes_feature(element['label'])

      # Add all the engineered features.
      for key in int_features:
        feature_mapping[key] = float_feature([int(element[key])])

      example = tf.train.Example(
          features=tf.train.Features(feature=feature_mapping)
      )
      self.success_cnt.inc()
      yield example
    except Exception as e:
      self.failed_cnt.inc()
      logging.warn(
          'Error %s while creating TFExample from element %s', e, element)


def default_args(argv):
  """Provides default values for Workflow flags."""
  parser = argparse.ArgumentParser()
  parser.add_argument(
      '--pipeline_mode',
      default='train',
      choices=['train', 'inference'],
      help='Indicates whether pipeline is generating training data or inference'
           'data. If `train` - output is split into 3 sets of files.')
  parser.add_argument(
      '--query_keep_pct',
      default=1.0,
      type=float,
      help='Used to keep a random subset of the query results when training.'
           'For inference, use 1.0')
  parser.add_argument(
      '--cpc_code_list',
      default='E,F',
      type=str,
      help='Comma separated string indicating the first letter of all CPC codes'
           'that should be included in results.')
  parser.add_argument(
      '--min_priority_year',
      default=1995,
      type=int,
      help='Earliest year to include in the data produced by pipeline.')
  parser.add_argument(
      '--output_path',
      required=True,
      help='Output directory for results. For DataflowRunner use a GCS bucket.')
  parser.add_argument(
      '--job_name',
      type=str,
      default='patent-claims-' + NOW,
      help='A unique job identifier.')
  parser.add_argument(
      '--num_workers',
      default=1,
      type=int,
      help='The initial number of workers to use.')
  parser.add_argument(
      '--max_num_workers',
      default=30,
      type=int,
      help='The maximum number of workers to use.')
  parser.add_argument(
      '--worker_machine_type',
      default='n1-highmem-4',
      type=str,
      help='The type of machine to use for each worker on GCP. See'
           'https://cloud.google.com/compute/docs/machine-types for options')
  parser.add_argument(
      '--runner',
      default='DirectRunner',
      choices=['DataflowRunner', 'DirectRunner'],
      help='Option to run locally or on GCP Cloud Dataflow service.')
  parser.add_argument(
      '--project',
      type=str,
      help='The cloud project name to be used for running this pipeline with'
           '--runner=DataflowRunner.')

  parsed_args, _ = parser.parse_known_args(argv)

  if parsed_args.runner == 'DataflowRunner':
    if not parsed_args.project:
      raise argparse.ArgumentTypeError(
          'If running with DataflowRunner please provide a GCP project.')

  # Setup some additional flags required with DataflowRunner.
  # These can be overridden via the command line.
  default_cloud_values = {
      'temp_location': os.path.join(parsed_args.output_path, 'tmp'),
      'staging_location': os.path.join(parsed_args.output_path, 'stg'),
      'save_main_session': True,
  }

  for kk, vv in default_cloud_values.iteritems():
    if kk not in parsed_args or not vars(parsed_args)[kk]:
      vars(parsed_args)[kk] = vv

  return parsed_args


def main(argv, query=None, await_completion=False):
  """Runs the Beam pipeline with args from user.

  Args:
     argv: commandline arguments from the user in raw string format.
     query: A string query to be executed. If `None` query is constructed based
       on input args.
     await_completion: Boolean indicating whether to keep python executing until
       pipeline finished.
  Returns:
    If await_comlpetion is true, returns Beam pipeline results, including any
    metrics logged during pipeline execution.
  """
  opt = default_args(argv)
  logging.info('Starting pipeline with args: %s', vars(opt))
  if not query:
    query = build_query_statement(
        opt.min_priority_year, opt.cpc_code_list, opt.query_keep_pct)
  pipeline_options = PipelineOptions().from_dictionary(vars(opt))
  p = beam.Pipeline(options=pipeline_options)
  logging.info('Query to be run: %s', query)
  data = p | 'BqInput' >> beam.io.Read(
      beam.io.BigQuerySource(query=query, use_standard_sql=True)
  )

  data = (data
          | 'ParseFirstClaim' >> beam.ParDo(GetFirstClaim())
          | 'AddFeatures' >> beam.ParDo(AddFeatures(), PATTERNS)
         )

  # Add a label and split into Train/Test/Eval.
  if opt.pipeline_mode == 'train':
    train_data = data | 'AddLabel' >> beam.ParDo(AddInferredClassLabel())
    splits = (train_data
              | 'TrainTestEvalSplit' >> beam.ParDo(
                  TrainTestSplit()).with_outputs('test', 'eval', main='train')
             )

    # Write 3 splits to Tensorflow Examples.
    for name, split in zip(['train', 'test', 'eval'], splits):
      tfr_path = os.path.join(opt.output_path, 'claim-data-{}'.format(name))
      _ = (split
           | 'CreateExampleProto-%s' % name >> beam.ParDo(
               TfExampleFromDict(), FEATURE_NAMES)
           | 'SerializeToString-%s' % name >> beam.Map(
               lambda x: x.SerializeToString())
           | 'WriteTFRecords-%s' % name >> beam.io.WriteToTFRecord(
               tfr_path, num_shards=15, file_name_suffix='.tfrecord.gz')
          )

  # If running an inference job, then generate examples for all records.
  if opt.pipeline_mode == 'inference':
    tfr_path = os.path.join(opt.output_path, 'claim-data-all-us-pubs')
    _ = (data
         | 'CreateExampleProto-alluS' >> beam.ParDo(
             TfExampleFromDict(), FEATURE_NAMES, is_inference=True)
         | 'SerializeToString-alluS'  >> beam.Map(
             lambda x: x.SerializeToString())
         | 'WriteTFRecords-alluS' >> beam.io.WriteToTFRecord(
             tfr_path, num_shards=30, file_name_suffix='.tfrecord.gz')
        )

  result = p.run()
  print('Pipeline running. visit https://console.cloud.google.com/dataflow to '
        'monitor progress.')
  if await_completion:
    result.wait_until_finish()
    return result


if __name__ == '__main__':
  main(sys.argv[1:])
