
---
geometry: margin=0.6in
---

# European Bioinformatics Institute


*****
## patents-public-data:ebi_chembl.action_type_23


Old table version `23`, schema skipped.





*****
## patents-public-data:ebi_chembl.action_type_24



> ChEMBL Data is a manually curated database of small molecules used in drug discovery, including information about existing patented drugs.
> 
> Schema: http://ftp.ebi.ac.uk/pub/databases/chembl/ChEMBLdb/releases/chembl_23/chembl_23_schema.png
> 
> Documentation: http://ftp.ebi.ac.uk/pub/databases/chembl/ChEMBLdb/releases/chembl_23/schema_documentation.html
> 
> “ChEMBL” by the European Bioinformatics Institute (EMBL-EBI), used under CC BY-SA 3.0. Modifications have been made to add normalized publication numbers.





| Stat | Value |
|----------|----------|
| Last updated | 2018-10-31 |
| Rows | 30 |
| Size | 3.9 kB |

### Schema
[View in BigQuery](https://bigquery.cloud.google.com/table/patents-public-data:ebi_chembl.action_type_24)

* `action_type` STRING NULLABLE 

* `description` STRING NULLABLE 

* `parent_type` STRING NULLABLE 














*****
## patents-public-data:ebi_chembl.activities_23


Old table version `23`, schema skipped.





*****
## patents-public-data:ebi_chembl.activities_24



> ChEMBL Data is a manually curated database of small molecules used in drug discovery, including information about existing patented drugs.
> 
> Schema: http://ftp.ebi.ac.uk/pub/databases/chembl/ChEMBLdb/releases/chembl_23/chembl_23_schema.png
> 
> Documentation: http://ftp.ebi.ac.uk/pub/databases/chembl/ChEMBLdb/releases/chembl_23/schema_documentation.html
> 
> “ChEMBL” by the European Bioinformatics Institute (EMBL-EBI), used under CC BY-SA 3.0. Modifications have been made to add normalized publication numbers.





| Stat | Value |
|----------|----------|
| Last updated | 2018-10-31 |
| Rows | 15,207,914 |
| Size | 2.6 GB |

### Schema
[View in BigQuery](https://bigquery.cloud.google.com/table/patents-public-data:ebi_chembl.activities_24)

* `activity_id` STRING NULLABLE 

* `assay_id` STRING NULLABLE 

* `doc_id` STRING NULLABLE 

* `record_id` STRING NULLABLE 

* `molregno` STRING NULLABLE  joins on **ChEMBL molregno**

* `standard_relation` STRING NULLABLE 

* `published_value` STRING NULLABLE 

* `published_units` STRING NULLABLE 

* `standard_value` STRING NULLABLE 

* `standard_units` STRING NULLABLE 

* `standard_flag` STRING NULLABLE 

* `standard_type` STRING NULLABLE 

* `activity_comment` STRING NULLABLE 

* `published_type` STRING NULLABLE 

* `data_validity_comment` STRING NULLABLE 

* `potential_duplicate` STRING NULLABLE 

* `published_relation` STRING NULLABLE 

* `pchembl_value` STRING NULLABLE 

* `bao_endpoint` STRING NULLABLE 

* `uo_units` STRING NULLABLE 

* `qudt_units` STRING NULLABLE 

* `toid` STRING NULLABLE 

* `upper_value` STRING NULLABLE 

* `standard_upper_value` STRING NULLABLE 

* `src_id` STRING NULLABLE 

* `type` STRING NULLABLE 

* `relation` STRING NULLABLE 

* `value` STRING NULLABLE 

* `units` STRING NULLABLE 

* `text_value` STRING NULLABLE 

* `standard_text_value` STRING NULLABLE 



### Join columns










#### molregno

joins to `patents-public-data:ebi_chembl.compound_properties_24::molregno` on **ChEMBL molregno** (99.59%, 15,145,635 rows)

| Key | Percent | Rows | Sample values |
|------|-----|--------|--------------------------------------------------------|
| `all` | 99.59% | 15,145,635 | `['371327', '571326', '1336649', '758484', '1000807']` |


    #standardSQL
    SELECT
      COUNT(*) AS cnt,
      COUNT(second.second_column) AS second_cnt,
      ARRAY_AGG(first.molregno IGNORE NULLS ORDER BY RAND() LIMIT 5) AS sample_value
    FROM `patents-public-data.ebi_chembl.activities_24`AS first
    LEFT JOIN (
      SELECT molregno AS second_column, COUNT(*) AS cnt
      FROM `patents-public-data.ebi_chembl.compound_properties_24`
      GROUP BY 1
    ) AS second ON first.molregno = second.second_column



joins from `patents-public-data:ebi_chembl.compound_properties_24::molregno` on **ChEMBL molregno** (95.16%, 1,735,006 rows)


























































*****
## patents-public-data:ebi_chembl.activity_properties_24



> ChEMBL Data is a manually curated database of small molecules used in drug discovery, including information about existing patented drugs.
> 
> Schema: http://ftp.ebi.ac.uk/pub/databases/chembl/ChEMBLdb/releases/chembl_23/chembl_23_schema.png
> 
> Documentation: http://ftp.ebi.ac.uk/pub/databases/chembl/ChEMBLdb/releases/chembl_23/schema_documentation.html
> 
> “ChEMBL” by the European Bioinformatics Institute (EMBL-EBI), used under CC BY-SA 3.0. Modifications have been made to add normalized publication numbers.





| Stat | Value |
|----------|----------|
| Last updated | 2018-10-31 |
| Rows | 5,339,435 |
| Size | 371.2 MB |

### Schema
[View in BigQuery](https://bigquery.cloud.google.com/table/patents-public-data:ebi_chembl.activity_properties_24)

* `ap_id` STRING NULLABLE 

* `activity_id` STRING NULLABLE 

* `type` STRING NULLABLE 

* `relation` STRING NULLABLE 

* `value` STRING NULLABLE 

* `units` STRING NULLABLE 

* `text_value` STRING NULLABLE 

* `standard_type` STRING NULLABLE 

* `standard_relation` STRING NULLABLE 

* `standard_value` STRING NULLABLE 

* `standard_units` STRING NULLABLE 

* `standard_text_value` STRING NULLABLE 

* `comments` STRING NULLABLE 

* `result_flag` STRING NULLABLE 




































*****
## patents-public-data:ebi_chembl.activity_smid_24



> ChEMBL Data is a manually curated database of small molecules used in drug discovery, including information about existing patented drugs.
> 
> Schema: http://ftp.ebi.ac.uk/pub/databases/chembl/ChEMBLdb/releases/chembl_23/chembl_23_schema.png
> 
> Documentation: http://ftp.ebi.ac.uk/pub/databases/chembl/ChEMBLdb/releases/chembl_23/schema_documentation.html
> 
> “ChEMBL” by the European Bioinformatics Institute (EMBL-EBI), used under CC BY-SA 3.0. Modifications have been made to add normalized publication numbers.





| Stat | Value |
|----------|----------|
| Last updated | 2018-10-31 |
| Rows | 1,723,378 |
| Size | 14.4 MB |

### Schema
[View in BigQuery](https://bigquery.cloud.google.com/table/patents-public-data:ebi_chembl.activity_smid_24)

* `smid` STRING NULLABLE 










*****
## patents-public-data:ebi_chembl.activity_stds_lookup_23


Old table version `23`, schema skipped.





*****
## patents-public-data:ebi_chembl.activity_stds_lookup_24



> ChEMBL Data is a manually curated database of small molecules used in drug discovery, including information about existing patented drugs.
> 
> Schema: http://ftp.ebi.ac.uk/pub/databases/chembl/ChEMBLdb/releases/chembl_23/chembl_23_schema.png
> 
> Documentation: http://ftp.ebi.ac.uk/pub/databases/chembl/ChEMBLdb/releases/chembl_23/schema_documentation.html
> 
> “ChEMBL” by the European Bioinformatics Institute (EMBL-EBI), used under CC BY-SA 3.0. Modifications have been made to add normalized publication numbers.





| Stat | Value |
|----------|----------|
| Last updated | 2018-10-31 |
| Rows | 144 |
| Size | 11.9 kB |

### Schema
[View in BigQuery](https://bigquery.cloud.google.com/table/patents-public-data:ebi_chembl.activity_stds_lookup_24)

* `std_act_id` STRING NULLABLE 

* `standard_type` STRING NULLABLE 

* `definition` STRING NULLABLE 

* `standard_units` STRING NULLABLE 

* `normal_range_min` STRING NULLABLE 

* `normal_range_max` STRING NULLABLE 




















*****
## patents-public-data:ebi_chembl.activity_supp_24



> ChEMBL Data is a manually curated database of small molecules used in drug discovery, including information about existing patented drugs.
> 
> Schema: http://ftp.ebi.ac.uk/pub/databases/chembl/ChEMBLdb/releases/chembl_23/chembl_23_schema.png
> 
> Documentation: http://ftp.ebi.ac.uk/pub/databases/chembl/ChEMBLdb/releases/chembl_23/schema_documentation.html
> 
> “ChEMBL” by the European Bioinformatics Institute (EMBL-EBI), used under CC BY-SA 3.0. Modifications have been made to add normalized publication numbers.





| Stat | Value |
|----------|----------|
| Last updated | 2018-10-31 |
| Rows | 1,723,378 |
| Size | 194.6 MB |

### Schema
[View in BigQuery](https://bigquery.cloud.google.com/table/patents-public-data:ebi_chembl.activity_supp_24)

* `as_id` STRING NULLABLE 

* `rgid` STRING NULLABLE 

* `smid` STRING NULLABLE 

* `type` STRING NULLABLE 

* `relation` STRING NULLABLE 

* `value` STRING NULLABLE 

* `units` STRING NULLABLE 

* `text_value` STRING NULLABLE 

* `standard_type` STRING NULLABLE 

* `standard_relation` STRING NULLABLE 

* `standard_value` STRING NULLABLE 

* `standard_units` STRING NULLABLE 

* `standard_text_value` STRING NULLABLE 

* `comments` STRING NULLABLE 




































*****
## patents-public-data:ebi_chembl.activity_supp_map_24



> ChEMBL Data is a manually curated database of small molecules used in drug discovery, including information about existing patented drugs.
> 
> Schema: http://ftp.ebi.ac.uk/pub/databases/chembl/ChEMBLdb/releases/chembl_23/chembl_23_schema.png
> 
> Documentation: http://ftp.ebi.ac.uk/pub/databases/chembl/ChEMBLdb/releases/chembl_23/schema_documentation.html
> 
> “ChEMBL” by the European Bioinformatics Institute (EMBL-EBI), used under CC BY-SA 3.0. Modifications have been made to add normalized publication numbers.





| Stat | Value |
|----------|----------|
| Last updated | 2018-10-31 |
| Rows | 2,005,362 |
| Size | 37.0 MB |

### Schema
[View in BigQuery](https://bigquery.cloud.google.com/table/patents-public-data:ebi_chembl.activity_supp_map_24)

* `activity_id` STRING NULLABLE 

* `smid` STRING NULLABLE 












*****
## patents-public-data:ebi_chembl.assay_parameters_23


Old table version `23`, schema skipped.





*****
## patents-public-data:ebi_chembl.assay_parameters_24



> ChEMBL Data is a manually curated database of small molecules used in drug discovery, including information about existing patented drugs.
> 
> Schema: http://ftp.ebi.ac.uk/pub/databases/chembl/ChEMBLdb/releases/chembl_23/chembl_23_schema.png
> 
> Documentation: http://ftp.ebi.ac.uk/pub/databases/chembl/ChEMBLdb/releases/chembl_23/schema_documentation.html
> 
> “ChEMBL” by the European Bioinformatics Institute (EMBL-EBI), used under CC BY-SA 3.0. Modifications have been made to add normalized publication numbers.





| Stat | Value |
|----------|----------|
| Last updated | 2018-10-31 |
| Rows | 267,387 |
| Size | 15.3 MB |

### Schema
[View in BigQuery](https://bigquery.cloud.google.com/table/patents-public-data:ebi_chembl.assay_parameters_24)

* `assay_param_id` STRING NULLABLE 

* `assay_id` STRING NULLABLE 

* `type` STRING NULLABLE 

* `relation` STRING NULLABLE 

* `value` STRING NULLABLE 

* `units` STRING NULLABLE 

* `text_value` STRING NULLABLE 

* `standard_type` STRING NULLABLE 

* `standard_relation` STRING NULLABLE 

* `standard_value` STRING NULLABLE 

* `standard_units` STRING NULLABLE 

* `standard_text_value` STRING NULLABLE 

* `comments` STRING NULLABLE 


































*****
## patents-public-data:ebi_chembl.assay_type_23


Old table version `23`, schema skipped.





*****
## patents-public-data:ebi_chembl.assay_type_24



> ChEMBL Data is a manually curated database of small molecules used in drug discovery, including information about existing patented drugs.
> 
> Schema: http://ftp.ebi.ac.uk/pub/databases/chembl/ChEMBLdb/releases/chembl_23/chembl_23_schema.png
> 
> Documentation: http://ftp.ebi.ac.uk/pub/databases/chembl/ChEMBLdb/releases/chembl_23/schema_documentation.html
> 
> “ChEMBL” by the European Bioinformatics Institute (EMBL-EBI), used under CC BY-SA 3.0. Modifications have been made to add normalized publication numbers.





| Stat | Value |
|----------|----------|
| Last updated | 2018-10-31 |
| Rows | 6 |
| Size | 84 Bytes |

### Schema
[View in BigQuery](https://bigquery.cloud.google.com/table/patents-public-data:ebi_chembl.assay_type_24)

* `assay_type` STRING NULLABLE 

* `assay_desc` STRING NULLABLE 












*****
## patents-public-data:ebi_chembl.assays_23


Old table version `23`, schema skipped.





*****
## patents-public-data:ebi_chembl.assays_24



> ChEMBL Data is a manually curated database of small molecules used in drug discovery, including information about existing patented drugs.
> 
> Schema: http://ftp.ebi.ac.uk/pub/databases/chembl/ChEMBLdb/releases/chembl_23/chembl_23_schema.png
> 
> Documentation: http://ftp.ebi.ac.uk/pub/databases/chembl/ChEMBLdb/releases/chembl_23/schema_documentation.html
> 
> “ChEMBL” by the European Bioinformatics Institute (EMBL-EBI), used under CC BY-SA 3.0. Modifications have been made to add normalized publication numbers.





| Stat | Value |
|----------|----------|
| Last updated | 2018-10-31 |
| Rows | 1,060,283 |
| Size | 243.2 MB |

### Schema
[View in BigQuery](https://bigquery.cloud.google.com/table/patents-public-data:ebi_chembl.assays_24)

* `assay_id` STRING NULLABLE 

* `doc_id` STRING NULLABLE 

* `description` STRING NULLABLE 

* `assay_type` STRING NULLABLE 

* `assay_test_type` STRING NULLABLE 

* `assay_category` STRING NULLABLE 

* `assay_organism` STRING NULLABLE 

* `assay_tax_id` STRING NULLABLE 

* `assay_strain` STRING NULLABLE 

* `assay_tissue` STRING NULLABLE 

* `assay_cell_type` STRING NULLABLE 

* `assay_subcellular_fraction` STRING NULLABLE 

* `tid` STRING NULLABLE 

* `relationship_type` STRING NULLABLE 

* `confidence_score` STRING NULLABLE 

* `curated_by` STRING NULLABLE 

* `src_id` STRING NULLABLE 

* `src_assay_id` STRING NULLABLE 

* `chembl_id` STRING NULLABLE 

* `cell_id` STRING NULLABLE 

* `bao_format` STRING NULLABLE 

* `tissue_id` STRING NULLABLE 

* `variant_id` STRING NULLABLE 

* `aidx` STRING NULLABLE 
























































*****
## patents-public-data:ebi_chembl.atc_classification_23


Old table version `23`, schema skipped.





*****
## patents-public-data:ebi_chembl.atc_classification_24



> ChEMBL Data is a manually curated database of small molecules used in drug discovery, including information about existing patented drugs.
> 
> Schema: http://ftp.ebi.ac.uk/pub/databases/chembl/ChEMBLdb/releases/chembl_23/chembl_23_schema.png
> 
> Documentation: http://ftp.ebi.ac.uk/pub/databases/chembl/ChEMBLdb/releases/chembl_23/schema_documentation.html
> 
> “ChEMBL” by the European Bioinformatics Institute (EMBL-EBI), used under CC BY-SA 3.0. Modifications have been made to add normalized publication numbers.





| Stat | Value |
|----------|----------|
| Last updated | 2018-10-31 |
| Rows | 4,886 |
| Size | 819.3 kB |

### Schema
[View in BigQuery](https://bigquery.cloud.google.com/table/patents-public-data:ebi_chembl.atc_classification_24)

* `who_name` STRING NULLABLE 

* `level1` STRING NULLABLE 

* `level2` STRING NULLABLE 

* `level3` STRING NULLABLE 

* `level4` STRING NULLABLE 

* `level5` STRING NULLABLE 

* `level1_description` STRING NULLABLE 

* `level2_description` STRING NULLABLE 

* `level3_description` STRING NULLABLE 

* `level4_description` STRING NULLABLE 




























*****
## patents-public-data:ebi_chembl.binding_sites_23


Old table version `23`, schema skipped.





*****
## patents-public-data:ebi_chembl.binding_sites_24



> ChEMBL Data is a manually curated database of small molecules used in drug discovery, including information about existing patented drugs.
> 
> Schema: http://ftp.ebi.ac.uk/pub/databases/chembl/ChEMBLdb/releases/chembl_23/chembl_23_schema.png
> 
> Documentation: http://ftp.ebi.ac.uk/pub/databases/chembl/ChEMBLdb/releases/chembl_23/schema_documentation.html
> 
> “ChEMBL” by the European Bioinformatics Institute (EMBL-EBI), used under CC BY-SA 3.0. Modifications have been made to add normalized publication numbers.





| Stat | Value |
|----------|----------|
| Last updated | 2018-10-31 |
| Rows | 9,483 |
| Size | 672.6 kB |

### Schema
[View in BigQuery](https://bigquery.cloud.google.com/table/patents-public-data:ebi_chembl.binding_sites_24)

* `site_id` STRING NULLABLE 

* `site_name` STRING NULLABLE 

* `tid` STRING NULLABLE 














*****
## patents-public-data:ebi_chembl.bio_component_sequences_23


Old table version `23`, schema skipped.





*****
## patents-public-data:ebi_chembl.bio_component_sequences_24



> ChEMBL Data is a manually curated database of small molecules used in drug discovery, including information about existing patented drugs.
> 
> Schema: http://ftp.ebi.ac.uk/pub/databases/chembl/ChEMBLdb/releases/chembl_23/chembl_23_schema.png
> 
> Documentation: http://ftp.ebi.ac.uk/pub/databases/chembl/ChEMBLdb/releases/chembl_23/schema_documentation.html
> 
> “ChEMBL” by the European Bioinformatics Institute (EMBL-EBI), used under CC BY-SA 3.0. Modifications have been made to add normalized publication numbers.





| Stat | Value |
|----------|----------|
| Last updated | 2018-10-31 |
| Rows | 629 |
| Size | 276.0 kB |

### Schema
[View in BigQuery](https://bigquery.cloud.google.com/table/patents-public-data:ebi_chembl.bio_component_sequences_24)

* `component_id` STRING NULLABLE 

* `component_type` STRING NULLABLE 

* `description` STRING NULLABLE 

* `sequence` STRING NULLABLE 

* `sequence_md5sum` STRING NULLABLE 

* `tax_id` STRING NULLABLE 

* `organism` STRING NULLABLE 






















*****
## patents-public-data:ebi_chembl.bioassay_ontology_23


Old table version `23`, schema skipped.





*****
## patents-public-data:ebi_chembl.bioassay_ontology_24



> ChEMBL Data is a manually curated database of small molecules used in drug discovery, including information about existing patented drugs.
> 
> Schema: http://ftp.ebi.ac.uk/pub/databases/chembl/ChEMBLdb/releases/chembl_23/chembl_23_schema.png
> 
> Documentation: http://ftp.ebi.ac.uk/pub/databases/chembl/ChEMBLdb/releases/chembl_23/schema_documentation.html
> 
> “ChEMBL” by the European Bioinformatics Institute (EMBL-EBI), used under CC BY-SA 3.0. Modifications have been made to add normalized publication numbers.





| Stat | Value |
|----------|----------|
| Last updated | 2018-10-31 |
| Rows | 311 |
| Size | 10.4 kB |

### Schema
[View in BigQuery](https://bigquery.cloud.google.com/table/patents-public-data:ebi_chembl.bioassay_ontology_24)

* `bao_id` STRING NULLABLE 

* `label` STRING NULLABLE 












*****
## patents-public-data:ebi_chembl.biotherapeutic_components_23


Old table version `23`, schema skipped.





*****
## patents-public-data:ebi_chembl.biotherapeutic_components_24



> ChEMBL Data is a manually curated database of small molecules used in drug discovery, including information about existing patented drugs.
> 
> Schema: http://ftp.ebi.ac.uk/pub/databases/chembl/ChEMBLdb/releases/chembl_23/chembl_23_schema.png
> 
> Documentation: http://ftp.ebi.ac.uk/pub/databases/chembl/ChEMBLdb/releases/chembl_23/schema_documentation.html
> 
> “ChEMBL” by the European Bioinformatics Institute (EMBL-EBI), used under CC BY-SA 3.0. Modifications have been made to add normalized publication numbers.





| Stat | Value |
|----------|----------|
| Last updated | 2018-10-31 |
| Rows | 663 |
| Size | 13.1 kB |

### Schema
[View in BigQuery](https://bigquery.cloud.google.com/table/patents-public-data:ebi_chembl.biotherapeutic_components_24)

* `biocomp_id` STRING NULLABLE 

* `molregno` STRING NULLABLE  joins on **ChEMBL molregno**

* `component_id` STRING NULLABLE 



### Join columns




#### molregno

joins to `patents-public-data:ebi_chembl.compound_properties_24::molregno` on **ChEMBL molregno** (1.21%, 8 rows)

| Key | Percent | Rows | Sample values |
|------|-----|--------|--------------------------------------------------------|
| `all` | 1.21% | 8 | `['1121856', '2197902', '1121901', '2197884', '2197894']` |


    #standardSQL
    SELECT
      COUNT(*) AS cnt,
      COUNT(second.second_column) AS second_cnt,
      ARRAY_AGG(first.molregno IGNORE NULLS ORDER BY RAND() LIMIT 5) AS sample_value
    FROM `patents-public-data.ebi_chembl.biotherapeutic_components_24`AS first
    LEFT JOIN (
      SELECT molregno AS second_column, COUNT(*) AS cnt
      FROM `patents-public-data.ebi_chembl.compound_properties_24`
      GROUP BY 1
    ) AS second ON first.molregno = second.second_column



joins from `patents-public-data:ebi_chembl.compound_properties_24::molregno` on **ChEMBL molregno** (0.00%, 8 rows)








*****
## patents-public-data:ebi_chembl.biotherapeutics_23


Old table version `23`, schema skipped.





*****
## patents-public-data:ebi_chembl.biotherapeutics_24



> ChEMBL Data is a manually curated database of small molecules used in drug discovery, including information about existing patented drugs.
> 
> Schema: http://ftp.ebi.ac.uk/pub/databases/chembl/ChEMBLdb/releases/chembl_23/chembl_23_schema.png
> 
> Documentation: http://ftp.ebi.ac.uk/pub/databases/chembl/ChEMBLdb/releases/chembl_23/schema_documentation.html
> 
> “ChEMBL” by the European Bioinformatics Institute (EMBL-EBI), used under CC BY-SA 3.0. Modifications have been made to add normalized publication numbers.





| Stat | Value |
|----------|----------|
| Last updated | 2018-10-31 |
| Rows | 21,310 |
| Size | 1.7 MB |

### Schema
[View in BigQuery](https://bigquery.cloud.google.com/table/patents-public-data:ebi_chembl.biotherapeutics_24)

* `molregno` STRING NULLABLE  joins on **ChEMBL molregno**

* `description` STRING NULLABLE 

* `helm_notation` STRING NULLABLE 



### Join columns


#### molregno

joins to `patents-public-data:ebi_chembl.compound_properties_24::molregno` on **ChEMBL molregno** (95.98%, 20,454 rows)

| Key | Percent | Rows | Sample values |
|------|-----|--------|--------------------------------------------------------|
| `all` | 95.98% | 20,454 | `['702913', '1959503', '2197309', '506748', '1731700']` |


    #standardSQL
    SELECT
      COUNT(*) AS cnt,
      COUNT(second.second_column) AS second_cnt,
      ARRAY_AGG(first.molregno IGNORE NULLS ORDER BY RAND() LIMIT 5) AS sample_value
    FROM `patents-public-data.ebi_chembl.biotherapeutics_24`AS first
    LEFT JOIN (
      SELECT molregno AS second_column, COUNT(*) AS cnt
      FROM `patents-public-data.ebi_chembl.compound_properties_24`
      GROUP BY 1
    ) AS second ON first.molregno = second.second_column



joins from `patents-public-data:ebi_chembl.compound_properties_24::molregno` on **ChEMBL molregno** (1.12%, 20,454 rows)










*****
## patents-public-data:ebi_chembl.cell_dictionary_23


Old table version `23`, schema skipped.





*****
## patents-public-data:ebi_chembl.cell_dictionary_24



> ChEMBL Data is a manually curated database of small molecules used in drug discovery, including information about existing patented drugs.
> 
> Schema: http://ftp.ebi.ac.uk/pub/databases/chembl/ChEMBLdb/releases/chembl_23/chembl_23_schema.png
> 
> Documentation: http://ftp.ebi.ac.uk/pub/databases/chembl/ChEMBLdb/releases/chembl_23/schema_documentation.html
> 
> “ChEMBL” by the European Bioinformatics Institute (EMBL-EBI), used under CC BY-SA 3.0. Modifications have been made to add normalized publication numbers.





| Stat | Value |
|----------|----------|
| Last updated | 2018-10-31 |
| Rows | 1,667 |
| Size | 161.1 kB |

### Schema
[View in BigQuery](https://bigquery.cloud.google.com/table/patents-public-data:ebi_chembl.cell_dictionary_24)

* `cell_id` STRING NULLABLE 

* `cell_name` STRING NULLABLE 

* `cell_description` STRING NULLABLE 

* `cell_source_tissue` STRING NULLABLE 

* `cell_source_organism` STRING NULLABLE 

* `cell_source_tax_id` STRING NULLABLE 

* `clo_id` STRING NULLABLE 

* `efo_id` STRING NULLABLE 

* `cellosaurus_id` STRING NULLABLE 

* `cl_lincs_id` STRING NULLABLE 

* `chembl_id` STRING NULLABLE 






























*****
## patents-public-data:ebi_chembl.chembl_id_lookup_23


Old table version `23`, schema skipped.





*****
## patents-public-data:ebi_chembl.chembl_id_lookup_24



> ChEMBL Data is a manually curated database of small molecules used in drug discovery, including information about existing patented drugs.
> 
> Schema: http://ftp.ebi.ac.uk/pub/databases/chembl/ChEMBLdb/releases/chembl_23/chembl_23_schema.png
> 
> Documentation: http://ftp.ebi.ac.uk/pub/databases/chembl/ChEMBLdb/releases/chembl_23/schema_documentation.html
> 
> “ChEMBL” by the European Bioinformatics Institute (EMBL-EBI), used under CC BY-SA 3.0. Modifications have been made to add normalized publication numbers.





| Stat | Value |
|----------|----------|
| Last updated | 2018-10-31 |
| Rows | 3,377,372 |
| Size | 133.9 MB |

### Schema
[View in BigQuery](https://bigquery.cloud.google.com/table/patents-public-data:ebi_chembl.chembl_id_lookup_24)

* `chembl_id` STRING NULLABLE 

* `entity_type` STRING NULLABLE 

* `entity_id` STRING NULLABLE 

* `status` STRING NULLABLE 
















*****
## patents-public-data:ebi_chembl.component_class_23


Old table version `23`, schema skipped.





*****
## patents-public-data:ebi_chembl.component_class_24



> ChEMBL Data is a manually curated database of small molecules used in drug discovery, including information about existing patented drugs.
> 
> Schema: http://ftp.ebi.ac.uk/pub/databases/chembl/ChEMBLdb/releases/chembl_23/chembl_23_schema.png
> 
> Documentation: http://ftp.ebi.ac.uk/pub/databases/chembl/ChEMBLdb/releases/chembl_23/schema_documentation.html
> 
> “ChEMBL” by the European Bioinformatics Institute (EMBL-EBI), used under CC BY-SA 3.0. Modifications have been made to add normalized publication numbers.





| Stat | Value |
|----------|----------|
| Last updated | 2018-10-31 |
| Rows | 9,005 |
| Size | 145.3 kB |

### Schema
[View in BigQuery](https://bigquery.cloud.google.com/table/patents-public-data:ebi_chembl.component_class_24)

* `component_id` STRING NULLABLE 

* `protein_class_id` STRING NULLABLE 

* `comp_class_id` STRING NULLABLE 














*****
## patents-public-data:ebi_chembl.component_domains_23


Old table version `23`, schema skipped.





*****
## patents-public-data:ebi_chembl.component_domains_24



> ChEMBL Data is a manually curated database of small molecules used in drug discovery, including information about existing patented drugs.
> 
> Schema: http://ftp.ebi.ac.uk/pub/databases/chembl/ChEMBLdb/releases/chembl_23/chembl_23_schema.png
> 
> Documentation: http://ftp.ebi.ac.uk/pub/databases/chembl/ChEMBLdb/releases/chembl_23/schema_documentation.html
> 
> “ChEMBL” by the European Bioinformatics Institute (EMBL-EBI), used under CC BY-SA 3.0. Modifications have been made to add normalized publication numbers.





| Stat | Value |
|----------|----------|
| Last updated | 2018-10-31 |
| Rows | 18,821 |
| Size | 540.6 kB |

### Schema
[View in BigQuery](https://bigquery.cloud.google.com/table/patents-public-data:ebi_chembl.component_domains_24)

* `compd_id` STRING NULLABLE 

* `domain_id` STRING NULLABLE 

* `component_id` STRING NULLABLE 

* `start_position` STRING NULLABLE 

* `end_position` STRING NULLABLE 


















*****
## patents-public-data:ebi_chembl.component_go_23


Old table version `23`, schema skipped.





*****
## patents-public-data:ebi_chembl.component_go_24



> ChEMBL Data is a manually curated database of small molecules used in drug discovery, including information about existing patented drugs.
> 
> Schema: http://ftp.ebi.ac.uk/pub/databases/chembl/ChEMBLdb/releases/chembl_23/chembl_23_schema.png
> 
> Documentation: http://ftp.ebi.ac.uk/pub/databases/chembl/ChEMBLdb/releases/chembl_23/schema_documentation.html
> 
> “ChEMBL” by the European Bioinformatics Institute (EMBL-EBI), used under CC BY-SA 3.0. Modifications have been made to add normalized publication numbers.





| Stat | Value |
|----------|----------|
| Last updated | 2018-10-31 |
| Rows | 117,496 |
| Size | 3.0 MB |

### Schema
[View in BigQuery](https://bigquery.cloud.google.com/table/patents-public-data:ebi_chembl.component_go_24)

* `comp_go_id` STRING NULLABLE 

* `component_id` STRING NULLABLE 

* `go_id` STRING NULLABLE 














*****
## patents-public-data:ebi_chembl.component_sequences_23


Old table version `23`, schema skipped.





*****
## patents-public-data:ebi_chembl.component_sequences_24



> ChEMBL Data is a manually curated database of small molecules used in drug discovery, including information about existing patented drugs.
> 
> Schema: http://ftp.ebi.ac.uk/pub/databases/chembl/ChEMBLdb/releases/chembl_23/chembl_23_schema.png
> 
> Documentation: http://ftp.ebi.ac.uk/pub/databases/chembl/ChEMBLdb/releases/chembl_23/schema_documentation.html
> 
> “ChEMBL” by the European Bioinformatics Institute (EMBL-EBI), used under CC BY-SA 3.0. Modifications have been made to add normalized publication numbers.





| Stat | Value |
|----------|----------|
| Last updated | 2018-10-31 |
| Rows | 8,835 |
| Size | 6.3 MB |

### Schema
[View in BigQuery](https://bigquery.cloud.google.com/table/patents-public-data:ebi_chembl.component_sequences_24)

* `component_id` STRING NULLABLE 

* `component_type` STRING NULLABLE 

* `accession` STRING NULLABLE 

* `sequence` STRING NULLABLE 

* `sequence_md5sum` STRING NULLABLE 

* `description` STRING NULLABLE 

* `tax_id` STRING NULLABLE 

* `organism` STRING NULLABLE 

* `db_source` STRING NULLABLE 

* `db_version` STRING NULLABLE 




























*****
## patents-public-data:ebi_chembl.component_synonyms_23


Old table version `23`, schema skipped.





*****
## patents-public-data:ebi_chembl.component_synonyms_24



> ChEMBL Data is a manually curated database of small molecules used in drug discovery, including information about existing patented drugs.
> 
> Schema: http://ftp.ebi.ac.uk/pub/databases/chembl/ChEMBLdb/releases/chembl_23/chembl_23_schema.png
> 
> Documentation: http://ftp.ebi.ac.uk/pub/databases/chembl/ChEMBLdb/releases/chembl_23/schema_documentation.html
> 
> “ChEMBL” by the European Bioinformatics Institute (EMBL-EBI), used under CC BY-SA 3.0. Modifications have been made to add normalized publication numbers.





| Stat | Value |
|----------|----------|
| Last updated | 2018-10-31 |
| Rows | 57,149 |
| Size | 2.5 MB |

### Schema
[View in BigQuery](https://bigquery.cloud.google.com/table/patents-public-data:ebi_chembl.component_synonyms_24)

* `compsyn_id` STRING NULLABLE 

* `component_id` STRING NULLABLE 

* `component_synonym` STRING NULLABLE 

* `syn_type` STRING NULLABLE 
















*****
## patents-public-data:ebi_chembl.compound_properties_23


Old table version `23`, schema skipped.





*****
## patents-public-data:ebi_chembl.compound_properties_24



> ChEMBL Data is a manually curated database of small molecules used in drug discovery, including information about existing patented drugs.
> 
> Schema: http://ftp.ebi.ac.uk/pub/databases/chembl/ChEMBLdb/releases/chembl_23/chembl_23_schema.png
> 
> Documentation: http://ftp.ebi.ac.uk/pub/databases/chembl/ChEMBLdb/releases/chembl_23/schema_documentation.html
> 
> “ChEMBL” by the European Bioinformatics Institute (EMBL-EBI), used under CC BY-SA 3.0. Modifications have been made to add normalized publication numbers.





| Stat | Value |
|----------|----------|
| Last updated | 2018-10-31 |
| Rows | 1,823,191 |
| Size | 218.3 MB |

### Schema
[View in BigQuery](https://bigquery.cloud.google.com/table/patents-public-data:ebi_chembl.compound_properties_24)

* `molregno` STRING NULLABLE  joins on **ChEMBL molregno**

* `mw_freebase` STRING NULLABLE 

* `alogp` STRING NULLABLE 

* `hba` STRING NULLABLE 

* `hbd` STRING NULLABLE 

* `psa` STRING NULLABLE 

* `rtb` STRING NULLABLE 

* `ro3_pass` STRING NULLABLE 

* `num_ro5_violations` STRING NULLABLE 

* `acd_most_apka` STRING NULLABLE 

* `acd_most_bpka` STRING NULLABLE 

* `acd_logp` STRING NULLABLE 

* `acd_logd` STRING NULLABLE 

* `molecular_species` STRING NULLABLE 

* `full_mwt` STRING NULLABLE 

* `aromatic_rings` STRING NULLABLE 

* `heavy_atoms` STRING NULLABLE 

* `qed_weighted` STRING NULLABLE 

* `mw_monoisotopic` STRING NULLABLE 

* `full_molformula` STRING NULLABLE 

* `hba_lipinski` STRING NULLABLE 

* `hbd_lipinski` STRING NULLABLE 

* `num_lipinski_ro5_violations` STRING NULLABLE 



### Join columns


#### molregno

joins to `patents-public-data:ebi_chembl.activities_24::molregno` on **ChEMBL molregno** (95.16%, 1,735,006 rows)

| Key | Percent | Rows | Sample values |
|------|-----|--------|--------------------------------------------------------|
| `all` | 95.16% | 1,735,006 | `['382806', '888949', '557958', '629843', '2060649']` |


    #standardSQL
    SELECT
      COUNT(*) AS cnt,
      COUNT(second.second_column) AS second_cnt,
      ARRAY_AGG(first.molregno IGNORE NULLS ORDER BY RAND() LIMIT 5) AS sample_value
    FROM `patents-public-data.ebi_chembl.compound_properties_24`AS first
    LEFT JOIN (
      SELECT molregno AS second_column, COUNT(*) AS cnt
      FROM `patents-public-data.ebi_chembl.activities_24`
      GROUP BY 1
    ) AS second ON first.molregno = second.second_column


joins to `patents-public-data:ebi_chembl.biotherapeutic_components_24::molregno` on **ChEMBL molregno** (0.00%, 8 rows)

| Key | Percent | Rows | Sample values |
|------|-----|--------|--------------------------------------------------------|
| `all` | 0.00% | 8 | `['1571723', '1915682', '594570', '2034388', '577592']` |


    #standardSQL
    SELECT
      COUNT(*) AS cnt,
      COUNT(second.second_column) AS second_cnt,
      ARRAY_AGG(first.molregno IGNORE NULLS ORDER BY RAND() LIMIT 5) AS sample_value
    FROM `patents-public-data.ebi_chembl.compound_properties_24`AS first
    LEFT JOIN (
      SELECT molregno AS second_column, COUNT(*) AS cnt
      FROM `patents-public-data.ebi_chembl.biotherapeutic_components_24`
      GROUP BY 1
    ) AS second ON first.molregno = second.second_column


joins to `patents-public-data:ebi_chembl.biotherapeutics_24::molregno` on **ChEMBL molregno** (1.12%, 20,454 rows)

| Key | Percent | Rows | Sample values |
|------|-----|--------|--------------------------------------------------------|
| `all` | 1.12% | 20,454 | `['1986269', '1020375', '252010', '1350551', '193887']` |


    #standardSQL
    SELECT
      COUNT(*) AS cnt,
      COUNT(second.second_column) AS second_cnt,
      ARRAY_AGG(first.molregno IGNORE NULLS ORDER BY RAND() LIMIT 5) AS sample_value
    FROM `patents-public-data.ebi_chembl.compound_properties_24`AS first
    LEFT JOIN (
      SELECT molregno AS second_column, COUNT(*) AS cnt
      FROM `patents-public-data.ebi_chembl.biotherapeutics_24`
      GROUP BY 1
    ) AS second ON first.molregno = second.second_column


joins to `patents-public-data:ebi_chembl.compound_records_24::molregno` on **ChEMBL molregno** (95.56%, 1,742,279 rows)

| Key | Percent | Rows | Sample values |
|------|-----|--------|--------------------------------------------------------|
| `all` | 95.56% | 1,742,279 | `['782768', '835927', '1518131', '856191', '1093807']` |


    #standardSQL
    SELECT
      COUNT(*) AS cnt,
      COUNT(second.second_column) AS second_cnt,
      ARRAY_AGG(first.molregno IGNORE NULLS ORDER BY RAND() LIMIT 5) AS sample_value
    FROM `patents-public-data.ebi_chembl.compound_properties_24`AS first
    LEFT JOIN (
      SELECT molregno AS second_column, COUNT(*) AS cnt
      FROM `patents-public-data.ebi_chembl.compound_records_24`
      GROUP BY 1
    ) AS second ON first.molregno = second.second_column


joins to `patents-public-data:ebi_chembl.compound_structural_alerts_24::molregno` on **ChEMBL molregno** (70.47%, 1,284,776 rows)

| Key | Percent | Rows | Sample values |
|------|-----|--------|--------------------------------------------------------|
| `all` | 70.47% | 1,284,776 | `['1838894', '2145582', '268148', '647333', '964029']` |


    #standardSQL
    SELECT
      COUNT(*) AS cnt,
      COUNT(second.second_column) AS second_cnt,
      ARRAY_AGG(first.molregno IGNORE NULLS ORDER BY RAND() LIMIT 5) AS sample_value
    FROM `patents-public-data.ebi_chembl.compound_properties_24`AS first
    LEFT JOIN (
      SELECT molregno AS second_column, COUNT(*) AS cnt
      FROM `patents-public-data.ebi_chembl.compound_structural_alerts_24`
      GROUP BY 1
    ) AS second ON first.molregno = second.second_column


joins to `patents-public-data:ebi_chembl.compound_structures_24::molregno` on **ChEMBL molregno** (99.83%, 1,820,030 rows)

| Key | Percent | Rows | Sample values |
|------|-----|--------|--------------------------------------------------------|
| `all` | 99.83% | 1,820,030 | `['125291', '656810', '835435', '406641', '2075271']` |


    #standardSQL
    SELECT
      COUNT(*) AS cnt,
      COUNT(second.second_column) AS second_cnt,
      ARRAY_AGG(first.molregno IGNORE NULLS ORDER BY RAND() LIMIT 5) AS sample_value
    FROM `patents-public-data.ebi_chembl.compound_properties_24`AS first
    LEFT JOIN (
      SELECT molregno AS second_column, COUNT(*) AS cnt
      FROM `patents-public-data.ebi_chembl.compound_structures_24`
      GROUP BY 1
    ) AS second ON first.molregno = second.second_column


joins to `patents-public-data:ebi_chembl.drug_indication_24::molregno` on **ChEMBL molregno** (0.21%, 3,743 rows)

| Key | Percent | Rows | Sample values |
|------|-----|--------|--------------------------------------------------------|
| `all` | 0.21% | 3,743 | `['1798186', '167025', '799976', '1837450', '1330405']` |


    #standardSQL
    SELECT
      COUNT(*) AS cnt,
      COUNT(second.second_column) AS second_cnt,
      ARRAY_AGG(first.molregno IGNORE NULLS ORDER BY RAND() LIMIT 5) AS sample_value
    FROM `patents-public-data.ebi_chembl.compound_properties_24`AS first
    LEFT JOIN (
      SELECT molregno AS second_column, COUNT(*) AS cnt
      FROM `patents-public-data.ebi_chembl.drug_indication_24`
      GROUP BY 1
    ) AS second ON first.molregno = second.second_column


joins to `patents-public-data:ebi_chembl.drug_mechanism_24::molregno` on **ChEMBL molregno** (0.15%, 2,721 rows)

| Key | Percent | Rows | Sample values |
|------|-----|--------|--------------------------------------------------------|
| `all` | 0.15% | 2,721 | `['1998132', '355169', '1012651', '1952911', '1879238']` |


    #standardSQL
    SELECT
      COUNT(*) AS cnt,
      COUNT(second.second_column) AS second_cnt,
      ARRAY_AGG(first.molregno IGNORE NULLS ORDER BY RAND() LIMIT 5) AS sample_value
    FROM `patents-public-data.ebi_chembl.compound_properties_24`AS first
    LEFT JOIN (
      SELECT molregno AS second_column, COUNT(*) AS cnt
      FROM `patents-public-data.ebi_chembl.drug_mechanism_24`
      GROUP BY 1
    ) AS second ON first.molregno = second.second_column


joins to `patents-public-data:ebi_chembl.formulations_24::molregno` on **ChEMBL molregno** (0.10%, 1,868 rows)

| Key | Percent | Rows | Sample values |
|------|-----|--------|--------------------------------------------------------|
| `all` | 0.10% | 1,868 | `['66797', '503205', '1741721', '1052506', '414141']` |


    #standardSQL
    SELECT
      COUNT(*) AS cnt,
      COUNT(second.second_column) AS second_cnt,
      ARRAY_AGG(first.molregno IGNORE NULLS ORDER BY RAND() LIMIT 5) AS sample_value
    FROM `patents-public-data.ebi_chembl.compound_properties_24`AS first
    LEFT JOIN (
      SELECT molregno AS second_column, COUNT(*) AS cnt
      FROM `patents-public-data.ebi_chembl.formulations_24`
      GROUP BY 1
    ) AS second ON first.molregno = second.second_column


joins to `patents-public-data:ebi_chembl.molecule_atc_classification_24::molregno` on **ChEMBL molregno** (0.16%, 2,833 rows)

| Key | Percent | Rows | Sample values |
|------|-----|--------|--------------------------------------------------------|
| `all` | 0.16% | 2,833 | `['516016', '290765', '1534708', '1039831', '2107167']` |


    #standardSQL
    SELECT
      COUNT(*) AS cnt,
      COUNT(second.second_column) AS second_cnt,
      ARRAY_AGG(first.molregno IGNORE NULLS ORDER BY RAND() LIMIT 5) AS sample_value
    FROM `patents-public-data.ebi_chembl.compound_properties_24`AS first
    LEFT JOIN (
      SELECT molregno AS second_column, COUNT(*) AS cnt
      FROM `patents-public-data.ebi_chembl.molecule_atc_classification_24`
      GROUP BY 1
    ) AS second ON first.molregno = second.second_column


joins to `patents-public-data:ebi_chembl.molecule_dictionary_24::molregno` on **ChEMBL molregno** (100.00%, 1,823,191 rows)

| Key | Percent | Rows | Sample values |
|------|-----|--------|--------------------------------------------------------|
| `all` | 100.00% | 1,823,191 | `['1242732', '1533399', '1876919', '876914', '843638']` |


    #standardSQL
    SELECT
      COUNT(*) AS cnt,
      COUNT(second.second_column) AS second_cnt,
      ARRAY_AGG(first.molregno IGNORE NULLS ORDER BY RAND() LIMIT 5) AS sample_value
    FROM `patents-public-data.ebi_chembl.compound_properties_24`AS first
    LEFT JOIN (
      SELECT molregno AS second_column, COUNT(*) AS cnt
      FROM `patents-public-data.ebi_chembl.molecule_dictionary_24`
      GROUP BY 1
    ) AS second ON first.molregno = second.second_column


joins to `patents-public-data:ebi_chembl.molecule_frac_classification_24::molregno` on **ChEMBL molregno** (0.01%, 145 rows)

| Key | Percent | Rows | Sample values |
|------|-----|--------|--------------------------------------------------------|
| `all` | 0.01% | 145 | `['2191787', '2007381', '629923', '1996253', '614593']` |


    #standardSQL
    SELECT
      COUNT(*) AS cnt,
      COUNT(second.second_column) AS second_cnt,
      ARRAY_AGG(first.molregno IGNORE NULLS ORDER BY RAND() LIMIT 5) AS sample_value
    FROM `patents-public-data.ebi_chembl.compound_properties_24`AS first
    LEFT JOIN (
      SELECT molregno AS second_column, COUNT(*) AS cnt
      FROM `patents-public-data.ebi_chembl.molecule_frac_classification_24`
      GROUP BY 1
    ) AS second ON first.molregno = second.second_column


joins to `patents-public-data:ebi_chembl.molecule_hierarchy_24::molregno` on **ChEMBL molregno** (95.66%, 1,744,111 rows)

| Key | Percent | Rows | Sample values |
|------|-----|--------|--------------------------------------------------------|
| `all` | 95.66% | 1,744,111 | `['886653', '832805', '1376448', '808262', '1572273']` |


    #standardSQL
    SELECT
      COUNT(*) AS cnt,
      COUNT(second.second_column) AS second_cnt,
      ARRAY_AGG(first.molregno IGNORE NULLS ORDER BY RAND() LIMIT 5) AS sample_value
    FROM `patents-public-data.ebi_chembl.compound_properties_24`AS first
    LEFT JOIN (
      SELECT molregno AS second_column, COUNT(*) AS cnt
      FROM `patents-public-data.ebi_chembl.molecule_hierarchy_24`
      GROUP BY 1
    ) AS second ON first.molregno = second.second_column


joins to `patents-public-data:ebi_chembl.molecule_hrac_classification_24::molregno` on **ChEMBL molregno** (0.01%, 203 rows)

| Key | Percent | Rows | Sample values |
|------|-----|--------|--------------------------------------------------------|
| `all` | 0.01% | 203 | `['1281504', '2126352', '2028597', '19421', '743200']` |


    #standardSQL
    SELECT
      COUNT(*) AS cnt,
      COUNT(second.second_column) AS second_cnt,
      ARRAY_AGG(first.molregno IGNORE NULLS ORDER BY RAND() LIMIT 5) AS sample_value
    FROM `patents-public-data.ebi_chembl.compound_properties_24`AS first
    LEFT JOIN (
      SELECT molregno AS second_column, COUNT(*) AS cnt
      FROM `patents-public-data.ebi_chembl.molecule_hrac_classification_24`
      GROUP BY 1
    ) AS second ON first.molregno = second.second_column


joins to `patents-public-data:ebi_chembl.molecule_irac_classification_24::molregno` on **ChEMBL molregno** (0.01%, 185 rows)

| Key | Percent | Rows | Sample values |
|------|-----|--------|--------------------------------------------------------|
| `all` | 0.01% | 185 | `['1511687', '1725533', '243611', '2166823', '951831']` |


    #standardSQL
    SELECT
      COUNT(*) AS cnt,
      COUNT(second.second_column) AS second_cnt,
      ARRAY_AGG(first.molregno IGNORE NULLS ORDER BY RAND() LIMIT 5) AS sample_value
    FROM `patents-public-data.ebi_chembl.compound_properties_24`AS first
    LEFT JOIN (
      SELECT molregno AS second_column, COUNT(*) AS cnt
      FROM `patents-public-data.ebi_chembl.molecule_irac_classification_24`
      GROUP BY 1
    ) AS second ON first.molregno = second.second_column


joins to `patents-public-data:ebi_chembl.molecule_synonyms_24::molregno` on **ChEMBL molregno** (4.54%, 82,838 rows)

| Key | Percent | Rows | Sample values |
|------|-----|--------|--------------------------------------------------------|
| `all` | 4.54% | 82,838 | `['2121510', '14510', '852939', '1971426', '37097']` |


    #standardSQL
    SELECT
      COUNT(*) AS cnt,
      COUNT(second.second_column) AS second_cnt,
      ARRAY_AGG(first.molregno IGNORE NULLS ORDER BY RAND() LIMIT 5) AS sample_value
    FROM `patents-public-data.ebi_chembl.compound_properties_24`AS first
    LEFT JOIN (
      SELECT molregno AS second_column, COUNT(*) AS cnt
      FROM `patents-public-data.ebi_chembl.molecule_synonyms_24`
      GROUP BY 1
    ) AS second ON first.molregno = second.second_column



joins from `patents-public-data:ebi_chembl.activities_24::molregno` on **ChEMBL molregno** (99.59%, 15,145,635 rows)

joins from `patents-public-data:ebi_chembl.biotherapeutic_components_24::molregno` on **ChEMBL molregno** (1.21%, 8 rows)

joins from `patents-public-data:ebi_chembl.biotherapeutics_24::molregno` on **ChEMBL molregno** (95.98%, 20,454 rows)

joins from `patents-public-data:ebi_chembl.compound_records_24::molregno` on **ChEMBL molregno** (99.69%, 2,268,901 rows)

joins from `patents-public-data:ebi_chembl.compound_structural_alerts_24::molregno` on **ChEMBL molregno** (100.00%, 5,477,519 rows)

joins from `patents-public-data:ebi_chembl.compound_structures_24::molregno` on **ChEMBL molregno** (100.00%, 1,820,030 rows)

joins from `patents-public-data:ebi_chembl.drug_indication_24::molregno` on **ChEMBL molregno** (80.62%, 23,512 rows)

joins from `patents-public-data:ebi_chembl.drug_mechanism_24::molregno` on **ChEMBL molregno** (72.08%, 3,598 rows)

joins from `patents-public-data:ebi_chembl.formulations_24::molregno` on **ChEMBL molregno** (96.31%, 39,824 rows)

joins from `patents-public-data:ebi_chembl.molecule_atc_classification_24::molregno` on **ChEMBL molregno** (89.44%, 3,810 rows)

joins from `patents-public-data:ebi_chembl.molecule_dictionary_24::molregno` on **ChEMBL molregno** (99.69%, 1,823,191 rows)

joins from `patents-public-data:ebi_chembl.molecule_frac_classification_24::molregno` on **ChEMBL molregno** (100.00%, 145 rows)

joins from `patents-public-data:ebi_chembl.molecule_hierarchy_24::molregno` on **ChEMBL molregno** (99.68%, 1,744,111 rows)

joins from `patents-public-data:ebi_chembl.molecule_hrac_classification_24::molregno` on **ChEMBL molregno** (100.00%, 205 rows)

joins from `patents-public-data:ebi_chembl.molecule_irac_classification_24::molregno` on **ChEMBL molregno** (100.00%, 185 rows)

joins from `patents-public-data:ebi_chembl.molecule_synonyms_24::molregno` on **ChEMBL molregno** (94.48%, 146,753 rows)


















































*****
## patents-public-data:ebi_chembl.compound_records_23


Old table version `23`, schema skipped.





*****
## patents-public-data:ebi_chembl.compound_records_24



> ChEMBL Data is a manually curated database of small molecules used in drug discovery, including information about existing patented drugs.
> 
> Schema: http://ftp.ebi.ac.uk/pub/databases/chembl/ChEMBLdb/releases/chembl_23/chembl_23_schema.png
> 
> Documentation: http://ftp.ebi.ac.uk/pub/databases/chembl/ChEMBLdb/releases/chembl_23/schema_documentation.html
> 
> “ChEMBL” by the European Bioinformatics Institute (EMBL-EBI), used under CC BY-SA 3.0. Modifications have been made to add normalized publication numbers.





| Stat | Value |
|----------|----------|
| Last updated | 2018-10-31 |
| Rows | 2,275,906 |
| Size | 234.2 MB |

### Schema
[View in BigQuery](https://bigquery.cloud.google.com/table/patents-public-data:ebi_chembl.compound_records_24)

* `record_id` STRING NULLABLE 

* `molregno` STRING NULLABLE  joins on **ChEMBL molregno**

* `doc_id` STRING NULLABLE 

* `compound_key` STRING NULLABLE 

* `compound_name` STRING NULLABLE 

* `src_id` STRING NULLABLE 

* `src_compound_id` STRING NULLABLE 

* `cidx` STRING NULLABLE 



### Join columns




#### molregno

joins to `patents-public-data:ebi_chembl.compound_properties_24::molregno` on **ChEMBL molregno** (99.69%, 2,268,901 rows)

| Key | Percent | Rows | Sample values |
|------|-----|--------|--------------------------------------------------------|
| `all` | 99.69% | 2,268,901 | `['225204', '2056139', '274191', '1678857', '3854']` |


    #standardSQL
    SELECT
      COUNT(*) AS cnt,
      COUNT(second.second_column) AS second_cnt,
      ARRAY_AGG(first.molregno IGNORE NULLS ORDER BY RAND() LIMIT 5) AS sample_value
    FROM `patents-public-data.ebi_chembl.compound_records_24`AS first
    LEFT JOIN (
      SELECT molregno AS second_column, COUNT(*) AS cnt
      FROM `patents-public-data.ebi_chembl.compound_properties_24`
      GROUP BY 1
    ) AS second ON first.molregno = second.second_column



joins from `patents-public-data:ebi_chembl.compound_properties_24::molregno` on **ChEMBL molregno** (95.56%, 1,742,279 rows)


















*****
## patents-public-data:ebi_chembl.compound_structural_alerts_23


Old table version `23`, schema skipped.





*****
## patents-public-data:ebi_chembl.compound_structural_alerts_24



> ChEMBL Data is a manually curated database of small molecules used in drug discovery, including information about existing patented drugs.
> 
> Schema: http://ftp.ebi.ac.uk/pub/databases/chembl/ChEMBLdb/releases/chembl_23/chembl_23_schema.png
> 
> Documentation: http://ftp.ebi.ac.uk/pub/databases/chembl/ChEMBLdb/releases/chembl_23/schema_documentation.html
> 
> “ChEMBL” by the European Bioinformatics Institute (EMBL-EBI), used under CC BY-SA 3.0. Modifications have been made to add normalized publication numbers.





| Stat | Value |
|----------|----------|
| Last updated | 2018-10-31 |
| Rows | 5,477,519 |
| Size | 124.3 MB |

### Schema
[View in BigQuery](https://bigquery.cloud.google.com/table/patents-public-data:ebi_chembl.compound_structural_alerts_24)

* `cpd_str_alert_id` STRING NULLABLE 

* `molregno` STRING NULLABLE  joins on **ChEMBL molregno**

* `alert_id` STRING NULLABLE 



### Join columns




#### molregno

joins to `patents-public-data:ebi_chembl.compound_properties_24::molregno` on **ChEMBL molregno** (100.00%, 5,477,519 rows)

| Key | Percent | Rows | Sample values |
|------|-----|--------|--------------------------------------------------------|
| `all` | 100.00% | 5,477,519 | `['116840', '2117811', '331273', '1578999', '778907']` |


    #standardSQL
    SELECT
      COUNT(*) AS cnt,
      COUNT(second.second_column) AS second_cnt,
      ARRAY_AGG(first.molregno IGNORE NULLS ORDER BY RAND() LIMIT 5) AS sample_value
    FROM `patents-public-data.ebi_chembl.compound_structural_alerts_24`AS first
    LEFT JOIN (
      SELECT molregno AS second_column, COUNT(*) AS cnt
      FROM `patents-public-data.ebi_chembl.compound_properties_24`
      GROUP BY 1
    ) AS second ON first.molregno = second.second_column



joins from `patents-public-data:ebi_chembl.compound_properties_24::molregno` on **ChEMBL molregno** (70.47%, 1,284,776 rows)








*****
## patents-public-data:ebi_chembl.compound_structures_23


Old table version `23`, schema skipped.





*****
## patents-public-data:ebi_chembl.compound_structures_24



> ChEMBL Data is a manually curated database of small molecules used in drug discovery, including information about existing patented drugs.
> 
> Schema: http://ftp.ebi.ac.uk/pub/databases/chembl/ChEMBLdb/releases/chembl_23/chembl_23_schema.png
> 
> Documentation: http://ftp.ebi.ac.uk/pub/databases/chembl/ChEMBLdb/releases/chembl_23/schema_documentation.html
> 
> “ChEMBL” by the European Bioinformatics Institute (EMBL-EBI), used under CC BY-SA 3.0. Modifications have been made to add normalized publication numbers.





| Stat | Value |
|----------|----------|
| Last updated | 2018-10-31 |
| Rows | 1,820,035 |
| Size | 4.3 GB |

### Schema
[View in BigQuery](https://bigquery.cloud.google.com/table/patents-public-data:ebi_chembl.compound_structures_24)

* `molregno` STRING NULLABLE  joins on **ChEMBL molregno**

* `molfile` STRING NULLABLE 

* `standard_inchi` STRING NULLABLE 

* `standard_inchi_key` STRING NULLABLE 

* `canonical_smiles` STRING NULLABLE 



### Join columns


#### molregno

joins to `patents-public-data:ebi_chembl.compound_properties_24::molregno` on **ChEMBL molregno** (100.00%, 1,820,030 rows)

| Key | Percent | Rows | Sample values |
|------|-----|--------|--------------------------------------------------------|
| `all` | 100.00% | 1,820,030 | `['116833', '1792073', '589285', '1898867', '1570138']` |


    #standardSQL
    SELECT
      COUNT(*) AS cnt,
      COUNT(second.second_column) AS second_cnt,
      ARRAY_AGG(first.molregno IGNORE NULLS ORDER BY RAND() LIMIT 5) AS sample_value
    FROM `patents-public-data.ebi_chembl.compound_structures_24`AS first
    LEFT JOIN (
      SELECT molregno AS second_column, COUNT(*) AS cnt
      FROM `patents-public-data.ebi_chembl.compound_properties_24`
      GROUP BY 1
    ) AS second ON first.molregno = second.second_column



joins from `patents-public-data:ebi_chembl.compound_properties_24::molregno` on **ChEMBL molregno** (99.83%, 1,820,030 rows)














*****
## patents-public-data:ebi_chembl.confidence_score_lookup_23


Old table version `23`, schema skipped.





*****
## patents-public-data:ebi_chembl.confidence_score_lookup_24



> ChEMBL Data is a manually curated database of small molecules used in drug discovery, including information about existing patented drugs.
> 
> Schema: http://ftp.ebi.ac.uk/pub/databases/chembl/ChEMBLdb/releases/chembl_23/chembl_23_schema.png
> 
> Documentation: http://ftp.ebi.ac.uk/pub/databases/chembl/ChEMBLdb/releases/chembl_23/schema_documentation.html
> 
> “ChEMBL” by the European Bioinformatics Institute (EMBL-EBI), used under CC BY-SA 3.0. Modifications have been made to add normalized publication numbers.





| Stat | Value |
|----------|----------|
| Last updated | 2018-10-31 |
| Rows | 10 |
| Size | 681 Bytes |

### Schema
[View in BigQuery](https://bigquery.cloud.google.com/table/patents-public-data:ebi_chembl.confidence_score_lookup_24)

* `confidence_score` STRING NULLABLE 

* `description` STRING NULLABLE 

* `target_mapping` STRING NULLABLE 














*****
## patents-public-data:ebi_chembl.curation_lookup_23


Old table version `23`, schema skipped.





*****
## patents-public-data:ebi_chembl.curation_lookup_24



> ChEMBL Data is a manually curated database of small molecules used in drug discovery, including information about existing patented drugs.
> 
> Schema: http://ftp.ebi.ac.uk/pub/databases/chembl/ChEMBLdb/releases/chembl_23/chembl_23_schema.png
> 
> Documentation: http://ftp.ebi.ac.uk/pub/databases/chembl/ChEMBLdb/releases/chembl_23/schema_documentation.html
> 
> “ChEMBL” by the European Bioinformatics Institute (EMBL-EBI), used under CC BY-SA 3.0. Modifications have been made to add normalized publication numbers.





| Stat | Value |
|----------|----------|
| Last updated | 2018-10-31 |
| Rows | 3 |
| Size | 214 Bytes |

### Schema
[View in BigQuery](https://bigquery.cloud.google.com/table/patents-public-data:ebi_chembl.curation_lookup_24)

* `curated_by` STRING NULLABLE 

* `description` STRING NULLABLE 












*****
## patents-public-data:ebi_chembl.data_validity_lookup_23


Old table version `23`, schema skipped.





*****
## patents-public-data:ebi_chembl.data_validity_lookup_24



> ChEMBL Data is a manually curated database of small molecules used in drug discovery, including information about existing patented drugs.
> 
> Schema: http://ftp.ebi.ac.uk/pub/databases/chembl/ChEMBLdb/releases/chembl_23/chembl_23_schema.png
> 
> Documentation: http://ftp.ebi.ac.uk/pub/databases/chembl/ChEMBLdb/releases/chembl_23/schema_documentation.html
> 
> “ChEMBL” by the European Bioinformatics Institute (EMBL-EBI), used under CC BY-SA 3.0. Modifications have been made to add normalized publication numbers.





| Stat | Value |
|----------|----------|
| Last updated | 2018-10-31 |
| Rows | 7 |
| Size | 804 Bytes |

### Schema
[View in BigQuery](https://bigquery.cloud.google.com/table/patents-public-data:ebi_chembl.data_validity_lookup_24)

* `data_validity_comment` STRING NULLABLE 

* `description` STRING NULLABLE 












*****
## patents-public-data:ebi_chembl.defined_daily_dose_23


Old table version `23`, schema skipped.





*****
## patents-public-data:ebi_chembl.defined_daily_dose_24



> ChEMBL Data is a manually curated database of small molecules used in drug discovery, including information about existing patented drugs.
> 
> Schema: http://ftp.ebi.ac.uk/pub/databases/chembl/ChEMBLdb/releases/chembl_23/chembl_23_schema.png
> 
> Documentation: http://ftp.ebi.ac.uk/pub/databases/chembl/ChEMBLdb/releases/chembl_23/schema_documentation.html
> 
> “ChEMBL” by the European Bioinformatics Institute (EMBL-EBI), used under CC BY-SA 3.0. Modifications have been made to add normalized publication numbers.





| Stat | Value |
|----------|----------|
| Last updated | 2018-10-31 |
| Rows | 2,456 |
| Size | 66.9 kB |

### Schema
[View in BigQuery](https://bigquery.cloud.google.com/table/patents-public-data:ebi_chembl.defined_daily_dose_24)

* `atc_code` STRING NULLABLE 

* `ddd_units` STRING NULLABLE 

* `ddd_admr` STRING NULLABLE 

* `ddd_comment` STRING NULLABLE 

* `ddd_id` STRING NULLABLE 

* `ddd_value` STRING NULLABLE 




















*****
## patents-public-data:ebi_chembl.docs_23


Old table version `23`, schema skipped.





*****
## patents-public-data:ebi_chembl.docs_24



> ChEMBL Data is a manually curated database of small molecules used in drug discovery, including information about existing patented drugs.
> 
> Schema: http://ftp.ebi.ac.uk/pub/databases/chembl/ChEMBLdb/releases/chembl_23/chembl_23_schema.png
> 
> Documentation: http://ftp.ebi.ac.uk/pub/databases/chembl/ChEMBLdb/releases/chembl_23/schema_documentation.html
> 
> “ChEMBL” by the European Bioinformatics Institute (EMBL-EBI), used under CC BY-SA 3.0. Modifications have been made to add normalized publication numbers.





| Stat | Value |
|----------|----------|
| Last updated | 2018-10-31 |
| Rows | 69,861 |
| Size | 75.5 MB |

### Schema
[View in BigQuery](https://bigquery.cloud.google.com/table/patents-public-data:ebi_chembl.docs_24)

* `doc_id` STRING NULLABLE 

* `journal` STRING NULLABLE 

* `year` STRING NULLABLE 

* `volume` STRING NULLABLE 

* `issue` STRING NULLABLE 

* `first_page` STRING NULLABLE 

* `last_page` STRING NULLABLE 

* `pubmed_id` STRING NULLABLE 

* `doi` STRING NULLABLE 

* `chembl_id` STRING NULLABLE 

* `title` STRING NULLABLE 

* `doc_type` STRING NULLABLE 

* `authors` STRING NULLABLE 

* `abstract` STRING NULLABLE 

* `patent_id` STRING NULLABLE 

* `ridx` STRING NULLABLE 

* `src_id` STRING NULLABLE 










































*****
## patents-public-data:ebi_chembl.domains_23


Old table version `23`, schema skipped.





*****
## patents-public-data:ebi_chembl.domains_24



> ChEMBL Data is a manually curated database of small molecules used in drug discovery, including information about existing patented drugs.
> 
> Schema: http://ftp.ebi.ac.uk/pub/databases/chembl/ChEMBLdb/releases/chembl_23/chembl_23_schema.png
> 
> Documentation: http://ftp.ebi.ac.uk/pub/databases/chembl/ChEMBLdb/releases/chembl_23/schema_documentation.html
> 
> “ChEMBL” by the European Bioinformatics Institute (EMBL-EBI), used under CC BY-SA 3.0. Modifications have been made to add normalized publication numbers.





| Stat | Value |
|----------|----------|
| Last updated | 2018-10-31 |
| Rows | 2,722 |
| Size | 93.0 kB |

### Schema
[View in BigQuery](https://bigquery.cloud.google.com/table/patents-public-data:ebi_chembl.domains_24)

* `domain_id` STRING NULLABLE 

* `domain_type` STRING NULLABLE 

* `source_domain_id` STRING NULLABLE 

* `domain_name` STRING NULLABLE 

* `domain_description` STRING NULLABLE 


















*****
## patents-public-data:ebi_chembl.drug_indication_23


Old table version `23`, schema skipped.





*****
## patents-public-data:ebi_chembl.drug_indication_24



> ChEMBL Data is a manually curated database of small molecules used in drug discovery, including information about existing patented drugs.
> 
> Schema: http://ftp.ebi.ac.uk/pub/databases/chembl/ChEMBLdb/releases/chembl_23/chembl_23_schema.png
> 
> Documentation: http://ftp.ebi.ac.uk/pub/databases/chembl/ChEMBLdb/releases/chembl_23/schema_documentation.html
> 
> “ChEMBL” by the European Bioinformatics Institute (EMBL-EBI), used under CC BY-SA 3.0. Modifications have been made to add normalized publication numbers.





| Stat | Value |
|----------|----------|
| Last updated | 2018-10-31 |
| Rows | 29,163 |
| Size | 2.6 MB |

### Schema
[View in BigQuery](https://bigquery.cloud.google.com/table/patents-public-data:ebi_chembl.drug_indication_24)

* `drugind_id` STRING NULLABLE 

* `record_id` STRING NULLABLE 

* `molregno` STRING NULLABLE  joins on **ChEMBL molregno**

* `max_phase_for_ind` STRING NULLABLE 

* `mesh_id` STRING NULLABLE 

* `mesh_heading` STRING NULLABLE 

* `efo_id` STRING NULLABLE 

* `efo_term` STRING NULLABLE 



### Join columns






#### molregno

joins to `patents-public-data:ebi_chembl.compound_properties_24::molregno` on **ChEMBL molregno** (80.62%, 23,512 rows)

| Key | Percent | Rows | Sample values |
|------|-----|--------|--------------------------------------------------------|
| `all` | 80.62% | 23,512 | `['1380352', '4730', '1626763', '1381852', '520664']` |


    #standardSQL
    SELECT
      COUNT(*) AS cnt,
      COUNT(second.second_column) AS second_cnt,
      ARRAY_AGG(first.molregno IGNORE NULLS ORDER BY RAND() LIMIT 5) AS sample_value
    FROM `patents-public-data.ebi_chembl.drug_indication_24`AS first
    LEFT JOIN (
      SELECT molregno AS second_column, COUNT(*) AS cnt
      FROM `patents-public-data.ebi_chembl.compound_properties_24`
      GROUP BY 1
    ) AS second ON first.molregno = second.second_column



joins from `patents-public-data:ebi_chembl.compound_properties_24::molregno` on **ChEMBL molregno** (0.21%, 3,743 rows)
















*****
## patents-public-data:ebi_chembl.drug_mechanism_23


Old table version `23`, schema skipped.





*****
## patents-public-data:ebi_chembl.drug_mechanism_24



> ChEMBL Data is a manually curated database of small molecules used in drug discovery, including information about existing patented drugs.
> 
> Schema: http://ftp.ebi.ac.uk/pub/databases/chembl/ChEMBLdb/releases/chembl_23/chembl_23_schema.png
> 
> Documentation: http://ftp.ebi.ac.uk/pub/databases/chembl/ChEMBLdb/releases/chembl_23/schema_documentation.html
> 
> “ChEMBL” by the European Bioinformatics Institute (EMBL-EBI), used under CC BY-SA 3.0. Modifications have been made to add normalized publication numbers.





| Stat | Value |
|----------|----------|
| Last updated | 2018-10-31 |
| Rows | 4,992 |
| Size | 694.4 kB |

### Schema
[View in BigQuery](https://bigquery.cloud.google.com/table/patents-public-data:ebi_chembl.drug_mechanism_24)

* `mec_id` STRING NULLABLE 

* `record_id` STRING NULLABLE 

* `molregno` STRING NULLABLE  joins on **ChEMBL molregno**

* `mechanism_of_action` STRING NULLABLE 

* `tid` STRING NULLABLE 

* `site_id` STRING NULLABLE 

* `action_type` STRING NULLABLE 

* `direct_interaction` STRING NULLABLE 

* `molecular_mechanism` STRING NULLABLE 

* `disease_efficacy` STRING NULLABLE 

* `mechanism_comment` STRING NULLABLE 

* `selectivity_comment` STRING NULLABLE 

* `binding_site_comment` STRING NULLABLE 



### Join columns






#### molregno

joins to `patents-public-data:ebi_chembl.compound_properties_24::molregno` on **ChEMBL molregno** (72.08%, 3,598 rows)

| Key | Percent | Rows | Sample values |
|------|-----|--------|--------------------------------------------------------|
| `all` | 72.08% | 3,598 | `['476314', '235143', '1380150', '682106', '1121294']` |


    #standardSQL
    SELECT
      COUNT(*) AS cnt,
      COUNT(second.second_column) AS second_cnt,
      ARRAY_AGG(first.molregno IGNORE NULLS ORDER BY RAND() LIMIT 5) AS sample_value
    FROM `patents-public-data.ebi_chembl.drug_mechanism_24`AS first
    LEFT JOIN (
      SELECT molregno AS second_column, COUNT(*) AS cnt
      FROM `patents-public-data.ebi_chembl.compound_properties_24`
      GROUP BY 1
    ) AS second ON first.molregno = second.second_column



joins from `patents-public-data:ebi_chembl.compound_properties_24::molregno` on **ChEMBL molregno** (0.15%, 2,721 rows)


























*****
## patents-public-data:ebi_chembl.formulations_23


Old table version `23`, schema skipped.





*****
## patents-public-data:ebi_chembl.formulations_24



> ChEMBL Data is a manually curated database of small molecules used in drug discovery, including information about existing patented drugs.
> 
> Schema: http://ftp.ebi.ac.uk/pub/databases/chembl/ChEMBLdb/releases/chembl_23/chembl_23_schema.png
> 
> Documentation: http://ftp.ebi.ac.uk/pub/databases/chembl/ChEMBLdb/releases/chembl_23/schema_documentation.html
> 
> “ChEMBL” by the European Bioinformatics Institute (EMBL-EBI), used under CC BY-SA 3.0. Modifications have been made to add normalized publication numbers.





| Stat | Value |
|----------|----------|
| Last updated | 2018-10-31 |
| Rows | 41,348 |
| Size | 3.2 MB |

### Schema
[View in BigQuery](https://bigquery.cloud.google.com/table/patents-public-data:ebi_chembl.formulations_24)

* `product_id` STRING NULLABLE 

* `ingredient` STRING NULLABLE 

* `strength` STRING NULLABLE 

* `record_id` STRING NULLABLE 

* `molregno` STRING NULLABLE  joins on **ChEMBL molregno**

* `formulation_id` STRING NULLABLE 



### Join columns










#### molregno

joins to `patents-public-data:ebi_chembl.compound_properties_24::molregno` on **ChEMBL molregno** (96.31%, 39,824 rows)

| Key | Percent | Rows | Sample values |
|------|-----|--------|--------------------------------------------------------|
| `all` | 96.31% | 39,824 | `['1676284', '386457', '674619', '32869', '8873']` |


    #standardSQL
    SELECT
      COUNT(*) AS cnt,
      COUNT(second.second_column) AS second_cnt,
      ARRAY_AGG(first.molregno IGNORE NULLS ORDER BY RAND() LIMIT 5) AS sample_value
    FROM `patents-public-data.ebi_chembl.formulations_24`AS first
    LEFT JOIN (
      SELECT molregno AS second_column, COUNT(*) AS cnt
      FROM `patents-public-data.ebi_chembl.compound_properties_24`
      GROUP BY 1
    ) AS second ON first.molregno = second.second_column



joins from `patents-public-data:ebi_chembl.compound_properties_24::molregno` on **ChEMBL molregno** (0.10%, 1,868 rows)








*****
## patents-public-data:ebi_chembl.frac_classification_23


Old table version `23`, schema skipped.





*****
## patents-public-data:ebi_chembl.frac_classification_24



> ChEMBL Data is a manually curated database of small molecules used in drug discovery, including information about existing patented drugs.
> 
> Schema: http://ftp.ebi.ac.uk/pub/databases/chembl/ChEMBLdb/releases/chembl_23/chembl_23_schema.png
> 
> Documentation: http://ftp.ebi.ac.uk/pub/databases/chembl/ChEMBLdb/releases/chembl_23/schema_documentation.html
> 
> “ChEMBL” by the European Bioinformatics Institute (EMBL-EBI), used under CC BY-SA 3.0. Modifications have been made to add normalized publication numbers.





| Stat | Value |
|----------|----------|
| Last updated | 2018-10-31 |
| Rows | 217 |
| Size | 37.2 kB |

### Schema
[View in BigQuery](https://bigquery.cloud.google.com/table/patents-public-data:ebi_chembl.frac_classification_24)

* `frac_class_id` STRING NULLABLE 

* `active_ingredient` STRING NULLABLE 

* `level1` STRING NULLABLE 

* `level1_description` STRING NULLABLE 

* `level2` STRING NULLABLE 

* `level2_description` STRING NULLABLE 

* `level3` STRING NULLABLE 

* `level3_description` STRING NULLABLE 

* `level4` STRING NULLABLE 

* `level4_description` STRING NULLABLE 

* `level5` STRING NULLABLE 

* `frac_code` STRING NULLABLE 
































*****
## patents-public-data:ebi_chembl.go_classification_23


Old table version `23`, schema skipped.





*****
## patents-public-data:ebi_chembl.go_classification_24



> ChEMBL Data is a manually curated database of small molecules used in drug discovery, including information about existing patented drugs.
> 
> Schema: http://ftp.ebi.ac.uk/pub/databases/chembl/ChEMBLdb/releases/chembl_23/chembl_23_schema.png
> 
> Documentation: http://ftp.ebi.ac.uk/pub/databases/chembl/ChEMBLdb/releases/chembl_23/schema_documentation.html
> 
> “ChEMBL” by the European Bioinformatics Institute (EMBL-EBI), used under CC BY-SA 3.0. Modifications have been made to add normalized publication numbers.





| Stat | Value |
|----------|----------|
| Last updated | 2018-10-31 |
| Rows | 309 |
| Size | 40.3 kB |

### Schema
[View in BigQuery](https://bigquery.cloud.google.com/table/patents-public-data:ebi_chembl.go_classification_24)

* `go_id` STRING NULLABLE 

* `parent_go_id` STRING NULLABLE 

* `pref_name` STRING NULLABLE 

* `class_level` STRING NULLABLE 

* `aspect` STRING NULLABLE 

* `path` STRING NULLABLE 




















*****
## patents-public-data:ebi_chembl.hrac_classification_23


Old table version `23`, schema skipped.





*****
## patents-public-data:ebi_chembl.hrac_classification_24



> ChEMBL Data is a manually curated database of small molecules used in drug discovery, including information about existing patented drugs.
> 
> Schema: http://ftp.ebi.ac.uk/pub/databases/chembl/ChEMBLdb/releases/chembl_23/chembl_23_schema.png
> 
> Documentation: http://ftp.ebi.ac.uk/pub/databases/chembl/ChEMBLdb/releases/chembl_23/schema_documentation.html
> 
> “ChEMBL” by the European Bioinformatics Institute (EMBL-EBI), used under CC BY-SA 3.0. Modifications have been made to add normalized publication numbers.





| Stat | Value |
|----------|----------|
| Last updated | 2018-10-31 |
| Rows | 273 |
| Size | 27.4 kB |

### Schema
[View in BigQuery](https://bigquery.cloud.google.com/table/patents-public-data:ebi_chembl.hrac_classification_24)

* `hrac_class_id` STRING NULLABLE 

* `active_ingredient` STRING NULLABLE 

* `level1` STRING NULLABLE 

* `level1_description` STRING NULLABLE 

* `level2` STRING NULLABLE 

* `level2_description` STRING NULLABLE 

* `level3` STRING NULLABLE 

* `hrac_code` STRING NULLABLE 
























*****
## patents-public-data:ebi_chembl.indication_refs_23


Old table version `23`, schema skipped.





*****
## patents-public-data:ebi_chembl.indication_refs_24



> ChEMBL Data is a manually curated database of small molecules used in drug discovery, including information about existing patented drugs.
> 
> Schema: http://ftp.ebi.ac.uk/pub/databases/chembl/ChEMBLdb/releases/chembl_23/chembl_23_schema.png
> 
> Documentation: http://ftp.ebi.ac.uk/pub/databases/chembl/ChEMBLdb/releases/chembl_23/schema_documentation.html
> 
> “ChEMBL” by the European Bioinformatics Institute (EMBL-EBI), used under CC BY-SA 3.0. Modifications have been made to add normalized publication numbers.





| Stat | Value |
|----------|----------|
| Last updated | 2018-10-31 |
| Rows | 35,268 |
| Size | 5.9 MB |

### Schema
[View in BigQuery](https://bigquery.cloud.google.com/table/patents-public-data:ebi_chembl.indication_refs_24)

* `indref_id` STRING NULLABLE 

* `drugind_id` STRING NULLABLE 

* `ref_type` STRING NULLABLE 

* `ref_id` STRING NULLABLE 

* `ref_url` STRING NULLABLE 


















*****
## patents-public-data:ebi_chembl.irac_classification_23


Old table version `23`, schema skipped.





*****
## patents-public-data:ebi_chembl.irac_classification_24



> ChEMBL Data is a manually curated database of small molecules used in drug discovery, including information about existing patented drugs.
> 
> Schema: http://ftp.ebi.ac.uk/pub/databases/chembl/ChEMBLdb/releases/chembl_23/chembl_23_schema.png
> 
> Documentation: http://ftp.ebi.ac.uk/pub/databases/chembl/ChEMBLdb/releases/chembl_23/schema_documentation.html
> 
> “ChEMBL” by the European Bioinformatics Institute (EMBL-EBI), used under CC BY-SA 3.0. Modifications have been made to add normalized publication numbers.





| Stat | Value |
|----------|----------|
| Last updated | 2018-10-31 |
| Rows | 251 |
| Size | 30.6 kB |

### Schema
[View in BigQuery](https://bigquery.cloud.google.com/table/patents-public-data:ebi_chembl.irac_classification_24)

* `irac_class_id` STRING NULLABLE 

* `active_ingredient` STRING NULLABLE 

* `level1` STRING NULLABLE 

* `level1_description` STRING NULLABLE 

* `level2` STRING NULLABLE 

* `level2_description` STRING NULLABLE 

* `level3` STRING NULLABLE 

* `level3_description` STRING NULLABLE 

* `level4` STRING NULLABLE 

* `irac_code` STRING NULLABLE 




























*****
## patents-public-data:ebi_chembl.ligand_eff_23


Old table version `23`, schema skipped.





*****
## patents-public-data:ebi_chembl.ligand_eff_24



> ChEMBL Data is a manually curated database of small molecules used in drug discovery, including information about existing patented drugs.
> 
> Schema: http://ftp.ebi.ac.uk/pub/databases/chembl/ChEMBLdb/releases/chembl_23/chembl_23_schema.png
> 
> Documentation: http://ftp.ebi.ac.uk/pub/databases/chembl/ChEMBLdb/releases/chembl_23/schema_documentation.html
> 
> “ChEMBL” by the European Bioinformatics Institute (EMBL-EBI), used under CC BY-SA 3.0. Modifications have been made to add normalized publication numbers.





| Stat | Value |
|----------|----------|
| Last updated | 2018-10-31 |
| Rows | 1,215,303 |
| Size | 40.9 MB |

### Schema
[View in BigQuery](https://bigquery.cloud.google.com/table/patents-public-data:ebi_chembl.ligand_eff_24)

* `activity_id` STRING NULLABLE 

* `bei` STRING NULLABLE 

* `sei` STRING NULLABLE 

* `le` STRING NULLABLE 

* `lle` STRING NULLABLE 


















*****
## patents-public-data:ebi_chembl.match_23


Old table version `23`, schema skipped.





*****
## patents-public-data:ebi_chembl.match_24



> ChEMBL Data is a manually curated database of small molecules used in drug discovery, including information about existing patented drugs.
> 
> Schema: http://ftp.ebi.ac.uk/pub/databases/chembl/ChEMBLdb/releases/chembl_23/chembl_23_schema.png
> 
> Documentation: http://ftp.ebi.ac.uk/pub/databases/chembl/ChEMBLdb/releases/chembl_23/schema_documentation.html
> 
> “ChEMBL” by the European Bioinformatics Institute (EMBL-EBI), used under CC BY-SA 3.0. Modifications have been made to add normalized publication numbers.





| Stat | Value |
|----------|----------|
| Last updated | 2018-10-31 |
| Rows | 4,456 |
| Size | 108.5 kB |

### Schema
[View in BigQuery](https://bigquery.cloud.google.com/table/patents-public-data:ebi_chembl.match_24)

* `patent_no` STRING NULLABLE  joins on **ChEMBL patent_no**

* `publication_number` STRING NULLABLE  joins on **publication_number**



### Join columns


#### patent_no

joins to `patents-public-data:ebi_chembl.product_patents_24::patent_no` on **ChEMBL patent_no** (100.00%, 4,456 rows)

| Key | Percent | Rows | Sample values |
|------|-----|--------|--------------------------------------------------------|
| `all` | 100.00% | 4,456 | `['9186357', '8137993', '7420057', '8039494', '6315173*PED']` |


    #standardSQL
    SELECT
      COUNT(*) AS cnt,
      COUNT(second.second_column) AS second_cnt,
      ARRAY_AGG(first.patent_no IGNORE NULLS ORDER BY RAND() LIMIT 5) AS sample_value
    FROM `patents-public-data.ebi_chembl.match_24`AS first
    LEFT JOIN (
      SELECT patent_no AS second_column, COUNT(*) AS cnt
      FROM `patents-public-data.ebi_chembl.product_patents_24`
      GROUP BY 1
    ) AS second ON first.patent_no = second.second_column



joins from `patents-public-data:ebi_chembl.product_patents_24::patent_no` on **ChEMBL patent_no** (100.00%, 14,113 rows)




#### publication_number

joins to `patents-public-data:patents.publications::publication_number` on **publication_number** (100.00%, 4,456 rows)

| Key | Percent | Rows | Sample values |
|------|-----|--------|--------------------------------------------------------|
| `all` | 100.00% | 4,456 | `['US-8608698-B2', 'US-8052994-B2', 'US-8604064-B2', 'US-9050302-B2', 'US-8858961-B2']` |


    #standardSQL
    SELECT
      COUNT(*) AS cnt,
      COUNT(second.second_column) AS second_cnt,
      ARRAY_AGG(first.publication_number IGNORE NULLS ORDER BY RAND() LIMIT 5) AS sample_value
    FROM `patents-public-data.ebi_chembl.match_24`AS first
    LEFT JOIN (
      SELECT publication_number AS second_column, COUNT(*) AS cnt
      FROM `patents-public-data.patents.publications`
      GROUP BY 1
    ) AS second ON first.publication_number = second.second_column



joins from `patents-public-data:patents.publications::publication_number` on **publication_number** (0.00%, 3,963 rows)






*****
## patents-public-data:ebi_chembl.mechanism_refs_23


Old table version `23`, schema skipped.





*****
## patents-public-data:ebi_chembl.mechanism_refs_24



> ChEMBL Data is a manually curated database of small molecules used in drug discovery, including information about existing patented drugs.
> 
> Schema: http://ftp.ebi.ac.uk/pub/databases/chembl/ChEMBLdb/releases/chembl_23/chembl_23_schema.png
> 
> Documentation: http://ftp.ebi.ac.uk/pub/databases/chembl/ChEMBLdb/releases/chembl_23/schema_documentation.html
> 
> “ChEMBL” by the European Bioinformatics Institute (EMBL-EBI), used under CC BY-SA 3.0. Modifications have been made to add normalized publication numbers.





| Stat | Value |
|----------|----------|
| Last updated | 2018-10-31 |
| Rows | 9,536 |
| Size | 907.4 kB |

### Schema
[View in BigQuery](https://bigquery.cloud.google.com/table/patents-public-data:ebi_chembl.mechanism_refs_24)

* `mecref_id` STRING NULLABLE 

* `mec_id` STRING NULLABLE 

* `ref_type` STRING NULLABLE 

* `ref_id` STRING NULLABLE 

* `ref_url` STRING NULLABLE 


















*****
## patents-public-data:ebi_chembl.metabolism_23


Old table version `23`, schema skipped.





*****
## patents-public-data:ebi_chembl.metabolism_24



> ChEMBL Data is a manually curated database of small molecules used in drug discovery, including information about existing patented drugs.
> 
> Schema: http://ftp.ebi.ac.uk/pub/databases/chembl/ChEMBLdb/releases/chembl_23/chembl_23_schema.png
> 
> Documentation: http://ftp.ebi.ac.uk/pub/databases/chembl/ChEMBLdb/releases/chembl_23/schema_documentation.html
> 
> “ChEMBL” by the European Bioinformatics Institute (EMBL-EBI), used under CC BY-SA 3.0. Modifications have been made to add normalized publication numbers.





| Stat | Value |
|----------|----------|
| Last updated | 2018-10-31 |
| Rows | 1,245 |
| Size | 246.7 kB |

### Schema
[View in BigQuery](https://bigquery.cloud.google.com/table/patents-public-data:ebi_chembl.metabolism_24)

* `met_id` STRING NULLABLE 

* `drug_record_id` STRING NULLABLE 

* `substrate_record_id` STRING NULLABLE 

* `metabolite_record_id` STRING NULLABLE 

* `pathway_id` STRING NULLABLE 

* `pathway_key` STRING NULLABLE 

* `enzyme_name` STRING NULLABLE 

* `enzyme_tid` STRING NULLABLE 

* `met_conversion` STRING NULLABLE 

* `organism` STRING NULLABLE 

* `tax_id` STRING NULLABLE 

* `met_comment` STRING NULLABLE 
































*****
## patents-public-data:ebi_chembl.metabolism_refs_23


Old table version `23`, schema skipped.





*****
## patents-public-data:ebi_chembl.metabolism_refs_24



> ChEMBL Data is a manually curated database of small molecules used in drug discovery, including information about existing patented drugs.
> 
> Schema: http://ftp.ebi.ac.uk/pub/databases/chembl/ChEMBLdb/releases/chembl_23/chembl_23_schema.png
> 
> Documentation: http://ftp.ebi.ac.uk/pub/databases/chembl/ChEMBLdb/releases/chembl_23/schema_documentation.html
> 
> “ChEMBL” by the European Bioinformatics Institute (EMBL-EBI), used under CC BY-SA 3.0. Modifications have been made to add normalized publication numbers.





| Stat | Value |
|----------|----------|
| Last updated | 2018-10-31 |
| Rows | 2,409 |
| Size | 215.5 kB |

### Schema
[View in BigQuery](https://bigquery.cloud.google.com/table/patents-public-data:ebi_chembl.metabolism_refs_24)

* `metref_id` STRING NULLABLE 

* `met_id` STRING NULLABLE 

* `ref_type` STRING NULLABLE 

* `ref_id` STRING NULLABLE 

* `ref_url` STRING NULLABLE 


















*****
## patents-public-data:ebi_chembl.molecule_atc_classification_23


Old table version `23`, schema skipped.





*****
## patents-public-data:ebi_chembl.molecule_atc_classification_24



> ChEMBL Data is a manually curated database of small molecules used in drug discovery, including information about existing patented drugs.
> 
> Schema: http://ftp.ebi.ac.uk/pub/databases/chembl/ChEMBLdb/releases/chembl_23/chembl_23_schema.png
> 
> Documentation: http://ftp.ebi.ac.uk/pub/databases/chembl/ChEMBLdb/releases/chembl_23/schema_documentation.html
> 
> “ChEMBL” by the European Bioinformatics Institute (EMBL-EBI), used under CC BY-SA 3.0. Modifications have been made to add normalized publication numbers.





| Stat | Value |
|----------|----------|
| Last updated | 2018-10-31 |
| Rows | 4,260 |
| Size | 102.0 kB |

### Schema
[View in BigQuery](https://bigquery.cloud.google.com/table/patents-public-data:ebi_chembl.molecule_atc_classification_24)

* `mol_atc_id` STRING NULLABLE 

* `level5` STRING NULLABLE 

* `molregno` STRING NULLABLE  joins on **ChEMBL molregno**



### Join columns






#### molregno

joins to `patents-public-data:ebi_chembl.compound_properties_24::molregno` on **ChEMBL molregno** (89.44%, 3,810 rows)

| Key | Percent | Rows | Sample values |
|------|-----|--------|--------------------------------------------------------|
| `all` | 89.44% | 3,810 | `['1381409', '675164', '139286', '1380107', '11143']` |


    #standardSQL
    SELECT
      COUNT(*) AS cnt,
      COUNT(second.second_column) AS second_cnt,
      ARRAY_AGG(first.molregno IGNORE NULLS ORDER BY RAND() LIMIT 5) AS sample_value
    FROM `patents-public-data.ebi_chembl.molecule_atc_classification_24`AS first
    LEFT JOIN (
      SELECT molregno AS second_column, COUNT(*) AS cnt
      FROM `patents-public-data.ebi_chembl.compound_properties_24`
      GROUP BY 1
    ) AS second ON first.molregno = second.second_column



joins from `patents-public-data:ebi_chembl.compound_properties_24::molregno` on **ChEMBL molregno** (0.16%, 2,833 rows)






*****
## patents-public-data:ebi_chembl.molecule_dictionary_23


Old table version `23`, schema skipped.





*****
## patents-public-data:ebi_chembl.molecule_dictionary_24



> ChEMBL Data is a manually curated database of small molecules used in drug discovery, including information about existing patented drugs.
> 
> Schema: http://ftp.ebi.ac.uk/pub/databases/chembl/ChEMBLdb/releases/chembl_23/chembl_23_schema.png
> 
> Documentation: http://ftp.ebi.ac.uk/pub/databases/chembl/ChEMBLdb/releases/chembl_23/schema_documentation.html
> 
> “ChEMBL” by the European Bioinformatics Institute (EMBL-EBI), used under CC BY-SA 3.0. Modifications have been made to add normalized publication numbers.





| Stat | Value |
|----------|----------|
| Last updated | 2018-10-31 |
| Rows | 1,828,820 |
| Size | 173.6 MB |

### Schema
[View in BigQuery](https://bigquery.cloud.google.com/table/patents-public-data:ebi_chembl.molecule_dictionary_24)

* `molregno` STRING NULLABLE  joins on **ChEMBL molregno**

* `pref_name` STRING NULLABLE 

* `chembl_id` STRING NULLABLE 

* `max_phase` STRING NULLABLE 

* `therapeutic_flag` STRING NULLABLE 

* `dosed_ingredient` STRING NULLABLE 

* `structure_type` STRING NULLABLE 

* `chebi_par_id` STRING NULLABLE 

* `molecule_type` STRING NULLABLE 

* `first_approval` STRING NULLABLE 

* `oral` STRING NULLABLE 

* `parenteral` STRING NULLABLE 

* `topical` STRING NULLABLE 

* `black_box_warning` STRING NULLABLE 

* `natural_product` STRING NULLABLE 

* `first_in_class` STRING NULLABLE 

* `chirality` STRING NULLABLE 

* `prodrug` STRING NULLABLE 

* `inorganic_flag` STRING NULLABLE 

* `usan_year` STRING NULLABLE 

* `availability_type` STRING NULLABLE 

* `usan_stem` STRING NULLABLE 

* `polymer_flag` STRING NULLABLE 

* `usan_substem` STRING NULLABLE 

* `usan_stem_definition` STRING NULLABLE 

* `indication_class` STRING NULLABLE 

* `withdrawn_flag` STRING NULLABLE 

* `withdrawn_year` STRING NULLABLE 

* `withdrawn_country` STRING NULLABLE 

* `withdrawn_reason` STRING NULLABLE 

* `withdrawn_class` STRING NULLABLE 



### Join columns


#### molregno

joins to `patents-public-data:ebi_chembl.compound_properties_24::molregno` on **ChEMBL molregno** (99.69%, 1,823,191 rows)

| Key | Percent | Rows | Sample values |
|------|-----|--------|--------------------------------------------------------|
| `all` | 99.69% | 1,823,191 | `['588882', '457772', '153391', '454374', '846922']` |


    #standardSQL
    SELECT
      COUNT(*) AS cnt,
      COUNT(second.second_column) AS second_cnt,
      ARRAY_AGG(first.molregno IGNORE NULLS ORDER BY RAND() LIMIT 5) AS sample_value
    FROM `patents-public-data.ebi_chembl.molecule_dictionary_24`AS first
    LEFT JOIN (
      SELECT molregno AS second_column, COUNT(*) AS cnt
      FROM `patents-public-data.ebi_chembl.compound_properties_24`
      GROUP BY 1
    ) AS second ON first.molregno = second.second_column



joins from `patents-public-data:ebi_chembl.compound_properties_24::molregno` on **ChEMBL molregno** (100.00%, 1,823,191 rows)


































































*****
## patents-public-data:ebi_chembl.molecule_frac_classification_23


Old table version `23`, schema skipped.





*****
## patents-public-data:ebi_chembl.molecule_frac_classification_24



> ChEMBL Data is a manually curated database of small molecules used in drug discovery, including information about existing patented drugs.
> 
> Schema: http://ftp.ebi.ac.uk/pub/databases/chembl/ChEMBLdb/releases/chembl_23/chembl_23_schema.png
> 
> Documentation: http://ftp.ebi.ac.uk/pub/databases/chembl/ChEMBLdb/releases/chembl_23/schema_documentation.html
> 
> “ChEMBL” by the European Bioinformatics Institute (EMBL-EBI), used under CC BY-SA 3.0. Modifications have been made to add normalized publication numbers.





| Stat | Value |
|----------|----------|
| Last updated | 2018-10-31 |
| Rows | 145 |
| Size | 2.6 kB |

### Schema
[View in BigQuery](https://bigquery.cloud.google.com/table/patents-public-data:ebi_chembl.molecule_frac_classification_24)

* `mol_frac_id` STRING NULLABLE 

* `frac_class_id` STRING NULLABLE 

* `molregno` STRING NULLABLE  joins on **ChEMBL molregno**



### Join columns






#### molregno

joins to `patents-public-data:ebi_chembl.compound_properties_24::molregno` on **ChEMBL molregno** (100.00%, 145 rows)

| Key | Percent | Rows | Sample values |
|------|-----|--------|--------------------------------------------------------|
| `all` | 100.00% | 145 | `['467422', '26722', '1493656', '1672848', '38856']` |


    #standardSQL
    SELECT
      COUNT(*) AS cnt,
      COUNT(second.second_column) AS second_cnt,
      ARRAY_AGG(first.molregno IGNORE NULLS ORDER BY RAND() LIMIT 5) AS sample_value
    FROM `patents-public-data.ebi_chembl.molecule_frac_classification_24`AS first
    LEFT JOIN (
      SELECT molregno AS second_column, COUNT(*) AS cnt
      FROM `patents-public-data.ebi_chembl.compound_properties_24`
      GROUP BY 1
    ) AS second ON first.molregno = second.second_column



joins from `patents-public-data:ebi_chembl.compound_properties_24::molregno` on **ChEMBL molregno** (0.01%, 145 rows)






*****
## patents-public-data:ebi_chembl.molecule_hierarchy_23


Old table version `23`, schema skipped.





*****
## patents-public-data:ebi_chembl.molecule_hierarchy_24



> ChEMBL Data is a manually curated database of small molecules used in drug discovery, including information about existing patented drugs.
> 
> Schema: http://ftp.ebi.ac.uk/pub/databases/chembl/ChEMBLdb/releases/chembl_23/chembl_23_schema.png
> 
> Documentation: http://ftp.ebi.ac.uk/pub/databases/chembl/ChEMBLdb/releases/chembl_23/schema_documentation.html
> 
> “ChEMBL” by the European Bioinformatics Institute (EMBL-EBI), used under CC BY-SA 3.0. Modifications have been made to add normalized publication numbers.





| Stat | Value |
|----------|----------|
| Last updated | 2018-10-31 |
| Rows | 1,749,733 |
| Size | 44.4 MB |

### Schema
[View in BigQuery](https://bigquery.cloud.google.com/table/patents-public-data:ebi_chembl.molecule_hierarchy_24)

* `molregno` STRING NULLABLE  joins on **ChEMBL molregno**

* `parent_molregno` STRING NULLABLE 

* `active_molregno` STRING NULLABLE 



### Join columns


#### molregno

joins to `patents-public-data:ebi_chembl.compound_properties_24::molregno` on **ChEMBL molregno** (99.68%, 1,744,111 rows)

| Key | Percent | Rows | Sample values |
|------|-----|--------|--------------------------------------------------------|
| `all` | 99.68% | 1,744,111 | `['1992998', '1609435', '523529', '1280708', '1228329']` |


    #standardSQL
    SELECT
      COUNT(*) AS cnt,
      COUNT(second.second_column) AS second_cnt,
      ARRAY_AGG(first.molregno IGNORE NULLS ORDER BY RAND() LIMIT 5) AS sample_value
    FROM `patents-public-data.ebi_chembl.molecule_hierarchy_24`AS first
    LEFT JOIN (
      SELECT molregno AS second_column, COUNT(*) AS cnt
      FROM `patents-public-data.ebi_chembl.compound_properties_24`
      GROUP BY 1
    ) AS second ON first.molregno = second.second_column



joins from `patents-public-data:ebi_chembl.compound_properties_24::molregno` on **ChEMBL molregno** (95.66%, 1,744,111 rows)










*****
## patents-public-data:ebi_chembl.molecule_hrac_classification_23


Old table version `23`, schema skipped.





*****
## patents-public-data:ebi_chembl.molecule_hrac_classification_24



> ChEMBL Data is a manually curated database of small molecules used in drug discovery, including information about existing patented drugs.
> 
> Schema: http://ftp.ebi.ac.uk/pub/databases/chembl/ChEMBLdb/releases/chembl_23/chembl_23_schema.png
> 
> Documentation: http://ftp.ebi.ac.uk/pub/databases/chembl/ChEMBLdb/releases/chembl_23/schema_documentation.html
> 
> “ChEMBL” by the European Bioinformatics Institute (EMBL-EBI), used under CC BY-SA 3.0. Modifications have been made to add normalized publication numbers.





| Stat | Value |
|----------|----------|
| Last updated | 2018-10-31 |
| Rows | 205 |
| Size | 3.6 kB |

### Schema
[View in BigQuery](https://bigquery.cloud.google.com/table/patents-public-data:ebi_chembl.molecule_hrac_classification_24)

* `mol_hrac_id` STRING NULLABLE 

* `hrac_class_id` STRING NULLABLE 

* `molregno` STRING NULLABLE  joins on **ChEMBL molregno**



### Join columns






#### molregno

joins to `patents-public-data:ebi_chembl.compound_properties_24::molregno` on **ChEMBL molregno** (100.00%, 205 rows)

| Key | Percent | Rows | Sample values |
|------|-----|--------|--------------------------------------------------------|
| `all` | 100.00% | 205 | `['1227289', '1475509', '454216', '1627951', '1016208']` |


    #standardSQL
    SELECT
      COUNT(*) AS cnt,
      COUNT(second.second_column) AS second_cnt,
      ARRAY_AGG(first.molregno IGNORE NULLS ORDER BY RAND() LIMIT 5) AS sample_value
    FROM `patents-public-data.ebi_chembl.molecule_hrac_classification_24`AS first
    LEFT JOIN (
      SELECT molregno AS second_column, COUNT(*) AS cnt
      FROM `patents-public-data.ebi_chembl.compound_properties_24`
      GROUP BY 1
    ) AS second ON first.molregno = second.second_column



joins from `patents-public-data:ebi_chembl.compound_properties_24::molregno` on **ChEMBL molregno** (0.01%, 203 rows)






*****
## patents-public-data:ebi_chembl.molecule_irac_classification_23


Old table version `23`, schema skipped.





*****
## patents-public-data:ebi_chembl.molecule_irac_classification_24



> ChEMBL Data is a manually curated database of small molecules used in drug discovery, including information about existing patented drugs.
> 
> Schema: http://ftp.ebi.ac.uk/pub/databases/chembl/ChEMBLdb/releases/chembl_23/chembl_23_schema.png
> 
> Documentation: http://ftp.ebi.ac.uk/pub/databases/chembl/ChEMBLdb/releases/chembl_23/schema_documentation.html
> 
> “ChEMBL” by the European Bioinformatics Institute (EMBL-EBI), used under CC BY-SA 3.0. Modifications have been made to add normalized publication numbers.





| Stat | Value |
|----------|----------|
| Last updated | 2018-10-31 |
| Rows | 185 |
| Size | 3.2 kB |

### Schema
[View in BigQuery](https://bigquery.cloud.google.com/table/patents-public-data:ebi_chembl.molecule_irac_classification_24)

* `mol_irac_id` STRING NULLABLE 

* `irac_class_id` STRING NULLABLE 

* `molregno` STRING NULLABLE  joins on **ChEMBL molregno**



### Join columns






#### molregno

joins to `patents-public-data:ebi_chembl.compound_properties_24::molregno` on **ChEMBL molregno** (100.00%, 185 rows)

| Key | Percent | Rows | Sample values |
|------|-----|--------|--------------------------------------------------------|
| `all` | 100.00% | 185 | `['1232083', '421902', '1464243', '1461978', '1476106']` |


    #standardSQL
    SELECT
      COUNT(*) AS cnt,
      COUNT(second.second_column) AS second_cnt,
      ARRAY_AGG(first.molregno IGNORE NULLS ORDER BY RAND() LIMIT 5) AS sample_value
    FROM `patents-public-data.ebi_chembl.molecule_irac_classification_24`AS first
    LEFT JOIN (
      SELECT molregno AS second_column, COUNT(*) AS cnt
      FROM `patents-public-data.ebi_chembl.compound_properties_24`
      GROUP BY 1
    ) AS second ON first.molregno = second.second_column



joins from `patents-public-data:ebi_chembl.compound_properties_24::molregno` on **ChEMBL molregno** (0.01%, 185 rows)






*****
## patents-public-data:ebi_chembl.molecule_synonyms_23


Old table version `23`, schema skipped.





*****
## patents-public-data:ebi_chembl.molecule_synonyms_24



> ChEMBL Data is a manually curated database of small molecules used in drug discovery, including information about existing patented drugs.
> 
> Schema: http://ftp.ebi.ac.uk/pub/databases/chembl/ChEMBLdb/releases/chembl_23/chembl_23_schema.png
> 
> Documentation: http://ftp.ebi.ac.uk/pub/databases/chembl/ChEMBLdb/releases/chembl_23/schema_documentation.html
> 
> “ChEMBL” by the European Bioinformatics Institute (EMBL-EBI), used under CC BY-SA 3.0. Modifications have been made to add normalized publication numbers.





| Stat | Value |
|----------|----------|
| Last updated | 2018-10-31 |
| Rows | 155,331 |
| Size | 6.6 MB |

### Schema
[View in BigQuery](https://bigquery.cloud.google.com/table/patents-public-data:ebi_chembl.molecule_synonyms_24)

* `molregno` STRING NULLABLE  joins on **ChEMBL molregno**

* `syn_type` STRING NULLABLE 

* `molsyn_id` STRING NULLABLE 

* `res_stem_id` STRING NULLABLE 

* `synonyms` STRING NULLABLE 



### Join columns


#### molregno

joins to `patents-public-data:ebi_chembl.compound_properties_24::molregno` on **ChEMBL molregno** (94.48%, 146,753 rows)

| Key | Percent | Rows | Sample values |
|------|-----|--------|--------------------------------------------------------|
| `all` | 94.48% | 146,753 | `['530090', '54404', '1381334', '1064828', '538050']` |


    #standardSQL
    SELECT
      COUNT(*) AS cnt,
      COUNT(second.second_column) AS second_cnt,
      ARRAY_AGG(first.molregno IGNORE NULLS ORDER BY RAND() LIMIT 5) AS sample_value
    FROM `patents-public-data.ebi_chembl.molecule_synonyms_24`AS first
    LEFT JOIN (
      SELECT molregno AS second_column, COUNT(*) AS cnt
      FROM `patents-public-data.ebi_chembl.compound_properties_24`
      GROUP BY 1
    ) AS second ON first.molregno = second.second_column



joins from `patents-public-data:ebi_chembl.compound_properties_24::molregno` on **ChEMBL molregno** (4.54%, 82,838 rows)














*****
## patents-public-data:ebi_chembl.organism_class_23


Old table version `23`, schema skipped.





*****
## patents-public-data:ebi_chembl.organism_class_24



> ChEMBL Data is a manually curated database of small molecules used in drug discovery, including information about existing patented drugs.
> 
> Schema: http://ftp.ebi.ac.uk/pub/databases/chembl/ChEMBLdb/releases/chembl_23/chembl_23_schema.png
> 
> Documentation: http://ftp.ebi.ac.uk/pub/databases/chembl/ChEMBLdb/releases/chembl_23/schema_documentation.html
> 
> “ChEMBL” by the European Bioinformatics Institute (EMBL-EBI), used under CC BY-SA 3.0. Modifications have been made to add normalized publication numbers.





| Stat | Value |
|----------|----------|
| Last updated | 2018-10-31 |
| Rows | 3,783 |
| Size | 170.3 kB |

### Schema
[View in BigQuery](https://bigquery.cloud.google.com/table/patents-public-data:ebi_chembl.organism_class_24)

* `oc_id` STRING NULLABLE 

* `tax_id` STRING NULLABLE 

* `l1` STRING NULLABLE 

* `l2` STRING NULLABLE 

* `l3` STRING NULLABLE 


















*****
## patents-public-data:ebi_chembl.parameter_type_23



> ChEMBL Data is a manually curated database of small molecules used in drug discovery, including information about existing patented drugs.
> 
> Schema: http://ftp.ebi.ac.uk/pub/databases/chembl/ChEMBLdb/releases/chembl_23/chembl_23_schema.png
> 
> Documentation: http://ftp.ebi.ac.uk/pub/databases/chembl/ChEMBLdb/releases/chembl_23/schema_documentation.html
> 
> “ChEMBL” by the European Bioinformatics Institute (EMBL-EBI), used under CC BY-SA 3.0. Modifications have been made to add normalized publication numbers.





| Stat | Value |
|----------|----------|
| Last updated | 2017-10-20 |
| Rows | 67 |
| Size | 5.9 kB |

### Schema
[View in BigQuery](https://bigquery.cloud.google.com/table/patents-public-data:ebi_chembl.parameter_type_23)

* `parameter_type` STRING  

* `description` STRING  












*****
## patents-public-data:ebi_chembl.patent_use_codes_23


Old table version `23`, schema skipped.





*****
## patents-public-data:ebi_chembl.patent_use_codes_24



> ChEMBL Data is a manually curated database of small molecules used in drug discovery, including information about existing patented drugs.
> 
> Schema: http://ftp.ebi.ac.uk/pub/databases/chembl/ChEMBLdb/releases/chembl_23/chembl_23_schema.png
> 
> Documentation: http://ftp.ebi.ac.uk/pub/databases/chembl/ChEMBLdb/releases/chembl_23/schema_documentation.html
> 
> “ChEMBL” by the European Bioinformatics Institute (EMBL-EBI), used under CC BY-SA 3.0. Modifications have been made to add normalized publication numbers.





| Stat | Value |
|----------|----------|
| Last updated | 2018-10-31 |
| Rows | 2,205 |
| Size | 240.7 kB |

### Schema
[View in BigQuery](https://bigquery.cloud.google.com/table/patents-public-data:ebi_chembl.patent_use_codes_24)

* `patent_use_code` STRING NULLABLE 

* `definition` STRING NULLABLE 












*****
## patents-public-data:ebi_chembl.predicted_binding_domains_23


Old table version `23`, schema skipped.





*****
## patents-public-data:ebi_chembl.predicted_binding_domains_24



> ChEMBL Data is a manually curated database of small molecules used in drug discovery, including information about existing patented drugs.
> 
> Schema: http://ftp.ebi.ac.uk/pub/databases/chembl/ChEMBLdb/releases/chembl_23/chembl_23_schema.png
> 
> Documentation: http://ftp.ebi.ac.uk/pub/databases/chembl/ChEMBLdb/releases/chembl_23/schema_documentation.html
> 
> “ChEMBL” by the European Bioinformatics Institute (EMBL-EBI), used under CC BY-SA 3.0. Modifications have been made to add normalized publication numbers.





| Stat | Value |
|----------|----------|
| Last updated | 2018-10-31 |
| Rows | 707,507 |
| Size | 31.8 MB |

### Schema
[View in BigQuery](https://bigquery.cloud.google.com/table/patents-public-data:ebi_chembl.predicted_binding_domains_24)

* `predbind_id` STRING NULLABLE 

* `activity_id` STRING NULLABLE 

* `site_id` STRING NULLABLE 

* `prediction_method` STRING NULLABLE 

* `confidence` STRING NULLABLE 


















*****
## patents-public-data:ebi_chembl.product_patents_23


Old table version `23`, schema skipped.





*****
## patents-public-data:ebi_chembl.product_patents_24



> ChEMBL Data is a manually curated database of small molecules used in drug discovery, including information about existing patented drugs.
> 
> Schema: http://ftp.ebi.ac.uk/pub/databases/chembl/ChEMBLdb/releases/chembl_23/chembl_23_schema.png
> 
> Documentation: http://ftp.ebi.ac.uk/pub/databases/chembl/ChEMBLdb/releases/chembl_23/schema_documentation.html
> 
> “ChEMBL” by the European Bioinformatics Institute (EMBL-EBI), used under CC BY-SA 3.0. Modifications have been made to add normalized publication numbers.





| Stat | Value |
|----------|----------|
| Last updated | 2018-10-31 |
| Rows | 14,113 |
| Size | 1.3 MB |

### Schema
[View in BigQuery](https://bigquery.cloud.google.com/table/patents-public-data:ebi_chembl.product_patents_24)

* `prod_pat_id` STRING NULLABLE 

* `product_id` STRING NULLABLE 

* `patent_no` STRING NULLABLE  joins on **ChEMBL patent_no**

* `patent_expire_date` STRING NULLABLE 

* `drug_substance_flag` STRING NULLABLE 

* `drug_product_flag` STRING NULLABLE 

* `patent_use_code` STRING NULLABLE 

* `delist_flag` STRING NULLABLE 

* `submission_date` STRING NULLABLE 



### Join columns






#### patent_no

joins to `patents-public-data:ebi_chembl.match_24::patent_no` on **ChEMBL patent_no** (100.00%, 14,113 rows)

| Key | Percent | Rows | Sample values |
|------|-----|--------|--------------------------------------------------------|
| `all` | 100.00% | 14,113 | `['8288539', '8691878*PED', '6596756*PED', '6066339', '6376515']` |


    #standardSQL
    SELECT
      COUNT(*) AS cnt,
      COUNT(second.second_column) AS second_cnt,
      ARRAY_AGG(first.patent_no IGNORE NULLS ORDER BY RAND() LIMIT 5) AS sample_value
    FROM `patents-public-data.ebi_chembl.product_patents_24`AS first
    LEFT JOIN (
      SELECT patent_no AS second_column, COUNT(*) AS cnt
      FROM `patents-public-data.ebi_chembl.match_24`
      GROUP BY 1
    ) AS second ON first.patent_no = second.second_column



joins from `patents-public-data:ebi_chembl.match_24::patent_no` on **ChEMBL patent_no** (100.00%, 4,456 rows)


















*****
## patents-public-data:ebi_chembl.products_23


Old table version `23`, schema skipped.





*****
## patents-public-data:ebi_chembl.products_24



> ChEMBL Data is a manually curated database of small molecules used in drug discovery, including information about existing patented drugs.
> 
> Schema: http://ftp.ebi.ac.uk/pub/databases/chembl/ChEMBLdb/releases/chembl_23/chembl_23_schema.png
> 
> Documentation: http://ftp.ebi.ac.uk/pub/databases/chembl/ChEMBLdb/releases/chembl_23/schema_documentation.html
> 
> “ChEMBL” by the European Bioinformatics Institute (EMBL-EBI), used under CC BY-SA 3.0. Modifications have been made to add normalized publication numbers.





| Stat | Value |
|----------|----------|
| Last updated | 2018-10-31 |
| Rows | 34,986 |
| Size | 4.7 MB |

### Schema
[View in BigQuery](https://bigquery.cloud.google.com/table/patents-public-data:ebi_chembl.products_24)

* `dosage_form` STRING NULLABLE 

* `route` STRING NULLABLE 

* `trade_name` STRING NULLABLE 

* `approval_date` STRING NULLABLE 

* `ad_type` STRING NULLABLE 

* `oral` STRING NULLABLE 

* `topical` STRING NULLABLE 

* `parenteral` STRING NULLABLE 

* `black_box_warning` STRING NULLABLE 

* `applicant_full_name` STRING NULLABLE 

* `innovator_company` STRING NULLABLE 

* `product_id` STRING NULLABLE 

* `nda_type` STRING NULLABLE 


































*****
## patents-public-data:ebi_chembl.protein_class_synonyms_23


Old table version `23`, schema skipped.





*****
## patents-public-data:ebi_chembl.protein_class_synonyms_24



> ChEMBL Data is a manually curated database of small molecules used in drug discovery, including information about existing patented drugs.
> 
> Schema: http://ftp.ebi.ac.uk/pub/databases/chembl/ChEMBLdb/releases/chembl_23/chembl_23_schema.png
> 
> Documentation: http://ftp.ebi.ac.uk/pub/databases/chembl/ChEMBLdb/releases/chembl_23/schema_documentation.html
> 
> “ChEMBL” by the European Bioinformatics Institute (EMBL-EBI), used under CC BY-SA 3.0. Modifications have been made to add normalized publication numbers.





| Stat | Value |
|----------|----------|
| Last updated | 2018-10-31 |
| Rows | 7,539 |
| Size | 383.1 kB |

### Schema
[View in BigQuery](https://bigquery.cloud.google.com/table/patents-public-data:ebi_chembl.protein_class_synonyms_24)

* `protclasssyn_id` STRING NULLABLE 

* `protein_class_id` STRING NULLABLE 

* `protein_class_synonym` STRING NULLABLE 

* `syn_type` STRING NULLABLE 
















*****
## patents-public-data:ebi_chembl.protein_classification_23


Old table version `23`, schema skipped.





*****
## patents-public-data:ebi_chembl.protein_classification_24



> ChEMBL Data is a manually curated database of small molecules used in drug discovery, including information about existing patented drugs.
> 
> Schema: http://ftp.ebi.ac.uk/pub/databases/chembl/ChEMBLdb/releases/chembl_23/chembl_23_schema.png
> 
> Documentation: http://ftp.ebi.ac.uk/pub/databases/chembl/ChEMBLdb/releases/chembl_23/schema_documentation.html
> 
> “ChEMBL” by the European Bioinformatics Institute (EMBL-EBI), used under CC BY-SA 3.0. Modifications have been made to add normalized publication numbers.





| Stat | Value |
|----------|----------|
| Last updated | 2018-10-31 |
| Rows | 858 |
| Size | 155.9 kB |

### Schema
[View in BigQuery](https://bigquery.cloud.google.com/table/patents-public-data:ebi_chembl.protein_classification_24)

* `protein_class_id` STRING NULLABLE 

* `parent_id` STRING NULLABLE 

* `pref_name` STRING NULLABLE 

* `short_name` STRING NULLABLE 

* `protein_class_desc` STRING NULLABLE 

* `definition` STRING NULLABLE 

* `class_level` STRING NULLABLE 






















*****
## patents-public-data:ebi_chembl.protein_family_classification_23


Old table version `23`, schema skipped.





*****
## patents-public-data:ebi_chembl.protein_family_classification_24



> ChEMBL Data is a manually curated database of small molecules used in drug discovery, including information about existing patented drugs.
> 
> Schema: http://ftp.ebi.ac.uk/pub/databases/chembl/ChEMBLdb/releases/chembl_23/chembl_23_schema.png
> 
> Documentation: http://ftp.ebi.ac.uk/pub/databases/chembl/ChEMBLdb/releases/chembl_23/schema_documentation.html
> 
> “ChEMBL” by the European Bioinformatics Institute (EMBL-EBI), used under CC BY-SA 3.0. Modifications have been made to add normalized publication numbers.





| Stat | Value |
|----------|----------|
| Last updated | 2018-10-31 |
| Rows | 857 |
| Size | 128.4 kB |

### Schema
[View in BigQuery](https://bigquery.cloud.google.com/table/patents-public-data:ebi_chembl.protein_family_classification_24)

* `protein_class_id` STRING NULLABLE 

* `protein_class_desc` STRING NULLABLE 

* `l1` STRING NULLABLE 

* `l2` STRING NULLABLE 

* `l3` STRING NULLABLE 

* `l4` STRING NULLABLE 

* `l5` STRING NULLABLE 

* `l6` STRING NULLABLE 

* `l7` STRING NULLABLE 

* `l8` STRING NULLABLE 




























*****
## patents-public-data:ebi_chembl.relationship_type_23


Old table version `23`, schema skipped.





*****
## patents-public-data:ebi_chembl.relationship_type_24



> ChEMBL Data is a manually curated database of small molecules used in drug discovery, including information about existing patented drugs.
> 
> Schema: http://ftp.ebi.ac.uk/pub/databases/chembl/ChEMBLdb/releases/chembl_23/chembl_23_schema.png
> 
> Documentation: http://ftp.ebi.ac.uk/pub/databases/chembl/ChEMBLdb/releases/chembl_23/schema_documentation.html
> 
> “ChEMBL” by the European Bioinformatics Institute (EMBL-EBI), used under CC BY-SA 3.0. Modifications have been made to add normalized publication numbers.





| Stat | Value |
|----------|----------|
| Last updated | 2018-10-31 |
| Rows | 6 |
| Size | 238 Bytes |

### Schema
[View in BigQuery](https://bigquery.cloud.google.com/table/patents-public-data:ebi_chembl.relationship_type_24)

* `relationship_type` STRING NULLABLE 

* `relationship_desc` STRING NULLABLE 












*****
## patents-public-data:ebi_chembl.research_companies_23


Old table version `23`, schema skipped.





*****
## patents-public-data:ebi_chembl.research_companies_24



> ChEMBL Data is a manually curated database of small molecules used in drug discovery, including information about existing patented drugs.
> 
> Schema: http://ftp.ebi.ac.uk/pub/databases/chembl/ChEMBLdb/releases/chembl_23/chembl_23_schema.png
> 
> Documentation: http://ftp.ebi.ac.uk/pub/databases/chembl/ChEMBLdb/releases/chembl_23/schema_documentation.html
> 
> “ChEMBL” by the European Bioinformatics Institute (EMBL-EBI), used under CC BY-SA 3.0. Modifications have been made to add normalized publication numbers.





| Stat | Value |
|----------|----------|
| Last updated | 2018-10-31 |
| Rows | 812 |
| Size | 25.6 kB |

### Schema
[View in BigQuery](https://bigquery.cloud.google.com/table/patents-public-data:ebi_chembl.research_companies_24)

* `co_stem_id` STRING NULLABLE 

* `res_stem_id` STRING NULLABLE 

* `company` STRING NULLABLE 

* `country` STRING NULLABLE 

* `previous_company` STRING NULLABLE 


















*****
## patents-public-data:ebi_chembl.research_stem_23


Old table version `23`, schema skipped.





*****
## patents-public-data:ebi_chembl.research_stem_24



> ChEMBL Data is a manually curated database of small molecules used in drug discovery, including information about existing patented drugs.
> 
> Schema: http://ftp.ebi.ac.uk/pub/databases/chembl/ChEMBLdb/releases/chembl_23/chembl_23_schema.png
> 
> Documentation: http://ftp.ebi.ac.uk/pub/databases/chembl/ChEMBLdb/releases/chembl_23/schema_documentation.html
> 
> “ChEMBL” by the European Bioinformatics Institute (EMBL-EBI), used under CC BY-SA 3.0. Modifications have been made to add normalized publication numbers.





| Stat | Value |
|----------|----------|
| Last updated | 2018-10-31 |
| Rows | 670 |
| Size | 6.4 kB |

### Schema
[View in BigQuery](https://bigquery.cloud.google.com/table/patents-public-data:ebi_chembl.research_stem_24)

* `res_stem_id` STRING NULLABLE 

* `research_stem` STRING NULLABLE 












*****
## patents-public-data:ebi_chembl.site_components_23


Old table version `23`, schema skipped.





*****
## patents-public-data:ebi_chembl.site_components_24



> ChEMBL Data is a manually curated database of small molecules used in drug discovery, including information about existing patented drugs.
> 
> Schema: http://ftp.ebi.ac.uk/pub/databases/chembl/ChEMBLdb/releases/chembl_23/chembl_23_schema.png
> 
> Documentation: http://ftp.ebi.ac.uk/pub/databases/chembl/ChEMBLdb/releases/chembl_23/schema_documentation.html
> 
> “ChEMBL” by the European Bioinformatics Institute (EMBL-EBI), used under CC BY-SA 3.0. Modifications have been made to add normalized publication numbers.





| Stat | Value |
|----------|----------|
| Last updated | 2018-10-31 |
| Rows | 13,620 |
| Size | 320.5 kB |

### Schema
[View in BigQuery](https://bigquery.cloud.google.com/table/patents-public-data:ebi_chembl.site_components_24)

* `sitecomp_id` STRING NULLABLE 

* `site_id` STRING NULLABLE 

* `component_id` STRING NULLABLE 

* `domain_id` STRING NULLABLE 

* `site_residues` STRING NULLABLE 


















*****
## patents-public-data:ebi_chembl.source_23


Old table version `23`, schema skipped.





*****
## patents-public-data:ebi_chembl.source_24



> ChEMBL Data is a manually curated database of small molecules used in drug discovery, including information about existing patented drugs.
> 
> Schema: http://ftp.ebi.ac.uk/pub/databases/chembl/ChEMBLdb/releases/chembl_23/chembl_23_schema.png
> 
> Documentation: http://ftp.ebi.ac.uk/pub/databases/chembl/ChEMBLdb/releases/chembl_23/schema_documentation.html
> 
> “ChEMBL” by the European Bioinformatics Institute (EMBL-EBI), used under CC BY-SA 3.0. Modifications have been made to add normalized publication numbers.





| Stat | Value |
|----------|----------|
| Last updated | 2018-10-31 |
| Rows | 44 |
| Size | 1.9 kB |

### Schema
[View in BigQuery](https://bigquery.cloud.google.com/table/patents-public-data:ebi_chembl.source_24)

* `src_id` STRING NULLABLE 

* `src_description` STRING NULLABLE 

* `src_short_name` STRING NULLABLE 














*****
## patents-public-data:ebi_chembl.sqlite_stat1_23


Old table version `23`, schema skipped.





*****
## patents-public-data:ebi_chembl.sqlite_stat1_24



> ChEMBL Data is a manually curated database of small molecules used in drug discovery, including information about existing patented drugs.
> 
> Schema: http://ftp.ebi.ac.uk/pub/databases/chembl/ChEMBLdb/releases/chembl_23/chembl_23_schema.png
> 
> Documentation: http://ftp.ebi.ac.uk/pub/databases/chembl/ChEMBLdb/releases/chembl_23/schema_documentation.html
> 
> “ChEMBL” by the European Bioinformatics Institute (EMBL-EBI), used under CC BY-SA 3.0. Modifications have been made to add normalized publication numbers.





| Stat | Value |
|----------|----------|
| Last updated | 2018-10-31 |
| Rows | 208 |
| Size | 12.1 kB |

### Schema
[View in BigQuery](https://bigquery.cloud.google.com/table/patents-public-data:ebi_chembl.sqlite_stat1_24)

* `tbl` STRING NULLABLE 

* `idx` STRING NULLABLE 

* `stat` STRING NULLABLE 














*****
## patents-public-data:ebi_chembl.structural_alert_sets_23


Old table version `23`, schema skipped.





*****
## patents-public-data:ebi_chembl.structural_alert_sets_24



> ChEMBL Data is a manually curated database of small molecules used in drug discovery, including information about existing patented drugs.
> 
> Schema: http://ftp.ebi.ac.uk/pub/databases/chembl/ChEMBLdb/releases/chembl_23/chembl_23_schema.png
> 
> Documentation: http://ftp.ebi.ac.uk/pub/databases/chembl/ChEMBLdb/releases/chembl_23/schema_documentation.html
> 
> “ChEMBL” by the European Bioinformatics Institute (EMBL-EBI), used under CC BY-SA 3.0. Modifications have been made to add normalized publication numbers.





| Stat | Value |
|----------|----------|
| Last updated | 2018-10-31 |
| Rows | 8 |
| Size | 114 Bytes |

### Schema
[View in BigQuery](https://bigquery.cloud.google.com/table/patents-public-data:ebi_chembl.structural_alert_sets_24)

* `alert_set_id` STRING NULLABLE 

* `set_name` STRING NULLABLE 

* `priority` STRING NULLABLE 














*****
## patents-public-data:ebi_chembl.structural_alerts_23


Old table version `23`, schema skipped.





*****
## patents-public-data:ebi_chembl.structural_alerts_24



> ChEMBL Data is a manually curated database of small molecules used in drug discovery, including information about existing patented drugs.
> 
> Schema: http://ftp.ebi.ac.uk/pub/databases/chembl/ChEMBLdb/releases/chembl_23/chembl_23_schema.png
> 
> Documentation: http://ftp.ebi.ac.uk/pub/databases/chembl/ChEMBLdb/releases/chembl_23/schema_documentation.html
> 
> “ChEMBL” by the European Bioinformatics Institute (EMBL-EBI), used under CC BY-SA 3.0. Modifications have been made to add normalized publication numbers.





| Stat | Value |
|----------|----------|
| Last updated | 2018-10-31 |
| Rows | 1,251 |
| Size | 107.2 kB |

### Schema
[View in BigQuery](https://bigquery.cloud.google.com/table/patents-public-data:ebi_chembl.structural_alerts_24)

* `alert_id` STRING NULLABLE 

* `alert_set_id` STRING NULLABLE 

* `alert_name` STRING NULLABLE 

* `smarts` STRING NULLABLE 
















*****
## patents-public-data:ebi_chembl.target_components_23


Old table version `23`, schema skipped.





*****
## patents-public-data:ebi_chembl.target_components_24



> ChEMBL Data is a manually curated database of small molecules used in drug discovery, including information about existing patented drugs.
> 
> Schema: http://ftp.ebi.ac.uk/pub/databases/chembl/ChEMBLdb/releases/chembl_23/chembl_23_schema.png
> 
> Documentation: http://ftp.ebi.ac.uk/pub/databases/chembl/ChEMBLdb/releases/chembl_23/schema_documentation.html
> 
> “ChEMBL” by the European Bioinformatics Institute (EMBL-EBI), used under CC BY-SA 3.0. Modifications have been made to add normalized publication numbers.





| Stat | Value |
|----------|----------|
| Last updated | 2018-10-31 |
| Rows | 10,468 |
| Size | 237.6 kB |

### Schema
[View in BigQuery](https://bigquery.cloud.google.com/table/patents-public-data:ebi_chembl.target_components_24)

* `tid` STRING NULLABLE 

* `component_id` STRING NULLABLE 

* `targcomp_id` STRING NULLABLE 

* `homologue` STRING NULLABLE 
















*****
## patents-public-data:ebi_chembl.target_dictionary_23


Old table version `23`, schema skipped.





*****
## patents-public-data:ebi_chembl.target_dictionary_24



> ChEMBL Data is a manually curated database of small molecules used in drug discovery, including information about existing patented drugs.
> 
> Schema: http://ftp.ebi.ac.uk/pub/databases/chembl/ChEMBLdb/releases/chembl_23/chembl_23_schema.png
> 
> Documentation: http://ftp.ebi.ac.uk/pub/databases/chembl/ChEMBLdb/releases/chembl_23/schema_documentation.html
> 
> “ChEMBL” by the European Bioinformatics Institute (EMBL-EBI), used under CC BY-SA 3.0. Modifications have been made to add normalized publication numbers.





| Stat | Value |
|----------|----------|
| Last updated | 2018-10-31 |
| Rows | 12,091 |
| Size | 1.1 MB |

### Schema
[View in BigQuery](https://bigquery.cloud.google.com/table/patents-public-data:ebi_chembl.target_dictionary_24)

* `tid` STRING NULLABLE 

* `target_type` STRING NULLABLE 

* `pref_name` STRING NULLABLE 

* `tax_id` STRING NULLABLE 

* `organism` STRING NULLABLE 

* `chembl_id` STRING NULLABLE 

* `species_group_flag` STRING NULLABLE 






















*****
## patents-public-data:ebi_chembl.target_relations_23


Old table version `23`, schema skipped.





*****
## patents-public-data:ebi_chembl.target_relations_24



> ChEMBL Data is a manually curated database of small molecules used in drug discovery, including information about existing patented drugs.
> 
> Schema: http://ftp.ebi.ac.uk/pub/databases/chembl/ChEMBLdb/releases/chembl_23/chembl_23_schema.png
> 
> Documentation: http://ftp.ebi.ac.uk/pub/databases/chembl/ChEMBLdb/releases/chembl_23/schema_documentation.html
> 
> “ChEMBL” by the European Bioinformatics Institute (EMBL-EBI), used under CC BY-SA 3.0. Modifications have been made to add normalized publication numbers.





| Stat | Value |
|----------|----------|
| Last updated | 2018-10-31 |
| Rows | 6,922 |
| Size | 244.7 kB |

### Schema
[View in BigQuery](https://bigquery.cloud.google.com/table/patents-public-data:ebi_chembl.target_relations_24)

* `tid` STRING NULLABLE 

* `relationship` STRING NULLABLE 

* `related_tid` STRING NULLABLE 

* `targrel_id` STRING NULLABLE 
















*****
## patents-public-data:ebi_chembl.target_type_23


Old table version `23`, schema skipped.





*****
## patents-public-data:ebi_chembl.target_type_24



> ChEMBL Data is a manually curated database of small molecules used in drug discovery, including information about existing patented drugs.
> 
> Schema: http://ftp.ebi.ac.uk/pub/databases/chembl/ChEMBLdb/releases/chembl_23/chembl_23_schema.png
> 
> Documentation: http://ftp.ebi.ac.uk/pub/databases/chembl/ChEMBLdb/releases/chembl_23/schema_documentation.html
> 
> “ChEMBL” by the European Bioinformatics Institute (EMBL-EBI), used under CC BY-SA 3.0. Modifications have been made to add normalized publication numbers.





| Stat | Value |
|----------|----------|
| Last updated | 2018-10-31 |
| Rows | 27 |
| Size | 2.3 kB |

### Schema
[View in BigQuery](https://bigquery.cloud.google.com/table/patents-public-data:ebi_chembl.target_type_24)

* `target_type` STRING NULLABLE 

* `target_desc` STRING NULLABLE 

* `parent_type` STRING NULLABLE 














*****
## patents-public-data:ebi_chembl.tissue_dictionary_23


Old table version `23`, schema skipped.





*****
## patents-public-data:ebi_chembl.tissue_dictionary_24



> ChEMBL Data is a manually curated database of small molecules used in drug discovery, including information about existing patented drugs.
> 
> Schema: http://ftp.ebi.ac.uk/pub/databases/chembl/ChEMBLdb/releases/chembl_23/chembl_23_schema.png
> 
> Documentation: http://ftp.ebi.ac.uk/pub/databases/chembl/ChEMBLdb/releases/chembl_23/schema_documentation.html
> 
> “ChEMBL” by the European Bioinformatics Institute (EMBL-EBI), used under CC BY-SA 3.0. Modifications have been made to add normalized publication numbers.





| Stat | Value |
|----------|----------|
| Last updated | 2018-10-31 |
| Rows | 655 |
| Size | 35.8 kB |

### Schema
[View in BigQuery](https://bigquery.cloud.google.com/table/patents-public-data:ebi_chembl.tissue_dictionary_24)

* `tissue_id` STRING NULLABLE 

* `uberon_id` STRING NULLABLE 

* `pref_name` STRING NULLABLE 

* `efo_id` STRING NULLABLE 

* `chembl_id` STRING NULLABLE 

* `bto_id` STRING NULLABLE 

* `caloha_id` STRING NULLABLE 






















*****
## patents-public-data:ebi_chembl.usan_stems_23


Old table version `23`, schema skipped.





*****
## patents-public-data:ebi_chembl.usan_stems_24



> ChEMBL Data is a manually curated database of small molecules used in drug discovery, including information about existing patented drugs.
> 
> Schema: http://ftp.ebi.ac.uk/pub/databases/chembl/ChEMBLdb/releases/chembl_23/chembl_23_schema.png
> 
> Documentation: http://ftp.ebi.ac.uk/pub/databases/chembl/ChEMBLdb/releases/chembl_23/schema_documentation.html
> 
> “ChEMBL” by the European Bioinformatics Institute (EMBL-EBI), used under CC BY-SA 3.0. Modifications have been made to add normalized publication numbers.





| Stat | Value |
|----------|----------|
| Last updated | 2018-10-31 |
| Rows | 700 |
| Size | 53.9 kB |

### Schema
[View in BigQuery](https://bigquery.cloud.google.com/table/patents-public-data:ebi_chembl.usan_stems_24)

* `usan_stem_id` STRING NULLABLE 

* `stem` STRING NULLABLE 

* `subgroup` STRING NULLABLE 

* `annotation` STRING NULLABLE 

* `stem_class` STRING NULLABLE 

* `major_class` STRING NULLABLE 

* `who_extra` STRING NULLABLE 






















*****
## patents-public-data:ebi_chembl.variant_sequences_23


Old table version `23`, schema skipped.





*****
## patents-public-data:ebi_chembl.variant_sequences_24



> ChEMBL Data is a manually curated database of small molecules used in drug discovery, including information about existing patented drugs.
> 
> Schema: http://ftp.ebi.ac.uk/pub/databases/chembl/ChEMBLdb/releases/chembl_23/chembl_23_schema.png
> 
> Documentation: http://ftp.ebi.ac.uk/pub/databases/chembl/ChEMBLdb/releases/chembl_23/schema_documentation.html
> 
> “ChEMBL” by the European Bioinformatics Institute (EMBL-EBI), used under CC BY-SA 3.0. Modifications have been made to add normalized publication numbers.





| Stat | Value |
|----------|----------|
| Last updated | 2018-10-31 |
| Rows | 1,200 |
| Size | 843.5 kB |

### Schema
[View in BigQuery](https://bigquery.cloud.google.com/table/patents-public-data:ebi_chembl.variant_sequences_24)

* `variant_id` STRING NULLABLE 

* `mutation` STRING NULLABLE 

* `accession` STRING NULLABLE 

* `version` STRING NULLABLE 

* `isoform` STRING NULLABLE 

* `sequence` STRING NULLABLE 

* `organism` STRING NULLABLE 






















*****
## patents-public-data:ebi_chembl.version_23


Old table version `23`, schema skipped.





*****
## patents-public-data:ebi_chembl.version_24



> ChEMBL Data is a manually curated database of small molecules used in drug discovery, including information about existing patented drugs.
> 
> Schema: http://ftp.ebi.ac.uk/pub/databases/chembl/ChEMBLdb/releases/chembl_23/chembl_23_schema.png
> 
> Documentation: http://ftp.ebi.ac.uk/pub/databases/chembl/ChEMBLdb/releases/chembl_23/schema_documentation.html
> 
> “ChEMBL” by the European Bioinformatics Institute (EMBL-EBI), used under CC BY-SA 3.0. Modifications have been made to add normalized publication numbers.





| Stat | Value |
|----------|----------|
| Last updated | 2018-10-31 |
| Rows | 1 |
| Size | 58 Bytes |

### Schema
[View in BigQuery](https://bigquery.cloud.google.com/table/patents-public-data:ebi_chembl.version_24)

* `name` STRING NULLABLE 

* `creation_date` STRING NULLABLE 

* `comments` STRING NULLABLE 














*****
## patents-public-data:ebi_surechembl.map



> SureChEMBL Data is a database of compounds extracted from the full text, images and attachments of patent documents.
> 
> “SureChEMBL” by the European Bioinformatics Institute (EMBL-EBI), used under CC BY-SA 3.0.





| Stat | Value |
|----------|----------|
| Last updated | 2018-11-01 |
| Rows | 278,559,964 |
| Size | 37.3 GB |

### Schema
[View in BigQuery](https://bigquery.cloud.google.com/table/patents-public-data:ebi_surechembl.map)

* `schembl_id` STRING NULLABLE 

* `smiles` STRING NULLABLE 

* `inchi_key` STRING NULLABLE 

* `corpus_frequency` STRING NULLABLE 

* `patent_id` STRING NULLABLE  joins on **SureChEMBL patent_id**

* `publication_date` STRING NULLABLE 

* `field` STRING NULLABLE 

* `field_frequency` STRING NULLABLE 



### Join columns










#### patent_id

joins to `patents-public-data:ebi_surechembl.match::patent_id` on **SureChEMBL patent_id** (100.00%, 278,559,964 rows)

| Key | Percent | Rows | Sample values |
|------|-----|--------|--------------------------------------------------------|
| `all` | 100.00% | 278,559,964 | `['US-20050038031-A1', 'US-7666895-B2', 'EP-1876174-B1', 'US-20060156484-A1', 'WO-2001034626-A1']` |


    #standardSQL
    SELECT
      COUNT(*) AS cnt,
      COUNT(second.second_column) AS second_cnt,
      ARRAY_AGG(first.patent_id IGNORE NULLS ORDER BY RAND() LIMIT 5) AS sample_value
    FROM `patents-public-data.ebi_surechembl.map`AS first
    LEFT JOIN (
      SELECT patent_id AS second_column, COUNT(*) AS cnt
      FROM `patents-public-data.ebi_surechembl.match`
      GROUP BY 1
    ) AS second ON first.patent_id = second.second_column



joins from `patents-public-data:ebi_surechembl.match::patent_id` on **SureChEMBL patent_id** (100.00%, 4,227,188 rows)












*****
## patents-public-data:ebi_surechembl.map_201710


Old table version `201710`, schema skipped.





*****
## patents-public-data:ebi_surechembl.match



> SureChEMBL Data is a database of compounds extracted from the full text, images and attachments of patent documents.
> 
> “SureChEMBL” by the European Bioinformatics Institute (EMBL-EBI), used under CC BY-SA 3.0.





| Stat | Value |
|----------|----------|
| Last updated | 2018-11-01 |
| Rows | 4,227,188 |
| Size | 136.9 MB |

### Schema
[View in BigQuery](https://bigquery.cloud.google.com/table/patents-public-data:ebi_surechembl.match)

* `patent_id` STRING NULLABLE  joins on **SureChEMBL patent_id**

* `publication_number` STRING NULLABLE  joins on **publication_number**



### Join columns


#### patent_id

joins to `patents-public-data:ebi_surechembl.map::patent_id` on **SureChEMBL patent_id** (100.00%, 4,227,188 rows)

| Key | Percent | Rows | Sample values |
|------|-----|--------|--------------------------------------------------------|
| `all` | 100.00% | 4,227,188 | `['US-9650617-B2', 'US-6011168-A', 'US-20100323423-A1', 'EP-3261436-A1', 'EP-2308977-B1']` |


    #standardSQL
    SELECT
      COUNT(*) AS cnt,
      COUNT(second.second_column) AS second_cnt,
      ARRAY_AGG(first.patent_id IGNORE NULLS ORDER BY RAND() LIMIT 5) AS sample_value
    FROM `patents-public-data.ebi_surechembl.match`AS first
    LEFT JOIN (
      SELECT patent_id AS second_column, COUNT(*) AS cnt
      FROM `patents-public-data.ebi_surechembl.map`
      GROUP BY 1
    ) AS second ON first.patent_id = second.second_column



joins from `patents-public-data:ebi_surechembl.map::patent_id` on **SureChEMBL patent_id** (100.00%, 278,559,964 rows)




#### publication_number

joins to `patents-public-data:patents.publications::publication_number` on **publication_number** (99.73%, 4,215,650 rows)

| Key | Percent | Rows | Sample values |
|------|-----|--------|--------------------------------------------------------|
| `all` | 99.73% | 4,215,650 | `['WO-2013122645-A1', 'JP-S5289676-A', 'US-6159510-A', 'US-2014093505-A1', 'US-2005272899-A1']` |


    #standardSQL
    SELECT
      COUNT(*) AS cnt,
      COUNT(second.second_column) AS second_cnt,
      ARRAY_AGG(first.publication_number IGNORE NULLS ORDER BY RAND() LIMIT 5) AS sample_value
    FROM `patents-public-data.ebi_surechembl.match`AS first
    LEFT JOIN (
      SELECT publication_number AS second_column, COUNT(*) AS cnt
      FROM `patents-public-data.patents.publications`
      GROUP BY 1
    ) AS second ON first.publication_number = second.second_column



joins from `patents-public-data:patents.publications::publication_number` on **publication_number** (4.29%, 4,215,650 rows)






*****
## patents-public-data:ebi_surechembl.match_201710


Old table version `201710`, schema skipped.




