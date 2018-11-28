
---
geometry: margin=0.6in
---

# USPTO


*****
## patents-public-data:patentsview.application



> PatentsView Data is a database that longitudinally links inventors, their organizations, locations, and overall patenting activity. The dataset uses data derived from USPTO bulk data files.
> 
> “PatentsView” by the USPTO, US Department of Agriculture (USDA), the Center for the Science of Science and Innovation Policy, New York University, the University of California at Berkeley, Twin Arch Technologies, and Periscopic, used under CC BY 4.0.





| Stat | Value |
|----------|----------|
| Last updated | 2017-10-13 |
| Rows | 6,366,664 |
| Size | 318.3 MB |

### Schema
[View in BigQuery](https://bigquery.cloud.google.com/table/patents-public-data:patentsview.application)

* `id` STRING  

* `patent_id` STRING   joins on **PatentsView patent_id**

* `series_code` STRING  

* `number` STRING  

* `country` STRING  

* `date` STRING  



### Join columns




#### patent_id

joins to `patents-public-data:patentsview.patent::id` on **PatentsView patent_id** (100.00%, 6,366,664 rows)

| Key | Percent | Rows | Sample values |
|------|-----|--------|--------------------------------------------------------|
| `all` | 100.00% | 6,366,664 | `['8389167', '6069629', '5948887', '9124985', '5368643']` |


    #standardSQL
    SELECT
      COUNT(*) AS cnt,
      COUNT(second.second_column) AS second_cnt,
      ARRAY_AGG(first.patent_id IGNORE NULLS ORDER BY RAND() LIMIT 5) AS sample_value
    FROM `patents-public-data.patentsview.application`AS first
    LEFT JOIN (
      SELECT id AS second_column, COUNT(*) AS cnt
      FROM `patents-public-data.patentsview.patent`
      GROUP BY 1
    ) AS second ON first.patent_id = second.second_column



joins from `patents-public-data:patentsview.patent::id` on **PatentsView patent_id** (100.00%, 6,366,664 rows)














*****
## patents-public-data:patentsview.application_201708


Old table version `201708`, schema skipped.





*****
## patents-public-data:patentsview.assignee



> PatentsView Data is a database that longitudinally links inventors, their organizations, locations, and overall patenting activity. The dataset uses data derived from USPTO bulk data files.
> 
> “PatentsView” by the USPTO, US Department of Agriculture (USDA), the Center for the Science of Science and Innovation Policy, New York University, the University of California at Berkeley, Twin Arch Technologies, and Periscopic, used under CC BY 4.0.





| Stat | Value |
|----------|----------|
| Last updated | 2017-10-13 |
| Rows | 376,913 |
| Size | 24.1 MB |

### Schema
[View in BigQuery](https://bigquery.cloud.google.com/table/patents-public-data:patentsview.assignee)

* `id` STRING  

* `type` STRING  

* `name_first` STRING  

* `name_last` STRING  

* `organization` STRING  


















*****
## patents-public-data:patentsview.assignee_201708


Old table version `201708`, schema skipped.





*****
## patents-public-data:patentsview.botanic



> PatentsView Data is a database that longitudinally links inventors, their organizations, locations, and overall patenting activity. The dataset uses data derived from USPTO bulk data files.
> 
> “PatentsView” by the USPTO, US Department of Agriculture (USDA), the Center for the Science of Science and Innovation Policy, New York University, the University of California at Berkeley, Twin Arch Technologies, and Periscopic, used under CC BY 4.0.





| Stat | Value |
|----------|----------|
| Last updated | 2017-10-13 |
| Rows | 12,805 |
| Size | 894.2 kB |

### Schema
[View in BigQuery](https://bigquery.cloud.google.com/table/patents-public-data:patentsview.botanic)

* `uuid` STRING  

* `patent_id` STRING   joins on **PatentsView patent_id**

* `latin_name` STRING  

* `variety` STRING  



### Join columns




#### patent_id

joins to `patents-public-data:patentsview.patent::id` on **PatentsView patent_id** (100.00%, 12,805 rows)

| Key | Percent | Rows | Sample values |
|------|-----|--------|--------------------------------------------------------|
| `all` | 100.00% | 12,805 | `['PP24882', 'PP22333', 'PP20400', 'PP21038', 'PP17235']` |


    #standardSQL
    SELECT
      COUNT(*) AS cnt,
      COUNT(second.second_column) AS second_cnt,
      ARRAY_AGG(first.patent_id IGNORE NULLS ORDER BY RAND() LIMIT 5) AS sample_value
    FROM `patents-public-data.patentsview.botanic`AS first
    LEFT JOIN (
      SELECT id AS second_column, COUNT(*) AS cnt
      FROM `patents-public-data.patentsview.patent`
      GROUP BY 1
    ) AS second ON first.patent_id = second.second_column



joins from `patents-public-data:patentsview.patent::id` on **PatentsView patent_id** (0.20%, 12,805 rows)










*****
## patents-public-data:patentsview.botanic_201708


Old table version `201708`, schema skipped.





*****
## patents-public-data:patentsview.brf_sum_text



> PatentsView Data is a database that longitudinally links inventors, their organizations, locations, and overall patenting activity. The dataset uses data derived from USPTO bulk data files.
> 
> “PatentsView” by the USPTO, US Department of Agriculture (USDA), the Center for the Science of Science and Innovation Policy, New York University, the University of California at Berkeley, Twin Arch Technologies, and Periscopic, used under CC BY 4.0.





| Stat | Value |
|----------|----------|
| Last updated | 2017-10-13 |
| Rows | 5,813,766 |
| Size | 52.7 GB |

### Schema
[View in BigQuery](https://bigquery.cloud.google.com/table/patents-public-data:patentsview.brf_sum_text)

* `uuid` STRING  

* `patent_id` STRING   joins on **PatentsView patent_id**

* `text` STRING  



### Join columns




#### patent_id

joins to `patents-public-data:patentsview.patent::id` on **PatentsView patent_id** (100.00%, 5,813,766 rows)

| Key | Percent | Rows | Sample values |
|------|-----|--------|--------------------------------------------------------|
| `all` | 100.00% | 5,813,766 | `['RE34164', '6310232', '8433229', '4979115', '4997900']` |


    #standardSQL
    SELECT
      COUNT(*) AS cnt,
      COUNT(second.second_column) AS second_cnt,
      ARRAY_AGG(first.patent_id IGNORE NULLS ORDER BY RAND() LIMIT 5) AS sample_value
    FROM `patents-public-data.patentsview.brf_sum_text`AS first
    LEFT JOIN (
      SELECT id AS second_column, COUNT(*) AS cnt
      FROM `patents-public-data.patentsview.patent`
      GROUP BY 1
    ) AS second ON first.patent_id = second.second_column



joins from `patents-public-data:patentsview.patent::id` on **PatentsView patent_id** (91.32%, 5,813,766 rows)








*****
## patents-public-data:patentsview.brf_sum_text_201708


Old table version `201708`, schema skipped.





*****
## patents-public-data:patentsview.claim



> PatentsView Data is a database that longitudinally links inventors, their organizations, locations, and overall patenting activity. The dataset uses data derived from USPTO bulk data files.
> 
> “PatentsView” by the USPTO, US Department of Agriculture (USDA), the Center for the Science of Science and Innovation Policy, New York University, the University of California at Berkeley, Twin Arch Technologies, and Periscopic, used under CC BY 4.0.





| Stat | Value |
|----------|----------|
| Last updated | 2017-10-13 |
| Rows | 89,944,541 |
| Size | 39.1 GB |

### Schema
[View in BigQuery](https://bigquery.cloud.google.com/table/patents-public-data:patentsview.claim)

* `uuid` STRING  

* `patent_id` STRING   joins on **PatentsView patent_id**

* `text` STRING  

* `dependent` STRING  

* `sequence` STRING  

* `exemplary` STRING  



### Join columns




#### patent_id

joins to `patents-public-data:patentsview.patent::id` on **PatentsView patent_id** (100.00%, 89,944,541 rows)

| Key | Percent | Rows | Sample values |
|------|-----|--------|--------------------------------------------------------|
| `all` | 100.00% | 89,944,541 | `['7670426', '7324448', '7700871', '8995983', '6595904']` |


    #standardSQL
    SELECT
      COUNT(*) AS cnt,
      COUNT(second.second_column) AS second_cnt,
      ARRAY_AGG(first.patent_id IGNORE NULLS ORDER BY RAND() LIMIT 5) AS sample_value
    FROM `patents-public-data.patentsview.claim`AS first
    LEFT JOIN (
      SELECT id AS second_column, COUNT(*) AS cnt
      FROM `patents-public-data.patentsview.patent`
      GROUP BY 1
    ) AS second ON first.patent_id = second.second_column



joins from `patents-public-data:patentsview.patent::id` on **PatentsView patent_id** (99.99%, 6,366,040 rows)














*****
## patents-public-data:patentsview.claim_201708


Old table version `201708`, schema skipped.





*****
## patents-public-data:patentsview.cpc_current



> PatentsView Data is a database that longitudinally links inventors, their organizations, locations, and overall patenting activity. The dataset uses data derived from USPTO bulk data files.
> 
> “PatentsView” by the USPTO, US Department of Agriculture (USDA), the Center for the Science of Science and Innovation Policy, New York University, the University of California at Berkeley, Twin Arch Technologies, and Periscopic, used under CC BY 4.0.





| Stat | Value |
|----------|----------|
| Last updated | 2017-10-13 |
| Rows | 32,874,742 |
| Size | 2.6 GB |

### Schema
[View in BigQuery](https://bigquery.cloud.google.com/table/patents-public-data:patentsview.cpc_current)

* `uuid` STRING  

* `patent_id` STRING   joins on **PatentsView patent_id**

* `section_id` STRING  

* `subsection_id` STRING  

* `group_id` STRING  

* `subgroup_id` STRING  

* `category` STRING  

* `sequence` STRING  



### Join columns




#### patent_id

joins to `patents-public-data:patentsview.patent::id` on **PatentsView patent_id** (100.00%, 32,874,742 rows)

| Key | Percent | Rows | Sample values |
|------|-----|--------|--------------------------------------------------------|
| `all` | 100.00% | 32,874,742 | `['6076688', '8952557', '7936936', '6116364', '8283061']` |


    #standardSQL
    SELECT
      COUNT(*) AS cnt,
      COUNT(second.second_column) AS second_cnt,
      ARRAY_AGG(first.patent_id IGNORE NULLS ORDER BY RAND() LIMIT 5) AS sample_value
    FROM `patents-public-data.patentsview.cpc_current`AS first
    LEFT JOIN (
      SELECT id AS second_column, COUNT(*) AS cnt
      FROM `patents-public-data.patentsview.patent`
      GROUP BY 1
    ) AS second ON first.patent_id = second.second_column



joins from `patents-public-data:patentsview.patent::id` on **PatentsView patent_id** (90.34%, 5,751,595 rows)


















*****
## patents-public-data:patentsview.cpc_current_201708


Old table version `201708`, schema skipped.





*****
## patents-public-data:patentsview.cpc_group



> PatentsView Data is a database that longitudinally links inventors, their organizations, locations, and overall patenting activity. The dataset uses data derived from USPTO bulk data files.
> 
> “PatentsView” by the USPTO, US Department of Agriculture (USDA), the Center for the Science of Science and Innovation Policy, New York University, the University of California at Berkeley, Twin Arch Technologies, and Periscopic, used under CC BY 4.0.





| Stat | Value |
|----------|----------|
| Last updated | 2017-10-13 |
| Rows | 656 |
| Size | 59.6 kB |

### Schema
[View in BigQuery](https://bigquery.cloud.google.com/table/patents-public-data:patentsview.cpc_group)

* `id` STRING  

* `title` STRING  












*****
## patents-public-data:patentsview.cpc_group_201708


Old table version `201708`, schema skipped.





*****
## patents-public-data:patentsview.cpc_subgroup



> PatentsView Data is a database that longitudinally links inventors, their organizations, locations, and overall patenting activity. The dataset uses data derived from USPTO bulk data files.
> 
> “PatentsView” by the USPTO, US Department of Agriculture (USDA), the Center for the Science of Science and Innovation Policy, New York University, the University of California at Berkeley, Twin Arch Technologies, and Periscopic, used under CC BY 4.0.





| Stat | Value |
|----------|----------|
| Last updated | 2017-10-13 |
| Rows | 259,048 |
| Size | 62.9 MB |

### Schema
[View in BigQuery](https://bigquery.cloud.google.com/table/patents-public-data:patentsview.cpc_subgroup)

* `id` STRING  

* `title` STRING  












*****
## patents-public-data:patentsview.cpc_subgroup_201708


Old table version `201708`, schema skipped.





*****
## patents-public-data:patentsview.cpc_subsection



> PatentsView Data is a database that longitudinally links inventors, their organizations, locations, and overall patenting activity. The dataset uses data derived from USPTO bulk data files.
> 
> “PatentsView” by the USPTO, US Department of Agriculture (USDA), the Center for the Science of Science and Innovation Policy, New York University, the University of California at Berkeley, Twin Arch Technologies, and Periscopic, used under CC BY 4.0.





| Stat | Value |
|----------|----------|
| Last updated | 2017-10-13 |
| Rows | 127 |
| Size | 6.2 kB |

### Schema
[View in BigQuery](https://bigquery.cloud.google.com/table/patents-public-data:patentsview.cpc_subsection)

* `id` STRING  

* `title` STRING  












*****
## patents-public-data:patentsview.cpc_subsection_201708


Old table version `201708`, schema skipped.





*****
## patents-public-data:patentsview.draw_desc_text



> PatentsView Data is a database that longitudinally links inventors, their organizations, locations, and overall patenting activity. The dataset uses data derived from USPTO bulk data files.
> 
> “PatentsView” by the USPTO, US Department of Agriculture (USDA), the Center for the Science of Science and Innovation Policy, New York University, the University of California at Berkeley, Twin Arch Technologies, and Periscopic, used under CC BY 4.0.





| Stat | Value |
|----------|----------|
| Last updated | 2017-10-13 |
| Rows | 61,307,429 |
| Size | 10.4 GB |

### Schema
[View in BigQuery](https://bigquery.cloud.google.com/table/patents-public-data:patentsview.draw_desc_text)

* `uuid` STRING  

* `patent_id` STRING   joins on **PatentsView patent_id**

* `text` STRING  

* `sequence` STRING  



### Join columns




#### patent_id

joins to `patents-public-data:patentsview.patent::id` on **PatentsView patent_id** (100.00%, 61,307,429 rows)

| Key | Percent | Rows | Sample values |
|------|-----|--------|--------------------------------------------------------|
| `all` | 100.00% | 61,307,429 | `['9505376', '7631319', '6842942', '7697406', '8578015']` |


    #standardSQL
    SELECT
      COUNT(*) AS cnt,
      COUNT(second.second_column) AS second_cnt,
      ARRAY_AGG(first.patent_id IGNORE NULLS ORDER BY RAND() LIMIT 5) AS sample_value
    FROM `patents-public-data.patentsview.draw_desc_text`AS first
    LEFT JOIN (
      SELECT id AS second_column, COUNT(*) AS cnt
      FROM `patents-public-data.patentsview.patent`
      GROUP BY 1
    ) AS second ON first.patent_id = second.second_column



joins from `patents-public-data:patentsview.patent::id` on **PatentsView patent_id** (88.78%, 5,652,621 rows)










*****
## patents-public-data:patentsview.draw_desc_text_201708


Old table version `201708`, schema skipped.





*****
## patents-public-data:patentsview.figures



> PatentsView Data is a database that longitudinally links inventors, their organizations, locations, and overall patenting activity. The dataset uses data derived from USPTO bulk data files.
> 
> “PatentsView” by the USPTO, US Department of Agriculture (USDA), the Center for the Science of Science and Innovation Policy, New York University, the University of California at Berkeley, Twin Arch Technologies, and Periscopic, used under CC BY 4.0.





| Stat | Value |
|----------|----------|
| Last updated | 2017-10-13 |
| Rows | 5,875,847 |
| Size | 250.4 MB |

### Schema
[View in BigQuery](https://bigquery.cloud.google.com/table/patents-public-data:patentsview.figures)

* `uuid` STRING  

* `patent_id` STRING   joins on **PatentsView patent_id**

* `num_figures` STRING  

* `num_sheets` STRING  



### Join columns




#### patent_id

joins to `patents-public-data:patentsview.patent::id` on **PatentsView patent_id** (100.00%, 5,875,847 rows)

| Key | Percent | Rows | Sample values |
|------|-----|--------|--------------------------------------------------------|
| `all` | 100.00% | 5,875,847 | `['5071090', '7291378', '8423231', '4603918', '8239509']` |


    #standardSQL
    SELECT
      COUNT(*) AS cnt,
      COUNT(second.second_column) AS second_cnt,
      ARRAY_AGG(first.patent_id IGNORE NULLS ORDER BY RAND() LIMIT 5) AS sample_value
    FROM `patents-public-data.patentsview.figures`AS first
    LEFT JOIN (
      SELECT id AS second_column, COUNT(*) AS cnt
      FROM `patents-public-data.patentsview.patent`
      GROUP BY 1
    ) AS second ON first.patent_id = second.second_column



joins from `patents-public-data:patentsview.patent::id` on **PatentsView patent_id** (92.29%, 5,875,847 rows)










*****
## patents-public-data:patentsview.figures_201708


Old table version `201708`, schema skipped.





*****
## patents-public-data:patentsview.foreign_priority



> PatentsView Data is a database that longitudinally links inventors, their organizations, locations, and overall patenting activity. The dataset uses data derived from USPTO bulk data files.
> 
> “PatentsView” by the USPTO, US Department of Agriculture (USDA), the Center for the Science of Science and Innovation Policy, New York University, the University of California at Berkeley, Twin Arch Technologies, and Periscopic, used under CC BY 4.0.





| Stat | Value |
|----------|----------|
| Last updated | 2017-10-13 |
| Rows | 2,992,770 |
| Size | 233.8 MB |

### Schema
[View in BigQuery](https://bigquery.cloud.google.com/table/patents-public-data:patentsview.foreign_priority)

* `uuid` STRING  

* `patent_id` STRING   joins on **PatentsView patent_id**

* `sequence` STRING  

* `kind` STRING  

* `number` STRING  

* `date` STRING  

* `country` STRING  

* `country_transformed` STRING  



### Join columns




#### patent_id

joins to `patents-public-data:patentsview.patent::id` on **PatentsView patent_id** (100.00%, 2,992,770 rows)

| Key | Percent | Rows | Sample values |
|------|-----|--------|--------------------------------------------------------|
| `all` | 100.00% | 2,992,770 | `['6863171', 'D377636', '4950234', '6766661', '6321696']` |


    #standardSQL
    SELECT
      COUNT(*) AS cnt,
      COUNT(second.second_column) AS second_cnt,
      ARRAY_AGG(first.patent_id IGNORE NULLS ORDER BY RAND() LIMIT 5) AS sample_value
    FROM `patents-public-data.patentsview.foreign_priority`AS first
    LEFT JOIN (
      SELECT id AS second_column, COUNT(*) AS cnt
      FROM `patents-public-data.patentsview.patent`
      GROUP BY 1
    ) AS second ON first.patent_id = second.second_column



joins from `patents-public-data:patentsview.patent::id` on **PatentsView patent_id** (37.32%, 2,376,338 rows)


















*****
## patents-public-data:patentsview.foreign_priority_201708


Old table version `201708`, schema skipped.





*****
## patents-public-data:patentsview.foreigncitation



> PatentsView Data is a database that longitudinally links inventors, their organizations, locations, and overall patenting activity. The dataset uses data derived from USPTO bulk data files.
> 
> “PatentsView” by the USPTO, US Department of Agriculture (USDA), the Center for the Science of Science and Innovation Policy, New York University, the University of California at Berkeley, Twin Arch Technologies, and Periscopic, used under CC BY 4.0.





| Stat | Value |
|----------|----------|
| Last updated | 2017-10-13 |
| Rows | 22,020,427 |
| Size | 1.8 GB |

### Schema
[View in BigQuery](https://bigquery.cloud.google.com/table/patents-public-data:patentsview.foreigncitation)

* `uuid` STRING  

* `patent_id` STRING   joins on **PatentsView patent_id**

* `date` STRING  

* `number` STRING  

* `country` STRING  

* `category` STRING  

* `sequence` STRING  



### Join columns




#### patent_id

joins to `patents-public-data:patentsview.patent::id` on **PatentsView patent_id** (100.00%, 22,020,427 rows)

| Key | Percent | Rows | Sample values |
|------|-----|--------|--------------------------------------------------------|
| `all` | 100.00% | 22,020,427 | `['7073061', '8174881', '9369142', '8980291', '7963467']` |


    #standardSQL
    SELECT
      COUNT(*) AS cnt,
      COUNT(second.second_column) AS second_cnt,
      ARRAY_AGG(first.patent_id IGNORE NULLS ORDER BY RAND() LIMIT 5) AS sample_value
    FROM `patents-public-data.patentsview.foreigncitation`AS first
    LEFT JOIN (
      SELECT id AS second_column, COUNT(*) AS cnt
      FROM `patents-public-data.patentsview.patent`
      GROUP BY 1
    ) AS second ON first.patent_id = second.second_column



joins from `patents-public-data:patentsview.patent::id` on **PatentsView patent_id** (52.53%, 3,344,703 rows)
















*****
## patents-public-data:patentsview.foreigncitation_201708


Old table version `201708`, schema skipped.





*****
## patents-public-data:patentsview.government_interest



> PatentsView Data is a database that longitudinally links inventors, their organizations, locations, and overall patenting activity. The dataset uses data derived from USPTO bulk data files.
> 
> “PatentsView” by the USPTO, US Department of Agriculture (USDA), the Center for the Science of Science and Innovation Policy, New York University, the University of California at Berkeley, Twin Arch Technologies, and Periscopic, used under CC BY 4.0.





| Stat | Value |
|----------|----------|
| Last updated | 2017-10-13 |
| Rows | 127,367 |
| Size | 26.4 MB |

### Schema
[View in BigQuery](https://bigquery.cloud.google.com/table/patents-public-data:patentsview.government_interest)

* `patent_id` STRING   joins on **PatentsView patent_id**

* `gi_statement` STRING  



### Join columns


#### patent_id

joins to `patents-public-data:patentsview.patent::id` on **PatentsView patent_id** (99.34%, 126,528 rows)

| Key | Percent | Rows | Sample values |
|------|-----|--------|--------------------------------------------------------|
| `all` | 99.34% | 126,528 | `['9595676', '9368710', '7147861', '5442548', '8751151']` |


    #standardSQL
    SELECT
      COUNT(*) AS cnt,
      COUNT(second.second_column) AS second_cnt,
      ARRAY_AGG(first.patent_id IGNORE NULLS ORDER BY RAND() LIMIT 5) AS sample_value
    FROM `patents-public-data.patentsview.government_interest`AS first
    LEFT JOIN (
      SELECT id AS second_column, COUNT(*) AS cnt
      FROM `patents-public-data.patentsview.patent`
      GROUP BY 1
    ) AS second ON first.patent_id = second.second_column



joins from `patents-public-data:patentsview.patent::id` on **PatentsView patent_id** (1.99%, 126,528 rows)








*****
## patents-public-data:patentsview.government_interest_201708


Old table version `201708`, schema skipped.





*****
## patents-public-data:patentsview.government_organization



> PatentsView Data is a database that longitudinally links inventors, their organizations, locations, and overall patenting activity. The dataset uses data derived from USPTO bulk data files.
> 
> “PatentsView” by the USPTO, US Department of Agriculture (USDA), the Center for the Science of Science and Innovation Policy, New York University, the University of California at Berkeley, Twin Arch Technologies, and Periscopic, used under CC BY 4.0.





| Stat | Value |
|----------|----------|
| Last updated | 2017-10-13 |
| Rows | 139 |
| Size | 14.5 kB |

### Schema
[View in BigQuery](https://bigquery.cloud.google.com/table/patents-public-data:patentsview.government_organization)

* `organization_id` STRING  

* `name` STRING  

* `level_one` STRING  

* `level_two` STRING  

* `level_three` STRING  


















*****
## patents-public-data:patentsview.government_organization_201708


Old table version `201708`, schema skipped.





*****
## patents-public-data:patentsview.inventor



> PatentsView Data is a database that longitudinally links inventors, their organizations, locations, and overall patenting activity. The dataset uses data derived from USPTO bulk data files.
> 
> “PatentsView” by the USPTO, US Department of Agriculture (USDA), the Center for the Science of Science and Innovation Policy, New York University, the University of California at Berkeley, Twin Arch Technologies, and Periscopic, used under CC BY 4.0.





| Stat | Value |
|----------|----------|
| Last updated | 2017-10-13 |
| Rows | 3,482,305 |
| Size | 102.7 MB |

### Schema
[View in BigQuery](https://bigquery.cloud.google.com/table/patents-public-data:patentsview.inventor)

* `id` STRING  

* `name_first` STRING  

* `name_last` STRING  














*****
## patents-public-data:patentsview.inventor_201708


Old table version `201708`, schema skipped.





*****
## patents-public-data:patentsview.ipcr



> PatentsView Data is a database that longitudinally links inventors, their organizations, locations, and overall patenting activity. The dataset uses data derived from USPTO bulk data files.
> 
> “PatentsView” by the USPTO, US Department of Agriculture (USDA), the Center for the Science of Science and Innovation Policy, New York University, the University of California at Berkeley, Twin Arch Technologies, and Periscopic, used under CC BY 4.0.





| Stat | Value |
|----------|----------|
| Last updated | 2017-10-13 |
| Rows | 11,557,735 |
| Size | 1.1 GB |

### Schema
[View in BigQuery](https://bigquery.cloud.google.com/table/patents-public-data:patentsview.ipcr)

* `uuid` STRING  

* `patent_id` STRING   joins on **PatentsView patent_id**

* `classification_level` STRING  

* `section` STRING  

* `ipc_class` STRING  

* `subclass` STRING  

* `main_group` STRING  

* `subgroup` STRING  

* `symbol_position` STRING  

* `classification_value` STRING  

* `classification_status` STRING  

* `classification_data_source` STRING  

* `action_date` STRING  

* `ipc_version_indicator` STRING  

* `sequence` STRING  



### Join columns




#### patent_id

joins to `patents-public-data:patentsview.patent::id` on **PatentsView patent_id** (100.00%, 11,557,735 rows)

| Key | Percent | Rows | Sample values |
|------|-----|--------|--------------------------------------------------------|
| `all` | 100.00% | 11,557,735 | `['4319089', '9159586', '6245972', '8480132', '8157281']` |


    #standardSQL
    SELECT
      COUNT(*) AS cnt,
      COUNT(second.second_column) AS second_cnt,
      ARRAY_AGG(first.patent_id IGNORE NULLS ORDER BY RAND() LIMIT 5) AS sample_value
    FROM `patents-public-data.patentsview.ipcr`AS first
    LEFT JOIN (
      SELECT id AS second_column, COUNT(*) AS cnt
      FROM `patents-public-data.patentsview.patent`
      GROUP BY 1
    ) AS second ON first.patent_id = second.second_column



joins from `patents-public-data:patentsview.patent::id` on **PatentsView patent_id** (91.44%, 5,821,568 rows)
































*****
## patents-public-data:patentsview.ipcr_201708


Old table version `201708`, schema skipped.





*****
## patents-public-data:patentsview.lawyer



> PatentsView Data is a database that longitudinally links inventors, their organizations, locations, and overall patenting activity. The dataset uses data derived from USPTO bulk data files.
> 
> “PatentsView” by the USPTO, US Department of Agriculture (USDA), the Center for the Science of Science and Innovation Policy, New York University, the University of California at Berkeley, Twin Arch Technologies, and Periscopic, used under CC BY 4.0.





| Stat | Value |
|----------|----------|
| Last updated | 2017-10-13 |
| Rows | 165,025 |
| Size | 10.6 MB |

### Schema
[View in BigQuery](https://bigquery.cloud.google.com/table/patents-public-data:patentsview.lawyer)

* `id` STRING  

* `name_first` STRING  

* `name_last` STRING  

* `organization` STRING  

* `country` STRING  


















*****
## patents-public-data:patentsview.lawyer_201708


Old table version `201708`, schema skipped.





*****
## patents-public-data:patentsview.location



> PatentsView Data is a database that longitudinally links inventors, their organizations, locations, and overall patenting activity. The dataset uses data derived from USPTO bulk data files.
> 
> “PatentsView” by the USPTO, US Department of Agriculture (USDA), the Center for the Science of Science and Innovation Policy, New York University, the University of California at Berkeley, Twin Arch Technologies, and Periscopic, used under CC BY 4.0.





| Stat | Value |
|----------|----------|
| Last updated | 2017-10-13 |
| Rows | 129,303 |
| Size | 8.0 MB |

### Schema
[View in BigQuery](https://bigquery.cloud.google.com/table/patents-public-data:patentsview.location)

* `id` STRING  

* `city` STRING  

* `state` STRING  

* `country` STRING  

* `latitude` STRING  

* `longitude` STRING  

* `county` STRING  

* `state_fips` STRING  

* `county_fips` STRING  


























*****
## patents-public-data:patentsview.location_201708


Old table version `201708`, schema skipped.





*****
## patents-public-data:patentsview.location_assignee



> PatentsView Data is a database that longitudinally links inventors, their organizations, locations, and overall patenting activity. The dataset uses data derived from USPTO bulk data files.
> 
> “PatentsView” by the USPTO, US Department of Agriculture (USDA), the Center for the Science of Science and Innovation Policy, New York University, the University of California at Berkeley, Twin Arch Technologies, and Periscopic, used under CC BY 4.0.





| Stat | Value |
|----------|----------|
| Last updated | 2017-10-13 |
| Rows | 525,658 |
| Size | 25.2 MB |

### Schema
[View in BigQuery](https://bigquery.cloud.google.com/table/patents-public-data:patentsview.location_assignee)

* `location_id` STRING  

* `assignee_id` STRING  












*****
## patents-public-data:patentsview.location_assignee_201708


Old table version `201708`, schema skipped.





*****
## patents-public-data:patentsview.location_inventor



> PatentsView Data is a database that longitudinally links inventors, their organizations, locations, and overall patenting activity. The dataset uses data derived from USPTO bulk data files.
> 
> “PatentsView” by the USPTO, US Department of Agriculture (USDA), the Center for the Science of Science and Innovation Policy, New York University, the University of California at Berkeley, Twin Arch Technologies, and Periscopic, used under CC BY 4.0.





| Stat | Value |
|----------|----------|
| Last updated | 2017-10-13 |
| Rows | 4,798,996 |
| Size | 120.0 MB |

### Schema
[View in BigQuery](https://bigquery.cloud.google.com/table/patents-public-data:patentsview.location_inventor)

* `location_id` STRING  

* `inventor_id` STRING  












*****
## patents-public-data:patentsview.location_inventor_201708


Old table version `201708`, schema skipped.





*****
## patents-public-data:patentsview.mainclass



> PatentsView Data is a database that longitudinally links inventors, their organizations, locations, and overall patenting activity. The dataset uses data derived from USPTO bulk data files.
> 
> “PatentsView” by the USPTO, US Department of Agriculture (USDA), the Center for the Science of Science and Innovation Policy, New York University, the University of California at Berkeley, Twin Arch Technologies, and Periscopic, used under CC BY 4.0.





| Stat | Value |
|----------|----------|
| Last updated | 2017-10-13 |
| Rows | 1,237 |
| Size | 6.1 kB |

### Schema
[View in BigQuery](https://bigquery.cloud.google.com/table/patents-public-data:patentsview.mainclass)

* `id` STRING  










*****
## patents-public-data:patentsview.mainclass_201708


Old table version `201708`, schema skipped.





*****
## patents-public-data:patentsview.mainclass_current



> PatentsView Data is a database that longitudinally links inventors, their organizations, locations, and overall patenting activity. The dataset uses data derived from USPTO bulk data files.
> 
> “PatentsView” by the USPTO, US Department of Agriculture (USDA), the Center for the Science of Science and Innovation Policy, New York University, the University of California at Berkeley, Twin Arch Technologies, and Periscopic, used under CC BY 4.0.





| Stat | Value |
|----------|----------|
| Last updated | 2017-10-13 |
| Rows | 511 |
| Size | 20.2 kB |

### Schema
[View in BigQuery](https://bigquery.cloud.google.com/table/patents-public-data:patentsview.mainclass_current)

* `id` STRING  

* `title` STRING  












*****
## patents-public-data:patentsview.mainclass_current_201708


Old table version `201708`, schema skipped.





*****
## patents-public-data:patentsview.match



> PatentsView Data is a database that longitudinally links inventors, their organizations, locations, and overall patenting activity. The dataset uses data derived from USPTO bulk data files.
> 
> “PatentsView” by the USPTO, US Department of Agriculture (USDA), the Center for the Science of Science and Innovation Policy, New York University, the University of California at Berkeley, Twin Arch Technologies, and Periscopic, used under CC BY 4.0.





| Stat | Value |
|----------|----------|
| Last updated | 2017-10-22 |
| Rows | 6,357,947 |
| Size | 149.8 MB |

### Schema
[View in BigQuery](https://bigquery.cloud.google.com/table/patents-public-data:patentsview.match)

* `patent_id` STRING NULLABLE  joins on **PatentsView patent_id**

* `publication_number` STRING NULLABLE  joins on **publication_number**



### Join columns


#### patent_id

joins to `patents-public-data:patentsview.patent::id` on **PatentsView patent_id** (100.00%, 6,357,947 rows)

| Key | Percent | Rows | Sample values |
|------|-----|--------|--------------------------------------------------------|
| `all` | 100.00% | 6,357,947 | `['7789625', '6278841', '6906014', '7445960', '7029697']` |


    #standardSQL
    SELECT
      COUNT(*) AS cnt,
      COUNT(second.second_column) AS second_cnt,
      ARRAY_AGG(first.patent_id IGNORE NULLS ORDER BY RAND() LIMIT 5) AS sample_value
    FROM `patents-public-data.patentsview.match`AS first
    LEFT JOIN (
      SELECT id AS second_column, COUNT(*) AS cnt
      FROM `patents-public-data.patentsview.patent`
      GROUP BY 1
    ) AS second ON first.patent_id = second.second_column



joins from `patents-public-data:patentsview.patent::id` on **PatentsView patent_id** (99.86%, 6,357,947 rows)




#### publication_number

joins to `patents-public-data:patents.publications::publication_number` on **publication_number** (99.93%, 6,353,198 rows)

| Key | Percent | Rows | Sample values |
|------|-----|--------|--------------------------------------------------------|
| `all` | 99.93% | 6,353,198 | `['US-9667102-B2', 'US-5479953-A', 'US-5526692-A', 'US-4208487-A', 'US-6634924-B1']` |


    #standardSQL
    SELECT
      COUNT(*) AS cnt,
      COUNT(second.second_column) AS second_cnt,
      ARRAY_AGG(first.publication_number IGNORE NULLS ORDER BY RAND() LIMIT 5) AS sample_value
    FROM `patents-public-data.patentsview.match`AS first
    LEFT JOIN (
      SELECT publication_number AS second_column, COUNT(*) AS cnt
      FROM `patents-public-data.patents.publications`
      GROUP BY 1
    ) AS second ON first.publication_number = second.second_column



joins from `patents-public-data:patents.publications::publication_number` on **publication_number** (6.47%, 6,353,172 rows)






*****
## patents-public-data:patentsview.match_201780


Old table version `201780`, schema skipped.





*****
## patents-public-data:patentsview.nber



> PatentsView Data is a database that longitudinally links inventors, their organizations, locations, and overall patenting activity. The dataset uses data derived from USPTO bulk data files.
> 
> “PatentsView” by the USPTO, US Department of Agriculture (USDA), the Center for the Science of Science and Innovation Policy, New York University, the University of California at Berkeley, Twin Arch Technologies, and Periscopic, used under CC BY 4.0.





| Stat | Value |
|----------|----------|
| Last updated | 2017-10-13 |
| Rows | 5,105,937 |
| Size | 219.6 MB |

### Schema
[View in BigQuery](https://bigquery.cloud.google.com/table/patents-public-data:patentsview.nber)

* `uuid` STRING  

* `patent_id` STRING   joins on **PatentsView patent_id**

* `category_id` STRING  

* `subcategory_id` STRING  



### Join columns




#### patent_id

joins to `patents-public-data:patentsview.patent::id` on **PatentsView patent_id** (100.00%, 5,105,937 rows)

| Key | Percent | Rows | Sample values |
|------|-----|--------|--------------------------------------------------------|
| `all` | 100.00% | 5,105,937 | `['4381400', '7504327', '5512221', '8080417', '6019526']` |


    #standardSQL
    SELECT
      COUNT(*) AS cnt,
      COUNT(second.second_column) AS second_cnt,
      ARRAY_AGG(first.patent_id IGNORE NULLS ORDER BY RAND() LIMIT 5) AS sample_value
    FROM `patents-public-data.patentsview.nber`AS first
    LEFT JOIN (
      SELECT id AS second_column, COUNT(*) AS cnt
      FROM `patents-public-data.patentsview.patent`
      GROUP BY 1
    ) AS second ON first.patent_id = second.second_column



joins from `patents-public-data:patentsview.patent::id` on **PatentsView patent_id** (80.20%, 5,105,937 rows)










*****
## patents-public-data:patentsview.nber_201708


Old table version `201708`, schema skipped.





*****
## patents-public-data:patentsview.nber_category



> PatentsView Data is a database that longitudinally links inventors, their organizations, locations, and overall patenting activity. The dataset uses data derived from USPTO bulk data files.
> 
> “PatentsView” by the USPTO, US Department of Agriculture (USDA), the Center for the Science of Science and Innovation Policy, New York University, the University of California at Berkeley, Twin Arch Technologies, and Periscopic, used under CC BY 4.0.





| Stat | Value |
|----------|----------|
| Last updated | 2017-10-13 |
| Rows | 6 |
| Size | 67 Bytes |

### Schema
[View in BigQuery](https://bigquery.cloud.google.com/table/patents-public-data:patentsview.nber_category)

* `id` STRING  

* `title` STRING  












*****
## patents-public-data:patentsview.nber_category_201708


Old table version `201708`, schema skipped.





*****
## patents-public-data:patentsview.nber_subcategory



> PatentsView Data is a database that longitudinally links inventors, their organizations, locations, and overall patenting activity. The dataset uses data derived from USPTO bulk data files.
> 
> “PatentsView” by the USPTO, US Department of Agriculture (USDA), the Center for the Science of Science and Innovation Policy, New York University, the University of California at Berkeley, Twin Arch Technologies, and Periscopic, used under CC BY 4.0.





| Stat | Value |
|----------|----------|
| Last updated | 2017-10-13 |
| Rows | 37 |
| Size | 819 Bytes |

### Schema
[View in BigQuery](https://bigquery.cloud.google.com/table/patents-public-data:patentsview.nber_subcategory)

* `id` STRING  

* `title` STRING  












*****
## patents-public-data:patentsview.nber_subcategory_201708


Old table version `201708`, schema skipped.





*****
## patents-public-data:patentsview.non_inventor_applicant



> PatentsView Data is a database that longitudinally links inventors, their organizations, locations, and overall patenting activity. The dataset uses data derived from USPTO bulk data files.
> 
> “PatentsView” by the USPTO, US Department of Agriculture (USDA), the Center for the Science of Science and Innovation Policy, New York University, the University of California at Berkeley, Twin Arch Technologies, and Periscopic, used under CC BY 4.0.





| Stat | Value |
|----------|----------|
| Last updated | 2017-10-13 |
| Rows | 598,855 |
| Size | 69.1 MB |

### Schema
[View in BigQuery](https://bigquery.cloud.google.com/table/patents-public-data:patentsview.non_inventor_applicant)

* `uuid` STRING  

* `patent_id` STRING   joins on **PatentsView patent_id**

* `rawlocation_id` STRING  

* `lname` STRING  

* `fname` STRING  

* `organization` STRING  

* `sequence` STRING  

* `designation` STRING  

* `applicant_type` STRING  



### Join columns




#### patent_id

joins to `patents-public-data:patentsview.patent::id` on **PatentsView patent_id** (100.00%, 598,855 rows)

| Key | Percent | Rows | Sample values |
|------|-----|--------|--------------------------------------------------------|
| `all` | 100.00% | 598,855 | `['D689382', '9719993', '8964375', '9285558', '8865723']` |


    #standardSQL
    SELECT
      COUNT(*) AS cnt,
      COUNT(second.second_column) AS second_cnt,
      ARRAY_AGG(first.patent_id IGNORE NULLS ORDER BY RAND() LIMIT 5) AS sample_value
    FROM `patents-public-data.patentsview.non_inventor_applicant`AS first
    LEFT JOIN (
      SELECT id AS second_column, COUNT(*) AS cnt
      FROM `patents-public-data.patentsview.patent`
      GROUP BY 1
    ) AS second ON first.patent_id = second.second_column



joins from `patents-public-data:patentsview.patent::id` on **PatentsView patent_id** (9.41%, 598,855 rows)




















*****
## patents-public-data:patentsview.non_inventor_applicant_201708


Old table version `201708`, schema skipped.





*****
## patents-public-data:patentsview.otherreference



> PatentsView Data is a database that longitudinally links inventors, their organizations, locations, and overall patenting activity. The dataset uses data derived from USPTO bulk data files.
> 
> “PatentsView” by the USPTO, US Department of Agriculture (USDA), the Center for the Science of Science and Innovation Policy, New York University, the University of California at Berkeley, Twin Arch Technologies, and Periscopic, used under CC BY 4.0.





| Stat | Value |
|----------|----------|
| Last updated | 2017-10-13 |
| Rows | 31,414,354 |
| Size | 5.8 GB |

### Schema
[View in BigQuery](https://bigquery.cloud.google.com/table/patents-public-data:patentsview.otherreference)

* `uuid` STRING  

* `patent_id` STRING   joins on **PatentsView patent_id**

* `text` STRING  

* `sequence` STRING  



### Join columns




#### patent_id

joins to `patents-public-data:patentsview.patent::id` on **PatentsView patent_id** (100.00%, 31,414,354 rows)

| Key | Percent | Rows | Sample values |
|------|-----|--------|--------------------------------------------------------|
| `all` | 100.00% | 31,414,354 | `['9443518', '6416998', '8314808', '7779707', '7695603']` |


    #standardSQL
    SELECT
      COUNT(*) AS cnt,
      COUNT(second.second_column) AS second_cnt,
      ARRAY_AGG(first.patent_id IGNORE NULLS ORDER BY RAND() LIMIT 5) AS sample_value
    FROM `patents-public-data.patentsview.otherreference`AS first
    LEFT JOIN (
      SELECT id AS second_column, COUNT(*) AS cnt
      FROM `patents-public-data.patentsview.patent`
      GROUP BY 1
    ) AS second ON first.patent_id = second.second_column



joins from `patents-public-data:patentsview.patent::id` on **PatentsView patent_id** (42.57%, 2,710,182 rows)










*****
## patents-public-data:patentsview.otherreference_201708


Old table version `201708`, schema skipped.





*****
## patents-public-data:patentsview.patent



> PatentsView Data is a database that longitudinally links inventors, their organizations, locations, and overall patenting activity. The dataset uses data derived from USPTO bulk data files.
> 
> “PatentsView” by the USPTO, US Department of Agriculture (USDA), the Center for the Science of Science and Innovation Policy, New York University, the University of California at Berkeley, Twin Arch Technologies, and Periscopic, used under CC BY 4.0.





| Stat | Value |
|----------|----------|
| Last updated | 2017-10-13 |
| Rows | 6,366,664 |
| Size | 5.0 GB |

### Schema
[View in BigQuery](https://bigquery.cloud.google.com/table/patents-public-data:patentsview.patent)

* `id` STRING   joins on **PatentsView patent_id**

* `type` STRING  

* `number` STRING  

* `country` STRING  

* `date` STRING  

* `abstract` STRING  

* `title` STRING  

* `kind` STRING  

* `num_claims` STRING  

* `filename` STRING  



### Join columns


#### id

joins to `patents-public-data:patentsview.application::patent_id` on **PatentsView patent_id** (100.00%, 6,366,664 rows)

| Key | Percent | Rows | Sample values |
|------|-----|--------|--------------------------------------------------------|
| `all` | 100.00% | 6,366,664 | `['6674890', '9254199', '5525579', '7470603', '5951143']` |


    #standardSQL
    SELECT
      COUNT(*) AS cnt,
      COUNT(second.second_column) AS second_cnt,
      ARRAY_AGG(first.id IGNORE NULLS ORDER BY RAND() LIMIT 5) AS sample_value
    FROM `patents-public-data.patentsview.patent`AS first
    LEFT JOIN (
      SELECT patent_id AS second_column, COUNT(*) AS cnt
      FROM `patents-public-data.patentsview.application`
      GROUP BY 1
    ) AS second ON first.id = second.second_column


joins to `patents-public-data:patentsview.botanic::patent_id` on **PatentsView patent_id** (0.20%, 12,805 rows)

| Key | Percent | Rows | Sample values |
|------|-----|--------|--------------------------------------------------------|
| `all` | 0.20% | 12,805 | `['7189910', '9047964', '9424969', '7562307', '9714069']` |


    #standardSQL
    SELECT
      COUNT(*) AS cnt,
      COUNT(second.second_column) AS second_cnt,
      ARRAY_AGG(first.id IGNORE NULLS ORDER BY RAND() LIMIT 5) AS sample_value
    FROM `patents-public-data.patentsview.patent`AS first
    LEFT JOIN (
      SELECT patent_id AS second_column, COUNT(*) AS cnt
      FROM `patents-public-data.patentsview.botanic`
      GROUP BY 1
    ) AS second ON first.id = second.second_column


joins to `patents-public-data:patentsview.brf_sum_text::patent_id` on **PatentsView patent_id** (91.32%, 5,813,766 rows)

| Key | Percent | Rows | Sample values |
|------|-----|--------|--------------------------------------------------------|
| `all` | 91.32% | 5,813,766 | `['D428016', '5870040', '9526498', '6497505', '4946762']` |


    #standardSQL
    SELECT
      COUNT(*) AS cnt,
      COUNT(second.second_column) AS second_cnt,
      ARRAY_AGG(first.id IGNORE NULLS ORDER BY RAND() LIMIT 5) AS sample_value
    FROM `patents-public-data.patentsview.patent`AS first
    LEFT JOIN (
      SELECT patent_id AS second_column, COUNT(*) AS cnt
      FROM `patents-public-data.patentsview.brf_sum_text`
      GROUP BY 1
    ) AS second ON first.id = second.second_column


joins to `patents-public-data:patentsview.claim::patent_id` on **PatentsView patent_id** (99.99%, 6,366,040 rows)

| Key | Percent | Rows | Sample values |
|------|-----|--------|--------------------------------------------------------|
| `all` | 99.99% | 6,366,040 | `['4973696', '6611420', '5945156', '5553930', '5553743']` |


    #standardSQL
    SELECT
      COUNT(*) AS cnt,
      COUNT(second.second_column) AS second_cnt,
      ARRAY_AGG(first.id IGNORE NULLS ORDER BY RAND() LIMIT 5) AS sample_value
    FROM `patents-public-data.patentsview.patent`AS first
    LEFT JOIN (
      SELECT patent_id AS second_column, COUNT(*) AS cnt
      FROM `patents-public-data.patentsview.claim`
      GROUP BY 1
    ) AS second ON first.id = second.second_column


joins to `patents-public-data:patentsview.cpc_current::patent_id` on **PatentsView patent_id** (90.34%, 5,751,595 rows)

| Key | Percent | Rows | Sample values |
|------|-----|--------|--------------------------------------------------------|
| `all` | 90.34% | 5,751,595 | `['6424471', 'D420655', '5513414', '9236147', '6975636']` |


    #standardSQL
    SELECT
      COUNT(*) AS cnt,
      COUNT(second.second_column) AS second_cnt,
      ARRAY_AGG(first.id IGNORE NULLS ORDER BY RAND() LIMIT 5) AS sample_value
    FROM `patents-public-data.patentsview.patent`AS first
    LEFT JOIN (
      SELECT patent_id AS second_column, COUNT(*) AS cnt
      FROM `patents-public-data.patentsview.cpc_current`
      GROUP BY 1
    ) AS second ON first.id = second.second_column


joins to `patents-public-data:patentsview.draw_desc_text::patent_id` on **PatentsView patent_id** (88.78%, 5,652,621 rows)

| Key | Percent | Rows | Sample values |
|------|-----|--------|--------------------------------------------------------|
| `all` | 88.78% | 5,652,621 | `['5727683', '7620486', '7767470', '8097018', '7318291']` |


    #standardSQL
    SELECT
      COUNT(*) AS cnt,
      COUNT(second.second_column) AS second_cnt,
      ARRAY_AGG(first.id IGNORE NULLS ORDER BY RAND() LIMIT 5) AS sample_value
    FROM `patents-public-data.patentsview.patent`AS first
    LEFT JOIN (
      SELECT patent_id AS second_column, COUNT(*) AS cnt
      FROM `patents-public-data.patentsview.draw_desc_text`
      GROUP BY 1
    ) AS second ON first.id = second.second_column


joins to `patents-public-data:patentsview.figures::patent_id` on **PatentsView patent_id** (92.29%, 5,875,847 rows)

| Key | Percent | Rows | Sample values |
|------|-----|--------|--------------------------------------------------------|
| `all` | 92.29% | 5,875,847 | `['5987461', '6418436', '7961677', '9225590', '4902534']` |


    #standardSQL
    SELECT
      COUNT(*) AS cnt,
      COUNT(second.second_column) AS second_cnt,
      ARRAY_AGG(first.id IGNORE NULLS ORDER BY RAND() LIMIT 5) AS sample_value
    FROM `patents-public-data.patentsview.patent`AS first
    LEFT JOIN (
      SELECT patent_id AS second_column, COUNT(*) AS cnt
      FROM `patents-public-data.patentsview.figures`
      GROUP BY 1
    ) AS second ON first.id = second.second_column


joins to `patents-public-data:patentsview.foreign_priority::patent_id` on **PatentsView patent_id** (37.32%, 2,376,338 rows)

| Key | Percent | Rows | Sample values |
|------|-----|--------|--------------------------------------------------------|
| `all` | 37.32% | 2,376,338 | `['5471183', '7647187', '6013167', '7964514', '4123527']` |


    #standardSQL
    SELECT
      COUNT(*) AS cnt,
      COUNT(second.second_column) AS second_cnt,
      ARRAY_AGG(first.id IGNORE NULLS ORDER BY RAND() LIMIT 5) AS sample_value
    FROM `patents-public-data.patentsview.patent`AS first
    LEFT JOIN (
      SELECT patent_id AS second_column, COUNT(*) AS cnt
      FROM `patents-public-data.patentsview.foreign_priority`
      GROUP BY 1
    ) AS second ON first.id = second.second_column


joins to `patents-public-data:patentsview.foreigncitation::patent_id` on **PatentsView patent_id** (52.53%, 3,344,703 rows)

| Key | Percent | Rows | Sample values |
|------|-----|--------|--------------------------------------------------------|
| `all` | 52.53% | 3,344,703 | `['5322551', '7576014', '4462916', '4883340', '7192651']` |


    #standardSQL
    SELECT
      COUNT(*) AS cnt,
      COUNT(second.second_column) AS second_cnt,
      ARRAY_AGG(first.id IGNORE NULLS ORDER BY RAND() LIMIT 5) AS sample_value
    FROM `patents-public-data.patentsview.patent`AS first
    LEFT JOIN (
      SELECT patent_id AS second_column, COUNT(*) AS cnt
      FROM `patents-public-data.patentsview.foreigncitation`
      GROUP BY 1
    ) AS second ON first.id = second.second_column


joins to `patents-public-data:patentsview.government_interest::patent_id` on **PatentsView patent_id** (1.99%, 126,528 rows)

| Key | Percent | Rows | Sample values |
|------|-----|--------|--------------------------------------------------------|
| `all` | 1.99% | 126,528 | `['6850174', '8239146', '4545066', '6516251', '7119074']` |


    #standardSQL
    SELECT
      COUNT(*) AS cnt,
      COUNT(second.second_column) AS second_cnt,
      ARRAY_AGG(first.id IGNORE NULLS ORDER BY RAND() LIMIT 5) AS sample_value
    FROM `patents-public-data.patentsview.patent`AS first
    LEFT JOIN (
      SELECT patent_id AS second_column, COUNT(*) AS cnt
      FROM `patents-public-data.patentsview.government_interest`
      GROUP BY 1
    ) AS second ON first.id = second.second_column


joins to `patents-public-data:patentsview.ipcr::patent_id` on **PatentsView patent_id** (91.44%, 5,821,568 rows)

| Key | Percent | Rows | Sample values |
|------|-----|--------|--------------------------------------------------------|
| `all` | 91.44% | 5,821,568 | `['5818247', '4887472', '5173934', 'D668385', '6476745']` |


    #standardSQL
    SELECT
      COUNT(*) AS cnt,
      COUNT(second.second_column) AS second_cnt,
      ARRAY_AGG(first.id IGNORE NULLS ORDER BY RAND() LIMIT 5) AS sample_value
    FROM `patents-public-data.patentsview.patent`AS first
    LEFT JOIN (
      SELECT patent_id AS second_column, COUNT(*) AS cnt
      FROM `patents-public-data.patentsview.ipcr`
      GROUP BY 1
    ) AS second ON first.id = second.second_column


joins to `patents-public-data:patentsview.match::patent_id` on **PatentsView patent_id** (99.86%, 6,357,947 rows)

| Key | Percent | Rows | Sample values |
|------|-----|--------|--------------------------------------------------------|
| `all` | 99.86% | 6,357,947 | `['4724676', '8573865', '7802353', '4471005', '7606088']` |


    #standardSQL
    SELECT
      COUNT(*) AS cnt,
      COUNT(second.second_column) AS second_cnt,
      ARRAY_AGG(first.id IGNORE NULLS ORDER BY RAND() LIMIT 5) AS sample_value
    FROM `patents-public-data.patentsview.patent`AS first
    LEFT JOIN (
      SELECT patent_id AS second_column, COUNT(*) AS cnt
      FROM `patents-public-data.patentsview.match`
      GROUP BY 1
    ) AS second ON first.id = second.second_column


joins to `patents-public-data:patentsview.nber::patent_id` on **PatentsView patent_id** (80.20%, 5,105,937 rows)

| Key | Percent | Rows | Sample values |
|------|-----|--------|--------------------------------------------------------|
| `all` | 80.20% | 5,105,937 | `['8468189', 'D557528', '8653305', '6817858', '5909399']` |


    #standardSQL
    SELECT
      COUNT(*) AS cnt,
      COUNT(second.second_column) AS second_cnt,
      ARRAY_AGG(first.id IGNORE NULLS ORDER BY RAND() LIMIT 5) AS sample_value
    FROM `patents-public-data.patentsview.patent`AS first
    LEFT JOIN (
      SELECT patent_id AS second_column, COUNT(*) AS cnt
      FROM `patents-public-data.patentsview.nber`
      GROUP BY 1
    ) AS second ON first.id = second.second_column


joins to `patents-public-data:patentsview.non_inventor_applicant::patent_id` on **PatentsView patent_id** (9.41%, 598,855 rows)

| Key | Percent | Rows | Sample values |
|------|-----|--------|--------------------------------------------------------|
| `all` | 9.41% | 598,855 | `['7144822', '9184876', '8628391', '6154148', '5091813']` |


    #standardSQL
    SELECT
      COUNT(*) AS cnt,
      COUNT(second.second_column) AS second_cnt,
      ARRAY_AGG(first.id IGNORE NULLS ORDER BY RAND() LIMIT 5) AS sample_value
    FROM `patents-public-data.patentsview.patent`AS first
    LEFT JOIN (
      SELECT patent_id AS second_column, COUNT(*) AS cnt
      FROM `patents-public-data.patentsview.non_inventor_applicant`
      GROUP BY 1
    ) AS second ON first.id = second.second_column


joins to `patents-public-data:patentsview.otherreference::patent_id` on **PatentsView patent_id** (42.57%, 2,710,182 rows)

| Key | Percent | Rows | Sample values |
|------|-----|--------|--------------------------------------------------------|
| `all` | 42.57% | 2,710,182 | `['7963788', '5797506', '9459069', '7639471', '5492141']` |


    #standardSQL
    SELECT
      COUNT(*) AS cnt,
      COUNT(second.second_column) AS second_cnt,
      ARRAY_AGG(first.id IGNORE NULLS ORDER BY RAND() LIMIT 5) AS sample_value
    FROM `patents-public-data.patentsview.patent`AS first
    LEFT JOIN (
      SELECT patent_id AS second_column, COUNT(*) AS cnt
      FROM `patents-public-data.patentsview.otherreference`
      GROUP BY 1
    ) AS second ON first.id = second.second_column


joins to `patents-public-data:patentsview.patent_assignee::patent_id` on **PatentsView patent_id** (85.62%, 5,451,090 rows)

| Key | Percent | Rows | Sample values |
|------|-----|--------|--------------------------------------------------------|
| `all` | 85.62% | 5,451,090 | `['7061671', '6528888', '6311712', 'D566453', '7451136']` |


    #standardSQL
    SELECT
      COUNT(*) AS cnt,
      COUNT(second.second_column) AS second_cnt,
      ARRAY_AGG(first.id IGNORE NULLS ORDER BY RAND() LIMIT 5) AS sample_value
    FROM `patents-public-data.patentsview.patent`AS first
    LEFT JOIN (
      SELECT patent_id AS second_column, COUNT(*) AS cnt
      FROM `patents-public-data.patentsview.patent_assignee`
      GROUP BY 1
    ) AS second ON first.id = second.second_column


joins to `patents-public-data:patentsview.patent_contractawardnumber::patent_id` on **PatentsView patent_id** (1.55%, 98,812 rows)

| Key | Percent | Rows | Sample values |
|------|-----|--------|--------------------------------------------------------|
| `all` | 1.55% | 98,812 | `['5347768', 'RE37037', '6426698', 'D763717', '8543520']` |


    #standardSQL
    SELECT
      COUNT(*) AS cnt,
      COUNT(second.second_column) AS second_cnt,
      ARRAY_AGG(first.id IGNORE NULLS ORDER BY RAND() LIMIT 5) AS sample_value
    FROM `patents-public-data.patentsview.patent`AS first
    LEFT JOIN (
      SELECT patent_id AS second_column, COUNT(*) AS cnt
      FROM `patents-public-data.patentsview.patent_contractawardnumber`
      GROUP BY 1
    ) AS second ON first.id = second.second_column


joins to `patents-public-data:patentsview.patent_govintorg::patent_id` on **PatentsView patent_id** (1.91%, 121,410 rows)

| Key | Percent | Rows | Sample values |
|------|-----|--------|--------------------------------------------------------|
| `all` | 1.91% | 121,410 | `['6604027', '8080026', '7000451', 'D287301', '4353679']` |


    #standardSQL
    SELECT
      COUNT(*) AS cnt,
      COUNT(second.second_column) AS second_cnt,
      ARRAY_AGG(first.id IGNORE NULLS ORDER BY RAND() LIMIT 5) AS sample_value
    FROM `patents-public-data.patentsview.patent`AS first
    LEFT JOIN (
      SELECT patent_id AS second_column, COUNT(*) AS cnt
      FROM `patents-public-data.patentsview.patent_govintorg`
      GROUP BY 1
    ) AS second ON first.id = second.second_column


joins to `patents-public-data:patentsview.patent_inventor::patent_id` on **PatentsView patent_id** (99.99%, 6,365,851 rows)

| Key | Percent | Rows | Sample values |
|------|-----|--------|--------------------------------------------------------|
| `all` | 99.99% | 6,365,851 | `['5464529', '6222187', '7883369', '5380543', '8046312']` |


    #standardSQL
    SELECT
      COUNT(*) AS cnt,
      COUNT(second.second_column) AS second_cnt,
      ARRAY_AGG(first.id IGNORE NULLS ORDER BY RAND() LIMIT 5) AS sample_value
    FROM `patents-public-data.patentsview.patent`AS first
    LEFT JOIN (
      SELECT patent_id AS second_column, COUNT(*) AS cnt
      FROM `patents-public-data.patentsview.patent_inventor`
      GROUP BY 1
    ) AS second ON first.id = second.second_column


joins to `patents-public-data:patentsview.patent_lawyer::patent_id` on **PatentsView patent_id** (92.44%, 5,885,331 rows)

| Key | Percent | Rows | Sample values |
|------|-----|--------|--------------------------------------------------------|
| `all` | 92.44% | 5,885,331 | `['8233160', '6843852', 'D255130', '9240628', '6424011']` |


    #standardSQL
    SELECT
      COUNT(*) AS cnt,
      COUNT(second.second_column) AS second_cnt,
      ARRAY_AGG(first.id IGNORE NULLS ORDER BY RAND() LIMIT 5) AS sample_value
    FROM `patents-public-data.patentsview.patent`AS first
    LEFT JOIN (
      SELECT patent_id AS second_column, COUNT(*) AS cnt
      FROM `patents-public-data.patentsview.patent_lawyer`
      GROUP BY 1
    ) AS second ON first.id = second.second_column


joins to `patents-public-data:patentsview.pct_data::patent_id` on **PatentsView patent_id** (9.00%, 572,891 rows)

| Key | Percent | Rows | Sample values |
|------|-----|--------|--------------------------------------------------------|
| `all` | 9.00% | 572,891 | `['6858149', '5992684', '7385475', '4581375', '5279424']` |


    #standardSQL
    SELECT
      COUNT(*) AS cnt,
      COUNT(second.second_column) AS second_cnt,
      ARRAY_AGG(first.id IGNORE NULLS ORDER BY RAND() LIMIT 5) AS sample_value
    FROM `patents-public-data.patentsview.patent`AS first
    LEFT JOIN (
      SELECT patent_id AS second_column, COUNT(*) AS cnt
      FROM `patents-public-data.patentsview.pct_data`
      GROUP BY 1
    ) AS second ON first.id = second.second_column


joins to `patents-public-data:patentsview.rawassignee::patent_id` on **PatentsView patent_id** (85.62%, 5,451,096 rows)

| Key | Percent | Rows | Sample values |
|------|-----|--------|--------------------------------------------------------|
| `all` | 85.62% | 5,451,096 | `['8360550', '6502080', '7205888', '8617398', '7301916']` |


    #standardSQL
    SELECT
      COUNT(*) AS cnt,
      COUNT(second.second_column) AS second_cnt,
      ARRAY_AGG(first.id IGNORE NULLS ORDER BY RAND() LIMIT 5) AS sample_value
    FROM `patents-public-data.patentsview.patent`AS first
    LEFT JOIN (
      SELECT patent_id AS second_column, COUNT(*) AS cnt
      FROM `patents-public-data.patentsview.rawassignee`
      GROUP BY 1
    ) AS second ON first.id = second.second_column


joins to `patents-public-data:patentsview.rawexaminer::patent_id` on **PatentsView patent_id** (99.98%, 6,365,105 rows)

| Key | Percent | Rows | Sample values |
|------|-----|--------|--------------------------------------------------------|
| `all` | 99.98% | 6,365,105 | `['5785921', '6249692', '9289185', '4906387', '4606896']` |


    #standardSQL
    SELECT
      COUNT(*) AS cnt,
      COUNT(second.second_column) AS second_cnt,
      ARRAY_AGG(first.id IGNORE NULLS ORDER BY RAND() LIMIT 5) AS sample_value
    FROM `patents-public-data.patentsview.patent`AS first
    LEFT JOIN (
      SELECT patent_id AS second_column, COUNT(*) AS cnt
      FROM `patents-public-data.patentsview.rawexaminer`
      GROUP BY 1
    ) AS second ON first.id = second.second_column


joins to `patents-public-data:patentsview.rawinventor::patent_id` on **PatentsView patent_id** (99.99%, 6,365,851 rows)

| Key | Percent | Rows | Sample values |
|------|-----|--------|--------------------------------------------------------|
| `all` | 99.99% | 6,365,851 | `['8567100', '7171401', '4437177', '4442025', '5588363']` |


    #standardSQL
    SELECT
      COUNT(*) AS cnt,
      COUNT(second.second_column) AS second_cnt,
      ARRAY_AGG(first.id IGNORE NULLS ORDER BY RAND() LIMIT 5) AS sample_value
    FROM `patents-public-data.patentsview.patent`AS first
    LEFT JOIN (
      SELECT patent_id AS second_column, COUNT(*) AS cnt
      FROM `patents-public-data.patentsview.rawinventor`
      GROUP BY 1
    ) AS second ON first.id = second.second_column


joins to `patents-public-data:patentsview.rawlawyer::patent_id` on **PatentsView patent_id** (92.44%, 5,885,426 rows)

| Key | Percent | Rows | Sample values |
|------|-----|--------|--------------------------------------------------------|
| `all` | 92.44% | 5,885,426 | `['6848512', '3941847', '4307190', '6584816', '4162075']` |


    #standardSQL
    SELECT
      COUNT(*) AS cnt,
      COUNT(second.second_column) AS second_cnt,
      ARRAY_AGG(first.id IGNORE NULLS ORDER BY RAND() LIMIT 5) AS sample_value
    FROM `patents-public-data.patentsview.patent`AS first
    LEFT JOIN (
      SELECT patent_id AS second_column, COUNT(*) AS cnt
      FROM `patents-public-data.patentsview.rawlawyer`
      GROUP BY 1
    ) AS second ON first.id = second.second_column


joins to `patents-public-data:patentsview.rel_app_text::patent_id` on **PatentsView patent_id** (22.59%, 1,438,215 rows)

| Key | Percent | Rows | Sample values |
|------|-----|--------|--------------------------------------------------------|
| `all` | 22.59% | 1,438,215 | `['7713406', '4765102', '9613321', '7722145', '9668527']` |


    #standardSQL
    SELECT
      COUNT(*) AS cnt,
      COUNT(second.second_column) AS second_cnt,
      ARRAY_AGG(first.id IGNORE NULLS ORDER BY RAND() LIMIT 5) AS sample_value
    FROM `patents-public-data.patentsview.patent`AS first
    LEFT JOIN (
      SELECT patent_id AS second_column, COUNT(*) AS cnt
      FROM `patents-public-data.patentsview.rel_app_text`
      GROUP BY 1
    ) AS second ON first.id = second.second_column


joins to `patents-public-data:patentsview.us_term_of_grant::patent_id` on **PatentsView patent_id** (45.91%, 2,923,111 rows)

| Key | Percent | Rows | Sample values |
|------|-----|--------|--------------------------------------------------------|
| `all` | 45.91% | 2,923,111 | `['8325895', '6552631', '7342668', '4196188', '6364983']` |


    #standardSQL
    SELECT
      COUNT(*) AS cnt,
      COUNT(second.second_column) AS second_cnt,
      ARRAY_AGG(first.id IGNORE NULLS ORDER BY RAND() LIMIT 5) AS sample_value
    FROM `patents-public-data.patentsview.patent`AS first
    LEFT JOIN (
      SELECT patent_id AS second_column, COUNT(*) AS cnt
      FROM `patents-public-data.patentsview.us_term_of_grant`
      GROUP BY 1
    ) AS second ON first.id = second.second_column


joins to `patents-public-data:patentsview.usapplicationcitation::patent_id` on **PatentsView patent_id** (36.83%, 2,344,704 rows)

| Key | Percent | Rows | Sample values |
|------|-----|--------|--------------------------------------------------------|
| `all` | 36.83% | 2,344,704 | `['6973241', '7300360', '9687673', '8913613', '8666954']` |


    #standardSQL
    SELECT
      COUNT(*) AS cnt,
      COUNT(second.second_column) AS second_cnt,
      ARRAY_AGG(first.id IGNORE NULLS ORDER BY RAND() LIMIT 5) AS sample_value
    FROM `patents-public-data.patentsview.patent`AS first
    LEFT JOIN (
      SELECT patent_id AS second_column, COUNT(*) AS cnt
      FROM `patents-public-data.patentsview.usapplicationcitation`
      GROUP BY 1
    ) AS second ON first.id = second.second_column


joins to `patents-public-data:patentsview.uspatentcitation::patent_id` on **PatentsView patent_id** (95.36%, 6,071,414 rows)

| Key | Percent | Rows | Sample values |
|------|-----|--------|--------------------------------------------------------|
| `all` | 95.36% | 6,071,414 | `['6725847', '4307341', '6358138', '6852080', '5860497']` |


    #standardSQL
    SELECT
      COUNT(*) AS cnt,
      COUNT(second.second_column) AS second_cnt,
      ARRAY_AGG(first.id IGNORE NULLS ORDER BY RAND() LIMIT 5) AS sample_value
    FROM `patents-public-data.patentsview.patent`AS first
    LEFT JOIN (
      SELECT patent_id AS second_column, COUNT(*) AS cnt
      FROM `patents-public-data.patentsview.uspatentcitation`
      GROUP BY 1
    ) AS second ON first.id = second.second_column


joins to `patents-public-data:patentsview.uspc::patent_id` on **PatentsView patent_id** (79.24%, 5,044,804 rows)

| Key | Percent | Rows | Sample values |
|------|-----|--------|--------------------------------------------------------|
| `all` | 79.24% | 5,044,804 | `['7533547', '4607007', '5516759', '6017979', '7748590']` |


    #standardSQL
    SELECT
      COUNT(*) AS cnt,
      COUNT(second.second_column) AS second_cnt,
      ARRAY_AGG(first.id IGNORE NULLS ORDER BY RAND() LIMIT 5) AS sample_value
    FROM `patents-public-data.patentsview.patent`AS first
    LEFT JOIN (
      SELECT patent_id AS second_column, COUNT(*) AS cnt
      FROM `patents-public-data.patentsview.uspc`
      GROUP BY 1
    ) AS second ON first.id = second.second_column


joins to `patents-public-data:patentsview.uspc_current::patent_id` on **PatentsView patent_id** (99.29%, 6,321,292 rows)

| Key | Percent | Rows | Sample values |
|------|-----|--------|--------------------------------------------------------|
| `all` | 99.29% | 6,321,292 | `['7484870', '6583447', '6710890', '6648713', '6791448']` |


    #standardSQL
    SELECT
      COUNT(*) AS cnt,
      COUNT(second.second_column) AS second_cnt,
      ARRAY_AGG(first.id IGNORE NULLS ORDER BY RAND() LIMIT 5) AS sample_value
    FROM `patents-public-data.patentsview.patent`AS first
    LEFT JOIN (
      SELECT patent_id AS second_column, COUNT(*) AS cnt
      FROM `patents-public-data.patentsview.uspc_current`
      GROUP BY 1
    ) AS second ON first.id = second.second_column


joins to `patents-public-data:patentsview.usreldoc::patent_id` on **PatentsView patent_id** (47.85%, 3,046,372 rows)

| Key | Percent | Rows | Sample values |
|------|-----|--------|--------------------------------------------------------|
| `all` | 47.85% | 3,046,372 | `['D335588', '7909661', '4324304', '8933972', '4232106']` |


    #standardSQL
    SELECT
      COUNT(*) AS cnt,
      COUNT(second.second_column) AS second_cnt,
      ARRAY_AGG(first.id IGNORE NULLS ORDER BY RAND() LIMIT 5) AS sample_value
    FROM `patents-public-data.patentsview.patent`AS first
    LEFT JOIN (
      SELECT patent_id AS second_column, COUNT(*) AS cnt
      FROM `patents-public-data.patentsview.usreldoc`
      GROUP BY 1
    ) AS second ON first.id = second.second_column


joins to `patents-public-data:patentsview.wipo::patent_id` on **PatentsView patent_id** (99.26%, 6,319,470 rows)

| Key | Percent | Rows | Sample values |
|------|-----|--------|--------------------------------------------------------|
| `all` | 99.26% | 6,319,470 | `['9455301', '5347761', 'D664330', '7537098', '5953756']` |


    #standardSQL
    SELECT
      COUNT(*) AS cnt,
      COUNT(second.second_column) AS second_cnt,
      ARRAY_AGG(first.id IGNORE NULLS ORDER BY RAND() LIMIT 5) AS sample_value
    FROM `patents-public-data.patentsview.patent`AS first
    LEFT JOIN (
      SELECT patent_id AS second_column, COUNT(*) AS cnt
      FROM `patents-public-data.patentsview.wipo`
      GROUP BY 1
    ) AS second ON first.id = second.second_column



joins from `patents-public-data:patentsview.application::patent_id` on **PatentsView patent_id** (100.00%, 6,366,664 rows)

joins from `patents-public-data:patentsview.botanic::patent_id` on **PatentsView patent_id** (100.00%, 12,805 rows)

joins from `patents-public-data:patentsview.brf_sum_text::patent_id` on **PatentsView patent_id** (100.00%, 5,813,766 rows)

joins from `patents-public-data:patentsview.claim::patent_id` on **PatentsView patent_id** (100.00%, 89,944,541 rows)

joins from `patents-public-data:patentsview.cpc_current::patent_id` on **PatentsView patent_id** (100.00%, 32,874,742 rows)

joins from `patents-public-data:patentsview.draw_desc_text::patent_id` on **PatentsView patent_id** (100.00%, 61,307,429 rows)

joins from `patents-public-data:patentsview.figures::patent_id` on **PatentsView patent_id** (100.00%, 5,875,847 rows)

joins from `patents-public-data:patentsview.foreign_priority::patent_id` on **PatentsView patent_id** (100.00%, 2,992,770 rows)

joins from `patents-public-data:patentsview.foreigncitation::patent_id` on **PatentsView patent_id** (100.00%, 22,020,427 rows)

joins from `patents-public-data:patentsview.government_interest::patent_id` on **PatentsView patent_id** (99.34%, 126,528 rows)

joins from `patents-public-data:patentsview.ipcr::patent_id` on **PatentsView patent_id** (100.00%, 11,557,735 rows)

joins from `patents-public-data:patentsview.match::patent_id` on **PatentsView patent_id** (100.00%, 6,357,947 rows)

joins from `patents-public-data:patentsview.nber::patent_id` on **PatentsView patent_id** (100.00%, 5,105,937 rows)

joins from `patents-public-data:patentsview.non_inventor_applicant::patent_id` on **PatentsView patent_id** (100.00%, 598,855 rows)

joins from `patents-public-data:patentsview.otherreference::patent_id` on **PatentsView patent_id** (100.00%, 31,414,354 rows)

joins from `patents-public-data:patentsview.patent_assignee::patent_id` on **PatentsView patent_id** (100.00%, 5,629,558 rows)

joins from `patents-public-data:patentsview.patent_contractawardnumber::patent_id` on **PatentsView patent_id** (99.79%, 138,703 rows)

joins from `patents-public-data:patentsview.patent_govintorg::patent_id` on **PatentsView patent_id** (99.41%, 142,889 rows)

joins from `patents-public-data:patentsview.patent_inventor::patent_id` on **PatentsView patent_id** (100.00%, 14,953,518 rows)

joins from `patents-public-data:patentsview.patent_lawyer::patent_id` on **PatentsView patent_id** (100.00%, 7,226,556 rows)

joins from `patents-public-data:patentsview.pct_data::patent_id` on **PatentsView patent_id** (100.00%, 1,100,050 rows)

joins from `patents-public-data:patentsview.rawassignee::patent_id` on **PatentsView patent_id** (100.00%, 5,629,565 rows)

joins from `patents-public-data:patentsview.rawexaminer::patent_id` on **PatentsView patent_id** (100.00%, 8,727,147 rows)

joins from `patents-public-data:patentsview.rawinventor::patent_id` on **PatentsView patent_id** (100.00%, 14,959,652 rows)

joins from `patents-public-data:patentsview.rawlawyer::patent_id` on **PatentsView patent_id** (100.00%, 7,226,654 rows)

joins from `patents-public-data:patentsview.rel_app_text::patent_id` on **PatentsView patent_id** (100.00%, 1,438,215 rows)

joins from `patents-public-data:patentsview.us_term_of_grant::patent_id` on **PatentsView patent_id** (100.00%, 2,923,111 rows)

joins from `patents-public-data:patentsview.usapplicationcitation::patent_id` on **PatentsView patent_id** (100.00%, 25,343,373 rows)

joins from `patents-public-data:patentsview.uspatentcitation::patent_id` on **PatentsView patent_id** (100.00%, 89,122,312 rows)

joins from `patents-public-data:patentsview.uspc::patent_id` on **PatentsView patent_id** (100.00%, 18,024,187 rows)

joins from `patents-public-data:patentsview.uspc_current::patent_id` on **PatentsView patent_id** (100.00%, 22,576,756 rows)

joins from `patents-public-data:patentsview.usreldoc::patent_id` on **PatentsView patent_id** (100.00%, 8,022,497 rows)

joins from `patents-public-data:patentsview.wipo::patent_id` on **PatentsView patent_id** (100.00%, 8,474,756 rows)
























*****
## patents-public-data:patentsview.patent_201708


Old table version `201708`, schema skipped.





*****
## patents-public-data:patentsview.patent_assignee



> PatentsView Data is a database that longitudinally links inventors, their organizations, locations, and overall patenting activity. The dataset uses data derived from USPTO bulk data files.
> 
> “PatentsView” by the USPTO, US Department of Agriculture (USDA), the Center for the Science of Science and Innovation Policy, New York University, the University of California at Berkeley, Twin Arch Technologies, and Periscopic, used under CC BY 4.0.





| Stat | Value |
|----------|----------|
| Last updated | 2017-10-13 |
| Rows | 5,629,558 |
| Size | 242.1 MB |

### Schema
[View in BigQuery](https://bigquery.cloud.google.com/table/patents-public-data:patentsview.patent_assignee)

* `patent_id` STRING   joins on **PatentsView patent_id**

* `assignee_id` STRING  



### Join columns


#### patent_id

joins to `patents-public-data:patentsview.patent::id` on **PatentsView patent_id** (100.00%, 5,629,558 rows)

| Key | Percent | Rows | Sample values |
|------|-----|--------|--------------------------------------------------------|
| `all` | 100.00% | 5,629,558 | `['6540048', '4750060', 'D498497', '6998660', '4688914']` |


    #standardSQL
    SELECT
      COUNT(*) AS cnt,
      COUNT(second.second_column) AS second_cnt,
      ARRAY_AGG(first.patent_id IGNORE NULLS ORDER BY RAND() LIMIT 5) AS sample_value
    FROM `patents-public-data.patentsview.patent_assignee`AS first
    LEFT JOIN (
      SELECT id AS second_column, COUNT(*) AS cnt
      FROM `patents-public-data.patentsview.patent`
      GROUP BY 1
    ) AS second ON first.patent_id = second.second_column



joins from `patents-public-data:patentsview.patent::id` on **PatentsView patent_id** (85.62%, 5,451,090 rows)








*****
## patents-public-data:patentsview.patent_assignee_201708


Old table version `201708`, schema skipped.





*****
## patents-public-data:patentsview.patent_contractawardnumber



> PatentsView Data is a database that longitudinally links inventors, their organizations, locations, and overall patenting activity. The dataset uses data derived from USPTO bulk data files.
> 
> “PatentsView” by the USPTO, US Department of Agriculture (USDA), the Center for the Science of Science and Innovation Policy, New York University, the University of California at Berkeley, Twin Arch Technologies, and Periscopic, used under CC BY 4.0.





| Stat | Value |
|----------|----------|
| Last updated | 2017-10-13 |
| Rows | 138,988 |
| Size | 3.3 MB |

### Schema
[View in BigQuery](https://bigquery.cloud.google.com/table/patents-public-data:patentsview.patent_contractawardnumber)

* `patent_id` STRING   joins on **PatentsView patent_id**

* `contract_award_number` STRING  



### Join columns


#### patent_id

joins to `patents-public-data:patentsview.patent::id` on **PatentsView patent_id** (99.79%, 138,703 rows)

| Key | Percent | Rows | Sample values |
|------|-----|--------|--------------------------------------------------------|
| `all` | 99.79% | 138,703 | `['4682053', '8805316', '5721143', '6602693', '6316131']` |


    #standardSQL
    SELECT
      COUNT(*) AS cnt,
      COUNT(second.second_column) AS second_cnt,
      ARRAY_AGG(first.patent_id IGNORE NULLS ORDER BY RAND() LIMIT 5) AS sample_value
    FROM `patents-public-data.patentsview.patent_contractawardnumber`AS first
    LEFT JOIN (
      SELECT id AS second_column, COUNT(*) AS cnt
      FROM `patents-public-data.patentsview.patent`
      GROUP BY 1
    ) AS second ON first.patent_id = second.second_column



joins from `patents-public-data:patentsview.patent::id` on **PatentsView patent_id** (1.55%, 98,812 rows)








*****
## patents-public-data:patentsview.patent_contractawardnumber_201708


Old table version `201708`, schema skipped.





*****
## patents-public-data:patentsview.patent_govintorg



> PatentsView Data is a database that longitudinally links inventors, their organizations, locations, and overall patenting activity. The dataset uses data derived from USPTO bulk data files.
> 
> “PatentsView” by the USPTO, US Department of Agriculture (USDA), the Center for the Science of Science and Innovation Policy, New York University, the University of California at Berkeley, Twin Arch Technologies, and Periscopic, used under CC BY 4.0.





| Stat | Value |
|----------|----------|
| Last updated | 2017-10-13 |
| Rows | 143,743 |
| Size | 1.9 MB |

### Schema
[View in BigQuery](https://bigquery.cloud.google.com/table/patents-public-data:patentsview.patent_govintorg)

* `patent_id` STRING   joins on **PatentsView patent_id**

* `organization_id` STRING  



### Join columns


#### patent_id

joins to `patents-public-data:patentsview.patent::id` on **PatentsView patent_id** (99.41%, 142,889 rows)

| Key | Percent | Rows | Sample values |
|------|-----|--------|--------------------------------------------------------|
| `all` | 99.41% | 142,889 | `['5591439', '7842144', '9577731', '5576147', '6448045']` |


    #standardSQL
    SELECT
      COUNT(*) AS cnt,
      COUNT(second.second_column) AS second_cnt,
      ARRAY_AGG(first.patent_id IGNORE NULLS ORDER BY RAND() LIMIT 5) AS sample_value
    FROM `patents-public-data.patentsview.patent_govintorg`AS first
    LEFT JOIN (
      SELECT id AS second_column, COUNT(*) AS cnt
      FROM `patents-public-data.patentsview.patent`
      GROUP BY 1
    ) AS second ON first.patent_id = second.second_column



joins from `patents-public-data:patentsview.patent::id` on **PatentsView patent_id** (1.91%, 121,410 rows)








*****
## patents-public-data:patentsview.patent_govintorg_201708


Old table version `201708`, schema skipped.





*****
## patents-public-data:patentsview.patent_inventor



> PatentsView Data is a database that longitudinally links inventors, their organizations, locations, and overall patenting activity. The dataset uses data derived from USPTO bulk data files.
> 
> “PatentsView” by the USPTO, US Department of Agriculture (USDA), the Center for the Science of Science and Innovation Policy, New York University, the University of California at Berkeley, Twin Arch Technologies, and Periscopic, used under CC BY 4.0.





| Stat | Value |
|----------|----------|
| Last updated | 2017-10-13 |
| Rows | 14,953,518 |
| Size | 299.1 MB |

### Schema
[View in BigQuery](https://bigquery.cloud.google.com/table/patents-public-data:patentsview.patent_inventor)

* `patent_id` STRING   joins on **PatentsView patent_id**

* `inventor_id` STRING  



### Join columns


#### patent_id

joins to `patents-public-data:patentsview.patent::id` on **PatentsView patent_id** (100.00%, 14,953,518 rows)

| Key | Percent | Rows | Sample values |
|------|-----|--------|--------------------------------------------------------|
| `all` | 100.00% | 14,953,518 | `['7721596', '9478958', '6861563', '7285876', '4952986']` |


    #standardSQL
    SELECT
      COUNT(*) AS cnt,
      COUNT(second.second_column) AS second_cnt,
      ARRAY_AGG(first.patent_id IGNORE NULLS ORDER BY RAND() LIMIT 5) AS sample_value
    FROM `patents-public-data.patentsview.patent_inventor`AS first
    LEFT JOIN (
      SELECT id AS second_column, COUNT(*) AS cnt
      FROM `patents-public-data.patentsview.patent`
      GROUP BY 1
    ) AS second ON first.patent_id = second.second_column



joins from `patents-public-data:patentsview.patent::id` on **PatentsView patent_id** (99.99%, 6,365,851 rows)








*****
## patents-public-data:patentsview.patent_inventor_201708


Old table version `201708`, schema skipped.





*****
## patents-public-data:patentsview.patent_lawyer



> PatentsView Data is a database that longitudinally links inventors, their organizations, locations, and overall patenting activity. The dataset uses data derived from USPTO bulk data files.
> 
> “PatentsView” by the USPTO, US Department of Agriculture (USDA), the Center for the Science of Science and Innovation Policy, New York University, the University of California at Berkeley, Twin Arch Technologies, and Periscopic, used under CC BY 4.0.





| Stat | Value |
|----------|----------|
| Last updated | 2017-10-13 |
| Rows | 7,226,556 |
| Size | 310.7 MB |

### Schema
[View in BigQuery](https://bigquery.cloud.google.com/table/patents-public-data:patentsview.patent_lawyer)

* `patent_id` STRING   joins on **PatentsView patent_id**

* `lawyer_id` STRING  



### Join columns


#### patent_id

joins to `patents-public-data:patentsview.patent::id` on **PatentsView patent_id** (100.00%, 7,226,556 rows)

| Key | Percent | Rows | Sample values |
|------|-----|--------|--------------------------------------------------------|
| `all` | 100.00% | 7,226,556 | `['5494108', '9726821', '8399659', '4655491', '4558250']` |


    #standardSQL
    SELECT
      COUNT(*) AS cnt,
      COUNT(second.second_column) AS second_cnt,
      ARRAY_AGG(first.patent_id IGNORE NULLS ORDER BY RAND() LIMIT 5) AS sample_value
    FROM `patents-public-data.patentsview.patent_lawyer`AS first
    LEFT JOIN (
      SELECT id AS second_column, COUNT(*) AS cnt
      FROM `patents-public-data.patentsview.patent`
      GROUP BY 1
    ) AS second ON first.patent_id = second.second_column



joins from `patents-public-data:patentsview.patent::id` on **PatentsView patent_id** (92.44%, 5,885,331 rows)








*****
## patents-public-data:patentsview.patent_lawyer_201708


Old table version `201708`, schema skipped.





*****
## patents-public-data:patentsview.pct_data



> PatentsView Data is a database that longitudinally links inventors, their organizations, locations, and overall patenting activity. The dataset uses data derived from USPTO bulk data files.
> 
> “PatentsView” by the USPTO, US Department of Agriculture (USDA), the Center for the Science of Science and Innovation Policy, New York University, the University of California at Berkeley, Twin Arch Technologies, and Periscopic, used under CC BY 4.0.





| Stat | Value |
|----------|----------|
| Last updated | 2017-10-13 |
| Rows | 1,100,050 |
| Size | 101.9 MB |

### Schema
[View in BigQuery](https://bigquery.cloud.google.com/table/patents-public-data:patentsview.pct_data)

* `uuid` STRING  

* `patent_id` STRING   joins on **PatentsView patent_id**

* `rel_id` STRING  

* `date` STRING  

* `f371_date` STRING  

* `country` STRING  

* `kind` STRING  

* `doc_type` STRING  

* `f102_date` STRING  



### Join columns




#### patent_id

joins to `patents-public-data:patentsview.patent::id` on **PatentsView patent_id** (100.00%, 1,100,050 rows)

| Key | Percent | Rows | Sample values |
|------|-----|--------|--------------------------------------------------------|
| `all` | 100.00% | 1,100,050 | `['7388010', '7731935', '9541681', '9068679', '8252430']` |


    #standardSQL
    SELECT
      COUNT(*) AS cnt,
      COUNT(second.second_column) AS second_cnt,
      ARRAY_AGG(first.patent_id IGNORE NULLS ORDER BY RAND() LIMIT 5) AS sample_value
    FROM `patents-public-data.patentsview.pct_data`AS first
    LEFT JOIN (
      SELECT id AS second_column, COUNT(*) AS cnt
      FROM `patents-public-data.patentsview.patent`
      GROUP BY 1
    ) AS second ON first.patent_id = second.second_column



joins from `patents-public-data:patentsview.patent::id` on **PatentsView patent_id** (9.00%, 572,891 rows)




















*****
## patents-public-data:patentsview.pct_data_201708


Old table version `201708`, schema skipped.





*****
## patents-public-data:patentsview.persistent_inventor_disamb



> PatentsView Data is a database that longitudinally links inventors, their organizations, locations, and overall patenting activity. The dataset uses data derived from USPTO bulk data files.
> 
> “PatentsView” by the USPTO, US Department of Agriculture (USDA), the Center for the Science of Science and Innovation Policy, New York University, the University of California at Berkeley, Twin Arch Technologies, and Periscopic, used under CC BY 4.0.





| Stat | Value |
|----------|----------|
| Last updated | 2017-10-13 |
| Rows | 14,959,652 |
| Size | 728.5 MB |

### Schema
[View in BigQuery](https://bigquery.cloud.google.com/table/patents-public-data:patentsview.persistent_inventor_disamb)

* `rawinventor_id` STRING  

* `disamb_inventor_id_20170307` STRING  

* `disamb_inventor_id_20170808` STRING  














*****
## patents-public-data:patentsview.persistent_inventor_disamb_201708


Old table version `201708`, schema skipped.





*****
## patents-public-data:patentsview.rawassignee



> PatentsView Data is a database that longitudinally links inventors, their organizations, locations, and overall patenting activity. The dataset uses data derived from USPTO bulk data files.
> 
> “PatentsView” by the USPTO, US Department of Agriculture (USDA), the Center for the Science of Science and Innovation Policy, New York University, the University of California at Berkeley, Twin Arch Technologies, and Periscopic, used under CC BY 4.0.





| Stat | Value |
|----------|----------|
| Last updated | 2017-10-13 |
| Rows | 5,629,565 |
| Size | 734.8 MB |

### Schema
[View in BigQuery](https://bigquery.cloud.google.com/table/patents-public-data:patentsview.rawassignee)

* `uuid` STRING  

* `patent_id` STRING   joins on **PatentsView patent_id**

* `assignee_id` STRING  

* `rawlocation_id` STRING  

* `type` STRING  

* `name_first` STRING  

* `name_last` STRING  

* `organization` STRING  

* `sequence` STRING  



### Join columns




#### patent_id

joins to `patents-public-data:patentsview.patent::id` on **PatentsView patent_id** (100.00%, 5,629,565 rows)

| Key | Percent | Rows | Sample values |
|------|-----|--------|--------------------------------------------------------|
| `all` | 100.00% | 5,629,565 | `['9311986', '7512376', '8142008', '6432904', '6715281']` |


    #standardSQL
    SELECT
      COUNT(*) AS cnt,
      COUNT(second.second_column) AS second_cnt,
      ARRAY_AGG(first.patent_id IGNORE NULLS ORDER BY RAND() LIMIT 5) AS sample_value
    FROM `patents-public-data.patentsview.rawassignee`AS first
    LEFT JOIN (
      SELECT id AS second_column, COUNT(*) AS cnt
      FROM `patents-public-data.patentsview.patent`
      GROUP BY 1
    ) AS second ON first.patent_id = second.second_column



joins from `patents-public-data:patentsview.patent::id` on **PatentsView patent_id** (85.62%, 5,451,096 rows)




















*****
## patents-public-data:patentsview.rawassignee_201708


Old table version `201708`, schema skipped.





*****
## patents-public-data:patentsview.rawexaminer



> PatentsView Data is a database that longitudinally links inventors, their organizations, locations, and overall patenting activity. The dataset uses data derived from USPTO bulk data files.
> 
> “PatentsView” by the USPTO, US Department of Agriculture (USDA), the Center for the Science of Science and Innovation Policy, New York University, the University of California at Berkeley, Twin Arch Technologies, and Periscopic, used under CC BY 4.0.





| Stat | Value |
|----------|----------|
| Last updated | 2017-10-13 |
| Rows | 8,727,147 |
| Size | 584.9 MB |

### Schema
[View in BigQuery](https://bigquery.cloud.google.com/table/patents-public-data:patentsview.rawexaminer)

* `uuid` STRING  

* `patent_id` STRING   joins on **PatentsView patent_id**

* `name_first` STRING  

* `name_last` STRING  

* `role` STRING  

* `group` STRING  



### Join columns




#### patent_id

joins to `patents-public-data:patentsview.patent::id` on **PatentsView patent_id** (100.00%, 8,727,147 rows)

| Key | Percent | Rows | Sample values |
|------|-----|--------|--------------------------------------------------------|
| `all` | 100.00% | 8,727,147 | `['9206285', 'D327083', '8026714', 'D472087', '4372373']` |


    #standardSQL
    SELECT
      COUNT(*) AS cnt,
      COUNT(second.second_column) AS second_cnt,
      ARRAY_AGG(first.patent_id IGNORE NULLS ORDER BY RAND() LIMIT 5) AS sample_value
    FROM `patents-public-data.patentsview.rawexaminer`AS first
    LEFT JOIN (
      SELECT id AS second_column, COUNT(*) AS cnt
      FROM `patents-public-data.patentsview.patent`
      GROUP BY 1
    ) AS second ON first.patent_id = second.second_column



joins from `patents-public-data:patentsview.patent::id` on **PatentsView patent_id** (99.98%, 6,365,105 rows)














*****
## patents-public-data:patentsview.rawexaminer_201708


Old table version `201708`, schema skipped.





*****
## patents-public-data:patentsview.rawinventor



> PatentsView Data is a database that longitudinally links inventors, their organizations, locations, and overall patenting activity. The dataset uses data derived from USPTO bulk data files.
> 
> “PatentsView” by the USPTO, US Department of Agriculture (USDA), the Center for the Science of Science and Innovation Policy, New York University, the University of California at Berkeley, Twin Arch Technologies, and Periscopic, used under CC BY 4.0.





| Stat | Value |
|----------|----------|
| Last updated | 2017-10-13 |
| Rows | 14,959,652 |
| Size | 1.5 GB |

### Schema
[View in BigQuery](https://bigquery.cloud.google.com/table/patents-public-data:patentsview.rawinventor)

* `uuid` STRING  

* `patent_id` STRING   joins on **PatentsView patent_id**

* `inventor_id` STRING  

* `rawlocation_id` STRING  

* `name_first` STRING  

* `name_last` STRING  

* `sequence` STRING  

* `rule_47` STRING  



### Join columns




#### patent_id

joins to `patents-public-data:patentsview.patent::id` on **PatentsView patent_id** (100.00%, 14,959,652 rows)

| Key | Percent | Rows | Sample values |
|------|-----|--------|--------------------------------------------------------|
| `all` | 100.00% | 14,959,652 | `['8665712', '9365638', '8961055', '7102858', '4314078']` |


    #standardSQL
    SELECT
      COUNT(*) AS cnt,
      COUNT(second.second_column) AS second_cnt,
      ARRAY_AGG(first.patent_id IGNORE NULLS ORDER BY RAND() LIMIT 5) AS sample_value
    FROM `patents-public-data.patentsview.rawinventor`AS first
    LEFT JOIN (
      SELECT id AS second_column, COUNT(*) AS cnt
      FROM `patents-public-data.patentsview.patent`
      GROUP BY 1
    ) AS second ON first.patent_id = second.second_column



joins from `patents-public-data:patentsview.patent::id` on **PatentsView patent_id** (99.99%, 6,365,851 rows)


















*****
## patents-public-data:patentsview.rawinventor_201708


Old table version `201708`, schema skipped.





*****
## patents-public-data:patentsview.rawlawyer



> PatentsView Data is a database that longitudinally links inventors, their organizations, locations, and overall patenting activity. The dataset uses data derived from USPTO bulk data files.
> 
> “PatentsView” by the USPTO, US Department of Agriculture (USDA), the Center for the Science of Science and Innovation Policy, New York University, the University of California at Berkeley, Twin Arch Technologies, and Periscopic, used under CC BY 4.0.





| Stat | Value |
|----------|----------|
| Last updated | 2017-10-13 |
| Rows | 7,226,654 |
| Size | 730.6 MB |

### Schema
[View in BigQuery](https://bigquery.cloud.google.com/table/patents-public-data:patentsview.rawlawyer)

* `uuid` STRING  

* `lawyer_id` STRING  

* `patent_id` STRING   joins on **PatentsView patent_id**

* `name_first` STRING  

* `name_last` STRING  

* `organization` STRING  

* `country` STRING  

* `sequence` STRING  



### Join columns






#### patent_id

joins to `patents-public-data:patentsview.patent::id` on **PatentsView patent_id** (100.00%, 7,226,654 rows)

| Key | Percent | Rows | Sample values |
|------|-----|--------|--------------------------------------------------------|
| `all` | 100.00% | 7,226,654 | `['5228771', '5771060', '4183744', '6539452', '8612261']` |


    #standardSQL
    SELECT
      COUNT(*) AS cnt,
      COUNT(second.second_column) AS second_cnt,
      ARRAY_AGG(first.patent_id IGNORE NULLS ORDER BY RAND() LIMIT 5) AS sample_value
    FROM `patents-public-data.patentsview.rawlawyer`AS first
    LEFT JOIN (
      SELECT id AS second_column, COUNT(*) AS cnt
      FROM `patents-public-data.patentsview.patent`
      GROUP BY 1
    ) AS second ON first.patent_id = second.second_column



joins from `patents-public-data:patentsview.patent::id` on **PatentsView patent_id** (92.44%, 5,885,426 rows)
















*****
## patents-public-data:patentsview.rawlawyer_201708


Old table version `201708`, schema skipped.





*****
## patents-public-data:patentsview.rawlocation



> PatentsView Data is a database that longitudinally links inventors, their organizations, locations, and overall patenting activity. The dataset uses data derived from USPTO bulk data files.
> 
> “PatentsView” by the USPTO, US Department of Agriculture (USDA), the Center for the Science of Science and Innovation Policy, New York University, the University of California at Berkeley, Twin Arch Technologies, and Periscopic, used under CC BY 4.0.





| Stat | Value |
|----------|----------|
| Last updated | 2017-10-13 |
| Rows | 20,705,708 |
| Size | 1.7 GB |

### Schema
[View in BigQuery](https://bigquery.cloud.google.com/table/patents-public-data:patentsview.rawlocation)

* `id` STRING  

* `location_id` STRING  

* `city` STRING  

* `state` STRING  

* `country` STRING  

* `latlong` STRING  




















*****
## patents-public-data:patentsview.rawlocation_201708


Old table version `201708`, schema skipped.





*****
## patents-public-data:patentsview.rel_app_text



> PatentsView Data is a database that longitudinally links inventors, their organizations, locations, and overall patenting activity. The dataset uses data derived from USPTO bulk data files.
> 
> “PatentsView” by the USPTO, US Department of Agriculture (USDA), the Center for the Science of Science and Innovation Policy, New York University, the University of California at Berkeley, Twin Arch Technologies, and Periscopic, used under CC BY 4.0.





| Stat | Value |
|----------|----------|
| Last updated | 2017-10-13 |
| Rows | 1,438,215 |
| Size | 604.4 MB |

### Schema
[View in BigQuery](https://bigquery.cloud.google.com/table/patents-public-data:patentsview.rel_app_text)

* `uuid` STRING  

* `patent_id` STRING   joins on **PatentsView patent_id**

* `text` STRING  

* `sequence` STRING  



### Join columns




#### patent_id

joins to `patents-public-data:patentsview.patent::id` on **PatentsView patent_id** (100.00%, 1,438,215 rows)

| Key | Percent | Rows | Sample values |
|------|-----|--------|--------------------------------------------------------|
| `all` | 100.00% | 1,438,215 | `['9449654', '8623030', '8519425', '3956232', '9173863']` |


    #standardSQL
    SELECT
      COUNT(*) AS cnt,
      COUNT(second.second_column) AS second_cnt,
      ARRAY_AGG(first.patent_id IGNORE NULLS ORDER BY RAND() LIMIT 5) AS sample_value
    FROM `patents-public-data.patentsview.rel_app_text`AS first
    LEFT JOIN (
      SELECT id AS second_column, COUNT(*) AS cnt
      FROM `patents-public-data.patentsview.patent`
      GROUP BY 1
    ) AS second ON first.patent_id = second.second_column



joins from `patents-public-data:patentsview.patent::id` on **PatentsView patent_id** (22.59%, 1,438,215 rows)










*****
## patents-public-data:patentsview.rel_app_text_201708


Old table version `201708`, schema skipped.





*****
## patents-public-data:patentsview.subclass



> PatentsView Data is a database that longitudinally links inventors, their organizations, locations, and overall patenting activity. The dataset uses data derived from USPTO bulk data files.
> 
> “PatentsView” by the USPTO, US Department of Agriculture (USDA), the Center for the Science of Science and Innovation Policy, New York University, the University of California at Berkeley, Twin Arch Technologies, and Periscopic, used under CC BY 4.0.





| Stat | Value |
|----------|----------|
| Last updated | 2017-10-13 |
| Rows | 264,386 |
| Size | 2.4 MB |

### Schema
[View in BigQuery](https://bigquery.cloud.google.com/table/patents-public-data:patentsview.subclass)

* `id` STRING  










*****
## patents-public-data:patentsview.subclass_201708


Old table version `201708`, schema skipped.





*****
## patents-public-data:patentsview.subclass_current



> PatentsView Data is a database that longitudinally links inventors, their organizations, locations, and overall patenting activity. The dataset uses data derived from USPTO bulk data files.
> 
> “PatentsView” by the USPTO, US Department of Agriculture (USDA), the Center for the Science of Science and Innovation Policy, New York University, the University of California at Berkeley, Twin Arch Technologies, and Periscopic, used under CC BY 4.0.





| Stat | Value |
|----------|----------|
| Last updated | 2017-10-13 |
| Rows | 171,053 |
| Size | 7.4 MB |

### Schema
[View in BigQuery](https://bigquery.cloud.google.com/table/patents-public-data:patentsview.subclass_current)

* `id` STRING  

* `title` STRING  












*****
## patents-public-data:patentsview.subclass_current_201708


Old table version `201708`, schema skipped.





*****
## patents-public-data:patentsview.us_term_of_grant



> PatentsView Data is a database that longitudinally links inventors, their organizations, locations, and overall patenting activity. The dataset uses data derived from USPTO bulk data files.
> 
> “PatentsView” by the USPTO, US Department of Agriculture (USDA), the Center for the Science of Science and Innovation Policy, New York University, the University of California at Berkeley, Twin Arch Technologies, and Periscopic, used under CC BY 4.0.





| Stat | Value |
|----------|----------|
| Last updated | 2017-10-13 |
| Rows | 2,923,111 |
| Size | 181.1 MB |

### Schema
[View in BigQuery](https://bigquery.cloud.google.com/table/patents-public-data:patentsview.us_term_of_grant)

* `uuid` STRING  

* `patent_id` STRING   joins on **PatentsView patent_id**

* `lapse_of_patent` STRING  

* `disclaimer_date` STRING  

* `term_disclaimer` STRING  

* `term_grant` STRING  

* `term_extension` STRING  



### Join columns




#### patent_id

joins to `patents-public-data:patentsview.patent::id` on **PatentsView patent_id** (100.00%, 2,923,111 rows)

| Key | Percent | Rows | Sample values |
|------|-----|--------|--------------------------------------------------------|
| `all` | 100.00% | 2,923,111 | `['7468394', '6911314', '8268000', '7629442', 'D699025']` |


    #standardSQL
    SELECT
      COUNT(*) AS cnt,
      COUNT(second.second_column) AS second_cnt,
      ARRAY_AGG(first.patent_id IGNORE NULLS ORDER BY RAND() LIMIT 5) AS sample_value
    FROM `patents-public-data.patentsview.us_term_of_grant`AS first
    LEFT JOIN (
      SELECT id AS second_column, COUNT(*) AS cnt
      FROM `patents-public-data.patentsview.patent`
      GROUP BY 1
    ) AS second ON first.patent_id = second.second_column



joins from `patents-public-data:patentsview.patent::id` on **PatentsView patent_id** (45.91%, 2,923,111 rows)
















*****
## patents-public-data:patentsview.us_term_of_grant_201708


Old table version `201708`, schema skipped.





*****
## patents-public-data:patentsview.usapplicationcitation



> PatentsView Data is a database that longitudinally links inventors, their organizations, locations, and overall patenting activity. The dataset uses data derived from USPTO bulk data files.
> 
> “PatentsView” by the USPTO, US Department of Agriculture (USDA), the Center for the Science of Science and Innovation Policy, New York University, the University of California at Berkeley, Twin Arch Technologies, and Periscopic, used under CC BY 4.0.





| Stat | Value |
|----------|----------|
| Last updated | 2017-10-13 |
| Rows | 25,343,373 |
| Size | 3.1 GB |

### Schema
[View in BigQuery](https://bigquery.cloud.google.com/table/patents-public-data:patentsview.usapplicationcitation)

* `uuid` STRING  

* `patent_id` STRING   joins on **PatentsView patent_id**

* `application_id` STRING  

* `date` STRING  

* `name` STRING  

* `kind` STRING  

* `number` STRING  

* `country` STRING  

* `category` STRING  

* `sequence` STRING  



### Join columns




#### patent_id

joins to `patents-public-data:patentsview.patent::id` on **PatentsView patent_id** (100.00%, 25,343,373 rows)

| Key | Percent | Rows | Sample values |
|------|-----|--------|--------------------------------------------------------|
| `all` | 100.00% | 25,343,373 | `['8729544', '9330598', '7254249', '8364808', '8085759']` |


    #standardSQL
    SELECT
      COUNT(*) AS cnt,
      COUNT(second.second_column) AS second_cnt,
      ARRAY_AGG(first.patent_id IGNORE NULLS ORDER BY RAND() LIMIT 5) AS sample_value
    FROM `patents-public-data.patentsview.usapplicationcitation`AS first
    LEFT JOIN (
      SELECT id AS second_column, COUNT(*) AS cnt
      FROM `patents-public-data.patentsview.patent`
      GROUP BY 1
    ) AS second ON first.patent_id = second.second_column



joins from `patents-public-data:patentsview.patent::id` on **PatentsView patent_id** (36.83%, 2,344,704 rows)






















*****
## patents-public-data:patentsview.usapplicationcitation_201708


Old table version `201708`, schema skipped.





*****
## patents-public-data:patentsview.uspatentcitation



> PatentsView Data is a database that longitudinally links inventors, their organizations, locations, and overall patenting activity. The dataset uses data derived from USPTO bulk data files.
> 
> “PatentsView” by the USPTO, US Department of Agriculture (USDA), the Center for the Science of Science and Innovation Policy, New York University, the University of California at Berkeley, Twin Arch Technologies, and Periscopic, used under CC BY 4.0.





| Stat | Value |
|----------|----------|
| Last updated | 2017-10-13 |
| Rows | 89,122,312 |
| Size | 8.7 GB |

### Schema
[View in BigQuery](https://bigquery.cloud.google.com/table/patents-public-data:patentsview.uspatentcitation)

* `uuid` STRING  

* `patent_id` STRING   joins on **PatentsView patent_id**

* `citation_id` STRING  

* `date` STRING  

* `name` STRING  

* `kind` STRING  

* `country` STRING  

* `category` STRING  

* `sequence` STRING  



### Join columns




#### patent_id

joins to `patents-public-data:patentsview.patent::id` on **PatentsView patent_id** (100.00%, 89,122,312 rows)

| Key | Percent | Rows | Sample values |
|------|-----|--------|--------------------------------------------------------|
| `all` | 100.00% | 89,122,312 | `['7747835', '8616663', '6423003', '6493479', '4062681']` |


    #standardSQL
    SELECT
      COUNT(*) AS cnt,
      COUNT(second.second_column) AS second_cnt,
      ARRAY_AGG(first.patent_id IGNORE NULLS ORDER BY RAND() LIMIT 5) AS sample_value
    FROM `patents-public-data.patentsview.uspatentcitation`AS first
    LEFT JOIN (
      SELECT id AS second_column, COUNT(*) AS cnt
      FROM `patents-public-data.patentsview.patent`
      GROUP BY 1
    ) AS second ON first.patent_id = second.second_column



joins from `patents-public-data:patentsview.patent::id` on **PatentsView patent_id** (95.36%, 6,071,414 rows)




















*****
## patents-public-data:patentsview.uspatentcitation_201708


Old table version `201708`, schema skipped.





*****
## patents-public-data:patentsview.uspc



> PatentsView Data is a database that longitudinally links inventors, their organizations, locations, and overall patenting activity. The dataset uses data derived from USPTO bulk data files.
> 
> “PatentsView” by the USPTO, US Department of Agriculture (USDA), the Center for the Science of Science and Innovation Policy, New York University, the University of California at Berkeley, Twin Arch Technologies, and Periscopic, used under CC BY 4.0.





| Stat | Value |
|----------|----------|
| Last updated | 2017-10-13 |
| Rows | 18,024,187 |
| Size | 954.3 MB |

### Schema
[View in BigQuery](https://bigquery.cloud.google.com/table/patents-public-data:patentsview.uspc)

* `uuid` STRING  

* `patent_id` STRING   joins on **PatentsView patent_id**

* `mainclass_id` STRING  

* `subclass_id` STRING  

* `sequence` STRING  



### Join columns




#### patent_id

joins to `patents-public-data:patentsview.patent::id` on **PatentsView patent_id** (100.00%, 18,024,187 rows)

| Key | Percent | Rows | Sample values |
|------|-----|--------|--------------------------------------------------------|
| `all` | 100.00% | 18,024,187 | `['5690987', '5882426', '7040837', '7323759', '5122832']` |


    #standardSQL
    SELECT
      COUNT(*) AS cnt,
      COUNT(second.second_column) AS second_cnt,
      ARRAY_AGG(first.patent_id IGNORE NULLS ORDER BY RAND() LIMIT 5) AS sample_value
    FROM `patents-public-data.patentsview.uspc`AS first
    LEFT JOIN (
      SELECT id AS second_column, COUNT(*) AS cnt
      FROM `patents-public-data.patentsview.patent`
      GROUP BY 1
    ) AS second ON first.patent_id = second.second_column



joins from `patents-public-data:patentsview.patent::id` on **PatentsView patent_id** (79.24%, 5,044,804 rows)












*****
## patents-public-data:patentsview.uspc_201708


Old table version `201708`, schema skipped.





*****
## patents-public-data:patentsview.uspc_current



> PatentsView Data is a database that longitudinally links inventors, their organizations, locations, and overall patenting activity. The dataset uses data derived from USPTO bulk data files.
> 
> “PatentsView” by the USPTO, US Department of Agriculture (USDA), the Center for the Science of Science and Innovation Policy, New York University, the University of California at Berkeley, Twin Arch Technologies, and Periscopic, used under CC BY 4.0.





| Stat | Value |
|----------|----------|
| Last updated | 2017-10-13 |
| Rows | 22,576,756 |
| Size | 1.2 GB |

### Schema
[View in BigQuery](https://bigquery.cloud.google.com/table/patents-public-data:patentsview.uspc_current)

* `uuid` STRING  

* `patent_id` STRING   joins on **PatentsView patent_id**

* `mainclass_id` STRING  

* `subclass_id` STRING  

* `sequence` STRING  



### Join columns




#### patent_id

joins to `patents-public-data:patentsview.patent::id` on **PatentsView patent_id** (100.00%, 22,576,756 rows)

| Key | Percent | Rows | Sample values |
|------|-----|--------|--------------------------------------------------------|
| `all` | 100.00% | 22,576,756 | `['6563835', '5573024', '5762148', '7727383', '4363039']` |


    #standardSQL
    SELECT
      COUNT(*) AS cnt,
      COUNT(second.second_column) AS second_cnt,
      ARRAY_AGG(first.patent_id IGNORE NULLS ORDER BY RAND() LIMIT 5) AS sample_value
    FROM `patents-public-data.patentsview.uspc_current`AS first
    LEFT JOIN (
      SELECT id AS second_column, COUNT(*) AS cnt
      FROM `patents-public-data.patentsview.patent`
      GROUP BY 1
    ) AS second ON first.patent_id = second.second_column



joins from `patents-public-data:patentsview.patent::id` on **PatentsView patent_id** (99.29%, 6,321,292 rows)












*****
## patents-public-data:patentsview.uspc_current_201708


Old table version `201708`, schema skipped.





*****
## patents-public-data:patentsview.usreldoc



> PatentsView Data is a database that longitudinally links inventors, their organizations, locations, and overall patenting activity. The dataset uses data derived from USPTO bulk data files.
> 
> “PatentsView” by the USPTO, US Department of Agriculture (USDA), the Center for the Science of Science and Innovation Policy, New York University, the University of California at Berkeley, Twin Arch Technologies, and Periscopic, used under CC BY 4.0.





| Stat | Value |
|----------|----------|
| Last updated | 2017-10-20 |
| Rows | 8,022,497 |
| Size | 792.1 MB |

### Schema
[View in BigQuery](https://bigquery.cloud.google.com/table/patents-public-data:patentsview.usreldoc)

* `uuid` STRING  

* `patent_id` STRING   joins on **PatentsView patent_id**

* `doctype` STRING  

* `relkind` STRING  

* `reldocno` STRING  

* `country` STRING  

* `date` STRING  

* `status` STRING  

* `sequence` STRING  

* `kind` STRING  



### Join columns




#### patent_id

joins to `patents-public-data:patentsview.patent::id` on **PatentsView patent_id** (100.00%, 8,022,497 rows)

| Key | Percent | Rows | Sample values |
|------|-----|--------|--------------------------------------------------------|
| `all` | 100.00% | 8,022,497 | `['6664339', '9084917', '9621931', '8556225', '6639478']` |


    #standardSQL
    SELECT
      COUNT(*) AS cnt,
      COUNT(second.second_column) AS second_cnt,
      ARRAY_AGG(first.patent_id IGNORE NULLS ORDER BY RAND() LIMIT 5) AS sample_value
    FROM `patents-public-data.patentsview.usreldoc`AS first
    LEFT JOIN (
      SELECT id AS second_column, COUNT(*) AS cnt
      FROM `patents-public-data.patentsview.patent`
      GROUP BY 1
    ) AS second ON first.patent_id = second.second_column



joins from `patents-public-data:patentsview.patent::id` on **PatentsView patent_id** (47.85%, 3,046,372 rows)






















*****
## patents-public-data:patentsview.usreldoc_201708


Old table version `201708`, schema skipped.





*****
## patents-public-data:patentsview.wipo



> PatentsView Data is a database that longitudinally links inventors, their organizations, locations, and overall patenting activity. The dataset uses data derived from USPTO bulk data files.
> 
> “PatentsView” by the USPTO, US Department of Agriculture (USDA), the Center for the Science of Science and Innovation Policy, New York University, the University of California at Berkeley, Twin Arch Technologies, and Periscopic, used under CC BY 4.0.





| Stat | Value |
|----------|----------|
| Last updated | 2017-10-20 |
| Rows | 8,474,756 |
| Size | 133.0 MB |

### Schema
[View in BigQuery](https://bigquery.cloud.google.com/table/patents-public-data:patentsview.wipo)

* `patent_id` STRING   joins on **PatentsView patent_id**

* `field_id` STRING  

* `sequence` STRING  



### Join columns


#### patent_id

joins to `patents-public-data:patentsview.patent::id` on **PatentsView patent_id** (100.00%, 8,474,756 rows)

| Key | Percent | Rows | Sample values |
|------|-----|--------|--------------------------------------------------------|
| `all` | 100.00% | 8,474,756 | `['9256970', '6848866', 'D641165', '9337071', '8815881']` |


    #standardSQL
    SELECT
      COUNT(*) AS cnt,
      COUNT(second.second_column) AS second_cnt,
      ARRAY_AGG(first.patent_id IGNORE NULLS ORDER BY RAND() LIMIT 5) AS sample_value
    FROM `patents-public-data.patentsview.wipo`AS first
    LEFT JOIN (
      SELECT id AS second_column, COUNT(*) AS cnt
      FROM `patents-public-data.patentsview.patent`
      GROUP BY 1
    ) AS second ON first.patent_id = second.second_column



joins from `patents-public-data:patentsview.patent::id` on **PatentsView patent_id** (99.26%, 6,319,470 rows)










*****
## patents-public-data:patentsview.wipo_201708


Old table version `201708`, schema skipped.





*****
## patents-public-data:patentsview.wipo_field



> PatentsView Data is a database that longitudinally links inventors, their organizations, locations, and overall patenting activity. The dataset uses data derived from USPTO bulk data files.
> 
> “PatentsView” by the USPTO, US Department of Agriculture (USDA), the Center for the Science of Science and Innovation Policy, New York University, the University of California at Berkeley, Twin Arch Technologies, and Periscopic, used under CC BY 4.0.





| Stat | Value |
|----------|----------|
| Last updated | 2017-10-20 |
| Rows | 70 |
| Size | 3.6 kB |

### Schema
[View in BigQuery](https://bigquery.cloud.google.com/table/patents-public-data:patentsview.wipo_field)

* `id` STRING  

* `sector_title` STRING  

* `field_title` STRING  














*****
## patents-public-data:patentsview.wipo_field_201708


Old table version `201708`, schema skipped.





*****
## patents-public-data:uspto_oce_assignment.assignee



> USPTO OCE Patent Assignment Dataset contains detailed data patent assignments and other transactions recorded at the USPTO since 1970.
> 
> "USPTO OCE Patent Assignment Data" by the USPTO, for public use.
> Marco, Alan C., Graham, Stuart J.H., Myers, Amanda F., D'Agostino, Paul A and Apple, Kirsten, "The USPTO Patent Assignment Dataset: Descriptions and Analysis" (July 27, 2015).





| Stat | Value |
|----------|----------|
| Last updated | 2017-10-12 |
| Rows | 7,495,292 |
| Size | 720.6 MB |

### Schema
[View in BigQuery](https://bigquery.cloud.google.com/table/patents-public-data:uspto_oce_assignment.assignee)

* `rf_id` STRING  

* `ee_name` STRING  

* `ee_address_1` STRING  

* `ee_address_2` STRING  

* `ee_city` STRING  

* `ee_state` STRING  

* `ee_postcode` STRING  

* `ee_country` STRING  
























*****
## patents-public-data:uspto_oce_assignment.assignee_2016


Old table version `2016`, schema skipped.





*****
## patents-public-data:uspto_oce_assignment.assignment



> USPTO OCE Patent Assignment Dataset contains detailed data patent assignments and other transactions recorded at the USPTO since 1970.
> 
> "USPTO OCE Patent Assignment Data" by the USPTO, for public use.
> Marco, Alan C., Graham, Stuart J.H., Myers, Amanda F., D'Agostino, Paul A and Apple, Kirsten, "The USPTO Patent Assignment Dataset: Descriptions and Analysis" (July 27, 2015).





| Stat | Value |
|----------|----------|
| Last updated | 2017-10-12 |
| Rows | 7,239,361 |
| Size | 1.5 GB |

### Schema
[View in BigQuery](https://bigquery.cloud.google.com/table/patents-public-data:uspto_oce_assignment.assignment)

* `rf_id` STRING  

* `file_id` STRING  

* `cname` STRING  

* `caddress_1` STRING  

* `caddress_2` STRING  

* `caddress_3` STRING  

* `caddress_4` STRING  

* `reel_no` STRING  

* `frame_no` STRING  

* `convey_text` STRING  

* `record_dt` STRING  

* `last_update_dt` STRING  

* `page_count` STRING  

* `purge_in` STRING  




































*****
## patents-public-data:uspto_oce_assignment.assignment_2016


Old table version `2016`, schema skipped.





*****
## patents-public-data:uspto_oce_assignment.assignment_conveyance



> USPTO OCE Patent Assignment Dataset contains detailed data patent assignments and other transactions recorded at the USPTO since 1970.
> 
> "USPTO OCE Patent Assignment Data" by the USPTO, for public use.
> Marco, Alan C., Graham, Stuart J.H., Myers, Amanda F., D'Agostino, Paul A and Apple, Kirsten, "The USPTO Patent Assignment Dataset: Descriptions and Analysis" (July 27, 2015).





| Stat | Value |
|----------|----------|
| Last updated | 2017-10-12 |
| Rows | 7,239,361 |
| Size | 184.9 MB |

### Schema
[View in BigQuery](https://bigquery.cloud.google.com/table/patents-public-data:uspto_oce_assignment.assignment_conveyance)

* `rf_id` STRING  

* `convey_ty` STRING  

* `employer_assign` STRING  














*****
## patents-public-data:uspto_oce_assignment.assignment_conveyance_2016


Old table version `2016`, schema skipped.





*****
## patents-public-data:uspto_oce_assignment.assignor



> USPTO OCE Patent Assignment Dataset contains detailed data patent assignments and other transactions recorded at the USPTO since 1970.
> 
> "USPTO OCE Patent Assignment Data" by the USPTO, for public use.
> Marco, Alan C., Graham, Stuart J.H., Myers, Amanda F., D'Agostino, Paul A and Apple, Kirsten, "The USPTO Patent Assignment Dataset: Descriptions and Analysis" (July 27, 2015).





| Stat | Value |
|----------|----------|
| Last updated | 2017-10-12 |
| Rows | 16,766,049 |
| Size | 694.3 MB |

### Schema
[View in BigQuery](https://bigquery.cloud.google.com/table/patents-public-data:uspto_oce_assignment.assignor)

* `rf_id` STRING  

* `or_name` STRING  

* `exec_dt` STRING  

* `ack_dt` STRING  
















*****
## patents-public-data:uspto_oce_assignment.assignor_2016


Old table version `2016`, schema skipped.





*****
## patents-public-data:uspto_oce_assignment.documentid



> USPTO OCE Patent Assignment Dataset contains detailed data patent assignments and other transactions recorded at the USPTO since 1970.
> 
> "USPTO OCE Patent Assignment Data" by the USPTO, for public use.
> Marco, Alan C., Graham, Stuart J.H., Myers, Amanda F., D'Agostino, Paul A and Apple, Kirsten, "The USPTO Patent Assignment Dataset: Descriptions and Analysis" (July 27, 2015).





| Stat | Value |
|----------|----------|
| Last updated | 2017-10-12 |
| Rows | 12,177,345 |
| Size | 1.6 GB |

### Schema
[View in BigQuery](https://bigquery.cloud.google.com/table/patents-public-data:uspto_oce_assignment.documentid)

* `rf_id` STRING  

* `title` STRING  

* `lang` STRING  

* `appno_doc_num` STRING  

* `appno_date` STRING  

* `appno_country` STRING  

* `pgpub_doc_num` STRING   joins on **OCE Assignment pgpub_doc_num**

* `pgpub_date` STRING  

* `pgpub_country` STRING  

* `grant_doc_num` STRING   joins on **OCE Assignment grant_doc_num**

* `grant_date` STRING  

* `grant_country` STRING  



### Join columns














#### pgpub_doc_num

joins to `patents-public-data:uspto_oce_assignment.match::pgpub_doc_num` on **OCE Assignment pgpub_doc_num** (54.48%, 6,634,799 rows)

| Key | Percent | Rows | Sample values |
|------|-----|--------|--------------------------------------------------------|
| `all` | 54.48% | 6,634,799 | `['20020091331', '20020004365', '20150144491', '20070074869', '20040065311']` |


    #standardSQL
    SELECT
      COUNT(*) AS cnt,
      COUNT(second.second_column) AS second_cnt,
      ARRAY_AGG(first.pgpub_doc_num IGNORE NULLS ORDER BY RAND() LIMIT 5) AS sample_value
    FROM `patents-public-data.uspto_oce_assignment.documentid`AS first
    LEFT JOIN (
      SELECT pgpub_doc_num AS second_column, COUNT(*) AS cnt
      FROM `patents-public-data.uspto_oce_assignment.match`
      GROUP BY 1
    ) AS second ON first.pgpub_doc_num = second.second_column



joins from `patents-public-data:uspto_oce_assignment.match::pgpub_doc_num` on **OCE Assignment pgpub_doc_num** (44.41%, 3,940,447 rows)








#### grant_doc_num

joins to `patents-public-data:uspto_oce_assignment.match::grant_doc_num` on **OCE Assignment grant_doc_num** (81.65%, 9,942,785 rows)

| Key | Percent | Rows | Sample values |
|------|-----|--------|--------------------------------------------------------|
| `all` | 81.65% | 9,942,785 | `['6140234', '8047950', '5314696', '7460178', 'D365706']` |


    #standardSQL
    SELECT
      COUNT(*) AS cnt,
      COUNT(second.second_column) AS second_cnt,
      ARRAY_AGG(first.grant_doc_num IGNORE NULLS ORDER BY RAND() LIMIT 5) AS sample_value
    FROM `patents-public-data.uspto_oce_assignment.documentid`AS first
    LEFT JOIN (
      SELECT grant_doc_num AS second_column, COUNT(*) AS cnt
      FROM `patents-public-data.uspto_oce_assignment.match`
      GROUP BY 1
    ) AS second ON first.grant_doc_num = second.second_column



joins from `patents-public-data:uspto_oce_assignment.match::grant_doc_num` on **OCE Assignment grant_doc_num** (55.59%, 4,932,961 rows)










*****
## patents-public-data:uspto_oce_assignment.documentid_2016


Old table version `2016`, schema skipped.





*****
## patents-public-data:uspto_oce_assignment.documentid_admin



> USPTO OCE Patent Assignment Dataset contains detailed data patent assignments and other transactions recorded at the USPTO since 1970.
> 
> "USPTO OCE Patent Assignment Data" by the USPTO, for public use.
> Marco, Alan C., Graham, Stuart J.H., Myers, Amanda F., D'Agostino, Paul A and Apple, Kirsten, "The USPTO Patent Assignment Dataset: Descriptions and Analysis" (July 27, 2015).





| Stat | Value |
|----------|----------|
| Last updated | 2017-10-12 |
| Rows | 12,131,132 |
| Size | 598.4 MB |

### Schema
[View in BigQuery](https://bigquery.cloud.google.com/table/patents-public-data:uspto_oce_assignment.documentid_admin)

* `rf_id` STRING  

* `appno_doc_num` STRING  

* `grant_doc_num` STRING  

* `admin_appl_id_for_grant` STRING  

* `admin_pat_no_for_appno` STRING  

* `error` STRING  




















*****
## patents-public-data:uspto_oce_assignment.documentid_admin_2016


Old table version `2016`, schema skipped.





*****
## patents-public-data:uspto_oce_assignment.match



> USPTO OCE Patent Assignment Dataset contains detailed data patent assignments and other transactions recorded at the USPTO since 1970.
> 
> "USPTO OCE Patent Assignment Data" by the USPTO, for public use.
> Marco, Alan C., Graham, Stuart J.H., Myers, Amanda F., D'Agostino, Paul A and Apple, Kirsten, "The USPTO Patent Assignment Dataset: Descriptions and Analysis" (July 27, 2015).





| Stat | Value |
|----------|----------|
| Last updated | 2017-10-22 |
| Rows | 8,873,408 |
| Size | 256.3 MB |

### Schema
[View in BigQuery](https://bigquery.cloud.google.com/table/patents-public-data:uspto_oce_assignment.match)

* `pgpub_doc_num` STRING NULLABLE  joins on **OCE Assignment pgpub_doc_num**

* `grant_doc_num` STRING NULLABLE  joins on **OCE Assignment grant_doc_num**

* `publication_number` STRING NULLABLE  joins on **publication_number**



### Join columns


#### pgpub_doc_num

joins to `patents-public-data:uspto_oce_assignment.documentid::pgpub_doc_num` on **OCE Assignment pgpub_doc_num** (44.41%, 3,940,447 rows)

| Key | Percent | Rows | Sample values |
|------|-----|--------|--------------------------------------------------------|
| `all` | 44.41% | 3,940,447 | `['20120156833', '20150251856', '', '20030141080', '20020095069']` |


    #standardSQL
    SELECT
      COUNT(*) AS cnt,
      COUNT(second.second_column) AS second_cnt,
      ARRAY_AGG(first.pgpub_doc_num IGNORE NULLS ORDER BY RAND() LIMIT 5) AS sample_value
    FROM `patents-public-data.uspto_oce_assignment.match`AS first
    LEFT JOIN (
      SELECT pgpub_doc_num AS second_column, COUNT(*) AS cnt
      FROM `patents-public-data.uspto_oce_assignment.documentid`
      GROUP BY 1
    ) AS second ON first.pgpub_doc_num = second.second_column



joins from `patents-public-data:uspto_oce_assignment.documentid::pgpub_doc_num` on **OCE Assignment pgpub_doc_num** (54.48%, 6,634,799 rows)




#### grant_doc_num

joins to `patents-public-data:uspto_oce_assignment.documentid::grant_doc_num` on **OCE Assignment grant_doc_num** (55.59%, 4,932,961 rows)

| Key | Percent | Rows | Sample values |
|------|-----|--------|--------------------------------------------------------|
| `all` | 55.59% | 4,932,961 | `['7380595', '', '7494038', '9264718', '6884598']` |


    #standardSQL
    SELECT
      COUNT(*) AS cnt,
      COUNT(second.second_column) AS second_cnt,
      ARRAY_AGG(first.grant_doc_num IGNORE NULLS ORDER BY RAND() LIMIT 5) AS sample_value
    FROM `patents-public-data.uspto_oce_assignment.match`AS first
    LEFT JOIN (
      SELECT grant_doc_num AS second_column, COUNT(*) AS cnt
      FROM `patents-public-data.uspto_oce_assignment.documentid`
      GROUP BY 1
    ) AS second ON first.grant_doc_num = second.second_column



joins from `patents-public-data:uspto_oce_assignment.documentid::grant_doc_num` on **OCE Assignment grant_doc_num** (81.65%, 9,942,785 rows)




#### publication_number

joins to `patents-public-data:patents.publications::publication_number` on **publication_number** (99.96%, 8,869,754 rows)

| Key | Percent | Rows | Sample values |
|------|-----|--------|--------------------------------------------------------|
| `all` | 99.96% | 8,869,754 | `['US-2014016098-A1', 'US-8008688-B2', 'US-7364189-B2', 'US-2011311184-A1', 'US-2015005717-A1']` |


    #standardSQL
    SELECT
      COUNT(*) AS cnt,
      COUNT(second.second_column) AS second_cnt,
      ARRAY_AGG(first.publication_number IGNORE NULLS ORDER BY RAND() LIMIT 5) AS sample_value
    FROM `patents-public-data.uspto_oce_assignment.match`AS first
    LEFT JOIN (
      SELECT publication_number AS second_column, COUNT(*) AS cnt
      FROM `patents-public-data.patents.publications`
      GROUP BY 1
    ) AS second ON first.publication_number = second.second_column



joins from `patents-public-data:patents.publications::publication_number` on **publication_number** (9.03%, 8,869,739 rows)






*****
## patents-public-data:uspto_oce_assignment.match_2016


Old table version `2016`, schema skipped.





*****
## patents-public-data:uspto_oce_cancer.match



> USPTO Cancer Moonshot Patent Data was generated using USPTO examiner tools to execute a series of queries designed to identify cancer-specific patents and patent applications. This includes drugs, diagnostics, cell lines, mouse models, radiation-based devices, surgical devices, image analytics, data analytics, and genomic-based inventions.
> 
> “USPTO Cancer Moonshot Patent Data” by the USPTO, for public use. Frumkin, Jesse and Myers, Amanda F., Cancer Moonshot Patent Data (August, 2016).





| Stat | Value |
|----------|----------|
| Last updated | 2017-10-23 |
| Rows | 269,244 |
| Size | 9.1 MB |

### Schema
[View in BigQuery](https://bigquery.cloud.google.com/table/patents-public-data:uspto_oce_cancer.match)

* `Patent_or_Publication_ID` STRING NULLABLE  joins on **OCE Cancer id**

* `publication_number` STRING NULLABLE  joins on **publication_number**



### Join columns


#### Patent_or_Publication_ID

joins to `patents-public-data:uspto_oce_cancer.publications::Patent_or_Publication_ID` on **OCE Cancer id** (100.00%, 269,244 rows)

| Key | Percent | Rows | Sample values |
|------|-----|--------|--------------------------------------------------------|
| `all` | 100.00% | 269,244 | `['US 20150185202 A1', 'US 20060111365 A1', 'US 20070298056 A1', 'US 8853396 B2', 'US 20090198074 A1']` |


    #standardSQL
    SELECT
      COUNT(*) AS cnt,
      COUNT(second.second_column) AS second_cnt,
      ARRAY_AGG(first.Patent_or_Publication_ID IGNORE NULLS ORDER BY RAND() LIMIT 5) AS sample_value
    FROM `patents-public-data.uspto_oce_cancer.match`AS first
    LEFT JOIN (
      SELECT Patent_or_Publication_ID AS second_column, COUNT(*) AS cnt
      FROM `patents-public-data.uspto_oce_cancer.publications`
      GROUP BY 1
    ) AS second ON first.Patent_or_Publication_ID = second.second_column



joins from `patents-public-data:uspto_oce_cancer.publications::Patent_or_Publication_ID` on **OCE Cancer id** (100.00%, 269,353 rows)




#### publication_number

joins to `patents-public-data:patents.publications::publication_number` on **publication_number** (99.97%, 269,168 rows)

| Key | Percent | Rows | Sample values |
|------|-----|--------|--------------------------------------------------------|
| `all` | 99.97% | 269,168 | `['US-2012251489-A1', 'US-8119742-B2', 'US-5651970-A', 'US-2015259313-A1', 'US-2007027408-A1']` |


    #standardSQL
    SELECT
      COUNT(*) AS cnt,
      COUNT(second.second_column) AS second_cnt,
      ARRAY_AGG(first.publication_number IGNORE NULLS ORDER BY RAND() LIMIT 5) AS sample_value
    FROM `patents-public-data.uspto_oce_cancer.match`AS first
    LEFT JOIN (
      SELECT publication_number AS second_column, COUNT(*) AS cnt
      FROM `patents-public-data.patents.publications`
      GROUP BY 1
    ) AS second ON first.publication_number = second.second_column



joins from `patents-public-data:patents.publications::publication_number` on **publication_number** (0.27%, 269,168 rows)






*****
## patents-public-data:uspto_oce_cancer.publications



> USPTO Cancer Moonshot Patent Data was generated using USPTO examiner tools to execute a series of queries designed to identify cancer-specific patents and patent applications. This includes drugs, diagnostics, cell lines, mouse models, radiation-based devices, surgical devices, image analytics, data analytics, and genomic-based inventions.
> 
> “USPTO Cancer Moonshot Patent Data” by the USPTO, for public use. Frumkin, Jesse and Myers, Amanda F., Cancer Moonshot Patent Data (August, 2016).





| Stat | Value |
|----------|----------|
| Last updated | 2017-10-12 |
| Rows | 269,353 |
| Size | 91.6 MB |

### Schema
[View in BigQuery](https://bigquery.cloud.google.com/table/patents-public-data:uspto_oce_cancer.publications)

* `Family_ID` STRING   joins on **family_id**

* `Patent_or_Publication_ID` STRING   joins on **OCE Cancer id**

* `Application_Number` STRING  

* `Filing_Date` STRING  

* `Grant_or_Publication_Date` STRING  

* `CPC_Inventive` STRING  

* `CPC_Additional` STRING  

* `IPC_Primary` STRING  

* `IPC_Secondary` STRING  

* `USPC_Current_Original` STRING  

* `USPC_Current_Cross_Reference` STRING  

* `Patent_Title` STRING  

* `Drugs_and_Chemistry` STRING  

* `Diagnostic_and_Surgical_Devices` STRING  

* `Radiation_Measurement` STRING  

* `Data_Science` STRING  

* `Food_and_Nutrition` STRING  

* `Model_Systems_and_Animals` STRING  

* `Cells_and_Enzymes` STRING  

* `Other_and_Preclassification` STRING  

* `DNA_RNA_or_Protein_Sequence` STRING  

* `NIH_Federal_Grant_Number` STRING  

* `NIH_Grant_Recipient_Organization` STRING  

* `FDA_Application_Number` STRING  

* `FDA_Drug_Trade_Name` STRING  

* `FDA_Approval_Date` STRING  

* `FDA_Applicant` STRING  

* `FDA_Ingredient` STRING  

* `TBD` STRING  



### Join columns


#### Family_ID

joins to `patents-public-data:patents.publications::family_id` on **family_id** (99.05%, 266,792 rows)

| Key | Percent | Rows | Sample values |
|------|-----|--------|--------------------------------------------------------|
| `all` | 99.05% | 266,792 | `['38668948', '50101625', '27559695', '38801492', '27606978']` |


    #standardSQL
    SELECT
      COUNT(*) AS cnt,
      COUNT(second.second_column) AS second_cnt,
      ARRAY_AGG(first.Family_ID IGNORE NULLS ORDER BY RAND() LIMIT 5) AS sample_value
    FROM `patents-public-data.uspto_oce_cancer.publications`AS first
    LEFT JOIN (
      SELECT family_id AS second_column, COUNT(*) AS cnt
      FROM `patents-public-data.patents.publications`
      GROUP BY 1
    ) AS second ON first.Family_ID = second.second_column



joins from `patents-public-data:patents.publications::family_id` on **family_id** (1.07%, 1,047,661 rows)




#### Patent_or_Publication_ID

joins to `patents-public-data:uspto_oce_cancer.match::Patent_or_Publication_ID` on **OCE Cancer id** (100.00%, 269,353 rows)

| Key | Percent | Rows | Sample values |
|------|-----|--------|--------------------------------------------------------|
| `all` | 100.00% | 269,353 | `['US 8012966 B2', 'US 20160214964 A1', 'US 8632592 B2', 'US 5620971 A', 'US 20120028245 A1']` |


    #standardSQL
    SELECT
      COUNT(*) AS cnt,
      COUNT(second.second_column) AS second_cnt,
      ARRAY_AGG(first.Patent_or_Publication_ID IGNORE NULLS ORDER BY RAND() LIMIT 5) AS sample_value
    FROM `patents-public-data.uspto_oce_cancer.publications`AS first
    LEFT JOIN (
      SELECT Patent_or_Publication_ID AS second_column, COUNT(*) AS cnt
      FROM `patents-public-data.uspto_oce_cancer.match`
      GROUP BY 1
    ) AS second ON first.Patent_or_Publication_ID = second.second_column



joins from `patents-public-data:uspto_oce_cancer.match::Patent_or_Publication_ID` on **OCE Cancer id** (100.00%, 269,244 rows)




























































*****
## patents-public-data:uspto_oce_claims.match



> USPTO OCE Patent Claims Research data contains detailed information on claims from U.S. patents granted between 1976 and 2014 and U.S. patent applications published between 2001 and 2014.
> 
> "USPTO OCE Patent Claims Research Data" by the USPTO, for public use.
> Marco, Alan C. and Sarnoff, Joshua D. and deGrazia, Charles, "Patent Claims and Patent Scope" (October 2016). USPTO Economic Working Paper 2016-04.





| Stat | Value |
|----------|----------|
| Last updated | 2017-10-23 |
| Rows | 8,955,275 |
| Size | 258.6 MB |

### Schema
[View in BigQuery](https://bigquery.cloud.google.com/table/patents-public-data:uspto_oce_claims.match)

* `pub_no` STRING NULLABLE  joins on **OCE Claims pub_no**

* `pat_no` STRING NULLABLE  joins on **OCE Claims pat_no**

* `publication_number` STRING NULLABLE  joins on **publication_number**



### Join columns


#### pub_no

joins to `patents-public-data:uspto_oce_claims.pgpub_document_stats::pub_no` on **OCE Claims pub_no** (44.68%, 4,000,952 rows)

| Key | Percent | Rows | Sample values |
|------|-----|--------|--------------------------------------------------------|
| `all` | 44.68% | 4,000,952 | `['20140308265', '', '', '', '20070094868']` |


    #standardSQL
    SELECT
      COUNT(*) AS cnt,
      COUNT(second.second_column) AS second_cnt,
      ARRAY_AGG(first.pub_no IGNORE NULLS ORDER BY RAND() LIMIT 5) AS sample_value
    FROM `patents-public-data.uspto_oce_claims.match`AS first
    LEFT JOIN (
      SELECT pub_no AS second_column, COUNT(*) AS cnt
      FROM `patents-public-data.uspto_oce_claims.pgpub_document_stats`
      GROUP BY 1
    ) AS second ON first.pub_no = second.second_column



joins from `patents-public-data:uspto_oce_claims.pgpub_document_stats::pub_no` on **OCE Claims pub_no** (100.00%, 4,000,952 rows)




#### pat_no

joins to `patents-public-data:uspto_oce_claims.patent_document_stats::pat_no` on **OCE Claims pat_no** (55.32%, 4,954,323 rows)

| Key | Percent | Rows | Sample values |
|------|-----|--------|--------------------------------------------------------|
| `all` | 55.32% | 4,954,323 | `['', '', '7402901', '', '8254196']` |


    #standardSQL
    SELECT
      COUNT(*) AS cnt,
      COUNT(second.second_column) AS second_cnt,
      ARRAY_AGG(first.pat_no IGNORE NULLS ORDER BY RAND() LIMIT 5) AS sample_value
    FROM `patents-public-data.uspto_oce_claims.match`AS first
    LEFT JOIN (
      SELECT pat_no AS second_column, COUNT(*) AS cnt
      FROM `patents-public-data.uspto_oce_claims.patent_document_stats`
      GROUP BY 1
    ) AS second ON first.pat_no = second.second_column



joins from `patents-public-data:uspto_oce_claims.patent_document_stats::pat_no` on **OCE Claims pat_no** (100.00%, 4,954,323 rows)




#### publication_number

joins to `patents-public-data:patents.publications::publication_number` on **publication_number** (99.95%, 8,950,539 rows)

| Key | Percent | Rows | Sample values |
|------|-----|--------|--------------------------------------------------------|
| `all` | 99.95% | 8,950,539 | `['US-8653613-B2', 'US-2013140755-A1', 'US-8788397-B2', 'US-6076732-A', 'US-5562220-A']` |


    #standardSQL
    SELECT
      COUNT(*) AS cnt,
      COUNT(second.second_column) AS second_cnt,
      ARRAY_AGG(first.publication_number IGNORE NULLS ORDER BY RAND() LIMIT 5) AS sample_value
    FROM `patents-public-data.uspto_oce_claims.match`AS first
    LEFT JOIN (
      SELECT publication_number AS second_column, COUNT(*) AS cnt
      FROM `patents-public-data.patents.publications`
      GROUP BY 1
    ) AS second ON first.publication_number = second.second_column



joins from `patents-public-data:patents.publications::publication_number` on **publication_number** (9.12%, 8,950,539 rows)






*****
## patents-public-data:uspto_oce_claims.match_2014


Old table version `2014`, schema skipped.





*****
## patents-public-data:uspto_oce_claims.patent_claims_fulltext



> USPTO OCE Patent Claims Research data contains detailed information on claims from U.S. patents granted between 1976 and 2014 and U.S. patent applications published between 2001 and 2014.
> 
> "USPTO OCE Patent Claims Research Data" by the USPTO, for public use.
> Marco, Alan C. and Sarnoff, Joshua D. and deGrazia, Charles, "Patent Claims and Patent Scope" (October 2016). USPTO Economic Working Paper 2016-04.





| Stat | Value |
|----------|----------|
| Last updated | 2017-10-12 |
| Rows | 75,955,411 |
| Size | 31.6 GB |

### Schema
[View in BigQuery](https://bigquery.cloud.google.com/table/patents-public-data:uspto_oce_claims.patent_claims_fulltext)

* `pat_no` STRING  

* `claim_no` STRING  

* `claim_txt` STRING  

* `dependencies` STRING  

* `ind_flg` STRING  

* `appl_id` STRING  




















*****
## patents-public-data:uspto_oce_claims.patent_claims_fulltext_2014


Old table version `2014`, schema skipped.





*****
## patents-public-data:uspto_oce_claims.patent_claims_stats



> USPTO OCE Patent Claims Research data contains detailed information on claims from U.S. patents granted between 1976 and 2014 and U.S. patent applications published between 2001 and 2014.
> 
> "USPTO OCE Patent Claims Research Data" by the USPTO, for public use.
> Marco, Alan C. and Sarnoff, Joshua D. and deGrazia, Charles, "Patent Claims and Patent Scope" (October 2016). USPTO Economic Working Paper 2016-04.





| Stat | Value |
|----------|----------|
| Last updated | 2017-10-12 |
| Rows | 75,930,664 |
| Size | 3.3 GB |

### Schema
[View in BigQuery](https://bigquery.cloud.google.com/table/patents-public-data:uspto_oce_claims.patent_claims_stats)

* `pat_no` STRING  

* `claim_no` STRING  

* `word_ct` STRING  

* `char_ct` STRING  

* `or_ct` STRING  

* `sf_ct` STRING  

* `cns_ct` STRING  

* `ind_flg` STRING  

* `appl_id` STRING  


























*****
## patents-public-data:uspto_oce_claims.patent_claims_stats_2014


Old table version `2014`, schema skipped.





*****
## patents-public-data:uspto_oce_claims.patent_document_stats



> USPTO OCE Patent Claims Research data contains detailed information on claims from U.S. patents granted between 1976 and 2014 and U.S. patent applications published between 2001 and 2014.
> 
> "USPTO OCE Patent Claims Research Data" by the USPTO, for public use.
> Marco, Alan C. and Sarnoff, Joshua D. and deGrazia, Charles, "Patent Claims and Patent Scope" (October 2016). USPTO Economic Working Paper 2016-04.





| Stat | Value |
|----------|----------|
| Last updated | 2017-10-12 |
| Rows | 4,954,323 |
| Size | 285.3 MB |

### Schema
[View in BigQuery](https://bigquery.cloud.google.com/table/patents-public-data:uspto_oce_claims.patent_document_stats)

* `pat_no` STRING   joins on **OCE Claims pat_no**

* `pat_clm_ct` STRING  

* `pat_wrd_ct` STRING  

* `pat_wrd_min` STRING  

* `pat_dep_clm_ct` STRING  

* `pat_dep_wrd_ct` STRING  

* `pat_dep_wrd_min` STRING  

* `pat_wrd_avg` STRING  

* `pat_dep_wrd_avg` STRING  

* `appl_id` STRING  



### Join columns


#### pat_no

joins to `patents-public-data:uspto_oce_claims.match::pat_no` on **OCE Claims pat_no** (100.00%, 4,954,323 rows)

| Key | Percent | Rows | Sample values |
|------|-----|--------|--------------------------------------------------------|
| `all` | 100.00% | 4,954,323 | `['6891490', '6207374', '5372498', '7749500', '6389585']` |


    #standardSQL
    SELECT
      COUNT(*) AS cnt,
      COUNT(second.second_column) AS second_cnt,
      ARRAY_AGG(first.pat_no IGNORE NULLS ORDER BY RAND() LIMIT 5) AS sample_value
    FROM `patents-public-data.uspto_oce_claims.patent_document_stats`AS first
    LEFT JOIN (
      SELECT pat_no AS second_column, COUNT(*) AS cnt
      FROM `patents-public-data.uspto_oce_claims.match`
      GROUP BY 1
    ) AS second ON first.pat_no = second.second_column



joins from `patents-public-data:uspto_oce_claims.match::pat_no` on **OCE Claims pat_no** (55.32%, 4,954,323 rows)
























*****
## patents-public-data:uspto_oce_claims.patent_document_stats_2014


Old table version `2014`, schema skipped.





*****
## patents-public-data:uspto_oce_claims.pgpub_claims_fulltext



> USPTO OCE Patent Claims Research data contains detailed information on claims from U.S. patents granted between 1976 and 2014 and U.S. patent applications published between 2001 and 2014.
> 
> "USPTO OCE Patent Claims Research Data" by the USPTO, for public use.
> Marco, Alan C. and Sarnoff, Joshua D. and deGrazia, Charles, "Patent Claims and Patent Scope" (October 2016). USPTO Economic Working Paper 2016-04.





| Stat | Value |
|----------|----------|
| Last updated | 2017-10-12 |
| Rows | 82,017,562 |
| Size | 28.3 GB |

### Schema
[View in BigQuery](https://bigquery.cloud.google.com/table/patents-public-data:uspto_oce_claims.pgpub_claims_fulltext)

* `pub_no` STRING  

* `appl_id` STRING  

* `claim_no` STRING  

* `claim_txt` STRING  

* `dependencies` STRING  

* `ind_flg` STRING  




















*****
## patents-public-data:uspto_oce_claims.pgpub_claims_fulltext_2014


Old table version `2014`, schema skipped.





*****
## patents-public-data:uspto_oce_claims.pgpub_document_stats



> USPTO OCE Patent Claims Research data contains detailed information on claims from U.S. patents granted between 1976 and 2014 and U.S. patent applications published between 2001 and 2014.
> 
> "USPTO OCE Patent Claims Research Data" by the USPTO, for public use.
> Marco, Alan C. and Sarnoff, Joshua D. and deGrazia, Charles, "Patent Claims and Patent Scope" (October 2016). USPTO Economic Working Paper 2016-04.





| Stat | Value |
|----------|----------|
| Last updated | 2017-10-12 |
| Rows | 4,000,990 |
| Size | 251.5 MB |

### Schema
[View in BigQuery](https://bigquery.cloud.google.com/table/patents-public-data:uspto_oce_claims.pgpub_document_stats)

* `pub_no` STRING   joins on **OCE Claims pub_no**

* `appl_id` STRING  

* `pub_clm_ct` STRING  

* `pub_wrd_ct` STRING  

* `pub_wrd_min` STRING  

* `pub_dep_clm_ct` STRING  

* `pub_dep_wrd_ct` STRING  

* `pub_dep_wrd_min` STRING  

* `pub_wrd_avg` STRING  

* `pub_dep_wrd_avg` STRING  



### Join columns


#### pub_no

joins to `patents-public-data:uspto_oce_claims.match::pub_no` on **OCE Claims pub_no** (100.00%, 4,000,952 rows)

| Key | Percent | Rows | Sample values |
|------|-----|--------|--------------------------------------------------------|
| `all` | 100.00% | 4,000,952 | `['20120150695', '20140178863', '20090313741', '20130288400', '20020065150']` |


    #standardSQL
    SELECT
      COUNT(*) AS cnt,
      COUNT(second.second_column) AS second_cnt,
      ARRAY_AGG(first.pub_no IGNORE NULLS ORDER BY RAND() LIMIT 5) AS sample_value
    FROM `patents-public-data.uspto_oce_claims.pgpub_document_stats`AS first
    LEFT JOIN (
      SELECT pub_no AS second_column, COUNT(*) AS cnt
      FROM `patents-public-data.uspto_oce_claims.match`
      GROUP BY 1
    ) AS second ON first.pub_no = second.second_column



joins from `patents-public-data:uspto_oce_claims.match::pub_no` on **OCE Claims pub_no** (44.68%, 4,000,952 rows)
























*****
## patents-public-data:uspto_oce_claims.pgpub_document_stats_2014


Old table version `2014`, schema skipped.





*****
## patents-public-data:uspto_oce_litigation.attorneys



> USPTO OCE Patent Litigation Docket Reports Data contains detailed patent litigation data on 74,623 unique district court cases filed during the period 1963-2015.
> 
> "USPTO OCE Patent Litigation Docket Reports Data" by the USPTO, for public use.
> Marco, A., A. Tesfayesus, A. Toole (2017). “Patent Litigation Data from US District Court Electronic Records (1963-2015).” USPTO Economic Working Paper No. 2017-06.





| Stat | Value |
|----------|----------|
| Last updated | 2017-10-12 |
| Rows | 1,223,417 |
| Size | 214.4 MB |

### Schema
[View in BigQuery](https://bigquery.cloud.google.com/table/patents-public-data:uspto_oce_litigation.attorneys)

* `case_row_id` STRING  

* `case_number` STRING  

* `party_row_count` STRING  

* `party_type` STRING  

* `attorney_row_count` STRING  

* `name` STRING  

* `contactinfo` STRING  

* `position` STRING  
























*****
## patents-public-data:uspto_oce_litigation.attorneys_2015


Old table version `2015`, schema skipped.





*****
## patents-public-data:uspto_oce_litigation.cases



> USPTO OCE Patent Litigation Docket Reports Data contains detailed patent litigation data on 74,623 unique district court cases filed during the period 1963-2015.
> 
> "USPTO OCE Patent Litigation Docket Reports Data" by the USPTO, for public use.
> Marco, A., A. Tesfayesus, A. Toole (2017). “Patent Litigation Data from US District Court Electronic Records (1963-2015).” USPTO Economic Working Paper No. 2017-06.





| Stat | Value |
|----------|----------|
| Last updated | 2017-10-12 |
| Rows | 74,629 |
| Size | 17.7 MB |

### Schema
[View in BigQuery](https://bigquery.cloud.google.com/table/patents-public-data:uspto_oce_litigation.cases)

* `case_row_id` STRING  

* `case_number` STRING  

* `pacer_id` STRING  

* `case_name` STRING  

* `court_name` STRING  

* `assigned_to` STRING  

* `referred_to` STRING  

* `case_cause` STRING  

* `jurisdictional_basis` STRING  

* `demand` STRING  

* `jury_demand` STRING  

* `lead_case` STRING  

* `related_case` STRING  

* `settlement` STRING  

* `date_filed` STRING  

* `date_closed` STRING  

* `date_last_filed` STRING  










































*****
## patents-public-data:uspto_oce_litigation.cases_2015


Old table version `2015`, schema skipped.





*****
## patents-public-data:uspto_oce_litigation.documents



> USPTO OCE Patent Litigation Docket Reports Data contains detailed patent litigation data on 74,623 unique district court cases filed during the period 1963-2015.
> 
> "USPTO OCE Patent Litigation Docket Reports Data" by the USPTO, for public use.
> Marco, A., A. Tesfayesus, A. Toole (2017). “Patent Litigation Data from US District Court Electronic Records (1963-2015).” USPTO Economic Working Paper No. 2017-06.





| Stat | Value |
|----------|----------|
| Last updated | 2017-10-12 |
| Rows | 5,186,344 |
| Size | 1.4 GB |

### Schema
[View in BigQuery](https://bigquery.cloud.google.com/table/patents-public-data:uspto_oce_litigation.documents)

* `case_row_id` STRING  

* `case_number` STRING  

* `doc_count` STRING  

* `attachment` STRING  

* `date_filed` STRING  

* `long_description` STRING  

* `doc_number` STRING  

* `short_description` STRING  

* `upload_date` STRING  


























*****
## patents-public-data:uspto_oce_litigation.documents_2015


Old table version `2015`, schema skipped.





*****
## patents-public-data:uspto_oce_litigation.names



> USPTO OCE Patent Litigation Docket Reports Data contains detailed patent litigation data on 74,623 unique district court cases filed during the period 1963-2015.
> 
> "USPTO OCE Patent Litigation Docket Reports Data" by the USPTO, for public use.
> Marco, A., A. Tesfayesus, A. Toole (2017). “Patent Litigation Data from US District Court Electronic Records (1963-2015).” USPTO Economic Working Paper No. 2017-06.





| Stat | Value |
|----------|----------|
| Last updated | 2017-10-12 |
| Rows | 561,017 |
| Size | 44.9 MB |

### Schema
[View in BigQuery](https://bigquery.cloud.google.com/table/patents-public-data:uspto_oce_litigation.names)

* `case_row_id` STRING  

* `case_number` STRING  

* `party_row_count` STRING  

* `party_type` STRING  

* `name_row_count` STRING  

* `name` STRING  




















*****
## patents-public-data:uspto_oce_litigation.names_2015


Old table version `2015`, schema skipped.





*****
## patents-public-data:uspto_oce_litigation.pacer_cases



> USPTO OCE Patent Litigation Docket Reports Data contains detailed patent litigation data on 74,623 unique district court cases filed during the period 1963-2015.
> 
> "USPTO OCE Patent Litigation Docket Reports Data" by the USPTO, for public use.
> Marco, A., A. Tesfayesus, A. Toole (2017). “Patent Litigation Data from US District Court Electronic Records (1963-2015).” USPTO Economic Working Paper No. 2017-06.





| Stat | Value |
|----------|----------|
| Last updated | 2017-10-12 |
| Rows | 74,953 |
| Size | 9.9 MB |

### Schema
[View in BigQuery](https://bigquery.cloud.google.com/table/patents-public-data:uspto_oce_litigation.pacer_cases)

* `case_name` STRING  

* `court_code` STRING  

* `court_name` STRING  

* `date_closed` STRING  

* `case_number` STRING  

* `pacer_id` STRING  

* `date_filed` STRING  






















*****
## patents-public-data:uspto_oce_litigation.pacer_cases_2015


Old table version `2015`, schema skipped.





*****
## patents-public-data:uspto_oce_office_actions.citations



> The Office Action Research Dataset for Patents contains detailed information derived from the Office actions issued by patent examiners to applicants during the patent examination process. The “Office action” is a written notification to the applicant of the examiner’s decision on patentability and generally discloses the grounds for a rejection, the claims affected, and the pertinent prior art. This initial release consists of three files derived from 4.4 million Office actions mailed during the 2008 to mid-2017 period from USPTO examiners to the applicants of 2.2 million unique patent applications.
> 
> A working paper describing this dataset is available and can be cited as Lu, Qiang and Myers, Amanda F. and Beliveau, Scott, USPTO Patent Prosecution Research Data: Unlocking Office Action Traits (November 20, 2017). USPTO Economic Working Paper No. 2017-10. Available at SSRN: https://ssrn.com/abstract=3024621 (link is external).
> 
> This effort is made possible by the USPTO Digital Services & Big Data portfolio and collaboration with the USPTO Office of the Chief Economist (OCE). The OCE provides these data files for public use and encourages users to identify fixes and improvements. Please provide all feedback to: EconomicsData@uspto.gov.





| Stat | Value |
|----------|----------|
| Last updated | 2017-12-06 |
| Rows | 58,862,278 |
| Size | 2.7 GB |

### Schema
[View in BigQuery](https://bigquery.cloud.google.com/table/patents-public-data:uspto_oce_office_actions.citations)

* `app_id` STRING   joins on **OCE OA app_id**

* `citation_pat_pgpub_id` STRING  

* `parsed` STRING   joins on **OCE OA pub_id**

* `ifw_number` STRING  

* `action_type` STRING  

* `action_subtype` STRING  

* `form892` STRING  

* `form1449` STRING  

* `citation_in_oa` STRING  



### Join columns


#### app_id

joins to `patents-public-data:uspto_oce_office_actions.match_app::app_id` on **OCE OA app_id** (99.46%, 58,545,451 rows)

| Key | Percent | Rows | Sample values |
|------|-----|--------|--------------------------------------------------------|
| `all` | 99.46% | 58,545,451 | `['13979608', '13923133', '12729490', '13635105', '14218464']` |


    #standardSQL
    SELECT
      COUNT(*) AS cnt,
      COUNT(second.second_column) AS second_cnt,
      ARRAY_AGG(first.app_id IGNORE NULLS ORDER BY RAND() LIMIT 5) AS sample_value
    FROM `patents-public-data.uspto_oce_office_actions.citations`AS first
    LEFT JOIN (
      SELECT app_id AS second_column, COUNT(*) AS cnt
      FROM `patents-public-data.uspto_oce_office_actions.match_app`
      GROUP BY 1
    ) AS second ON first.app_id = second.second_column


joins to `patents-public-data:uspto_oce_office_actions.office_actions::app_id` on **OCE OA app_id** (99.46%, 58,545,451 rows)

| Key | Percent | Rows | Sample values |
|------|-----|--------|--------------------------------------------------------|
| `all` | 99.46% | 58,545,451 | `['12519016', '13039028', '14686893', '14662712', '12880949']` |


    #standardSQL
    SELECT
      COUNT(*) AS cnt,
      COUNT(second.second_column) AS second_cnt,
      ARRAY_AGG(first.app_id IGNORE NULLS ORDER BY RAND() LIMIT 5) AS sample_value
    FROM `patents-public-data.uspto_oce_office_actions.citations`AS first
    LEFT JOIN (
      SELECT app_id AS second_column, COUNT(*) AS cnt
      FROM `patents-public-data.uspto_oce_office_actions.office_actions`
      GROUP BY 1
    ) AS second ON first.app_id = second.second_column


joins to `patents-public-data:uspto_oce_office_actions.rejections::app_id` on **OCE OA app_id** (99.46%, 58,545,451 rows)

| Key | Percent | Rows | Sample values |
|------|-----|--------|--------------------------------------------------------|
| `all` | 99.46% | 58,545,451 | `['13400829', '14617574', '14477628', '12360738', '13174542']` |


    #standardSQL
    SELECT
      COUNT(*) AS cnt,
      COUNT(second.second_column) AS second_cnt,
      ARRAY_AGG(first.app_id IGNORE NULLS ORDER BY RAND() LIMIT 5) AS sample_value
    FROM `patents-public-data.uspto_oce_office_actions.citations`AS first
    LEFT JOIN (
      SELECT app_id AS second_column, COUNT(*) AS cnt
      FROM `patents-public-data.uspto_oce_office_actions.rejections`
      GROUP BY 1
    ) AS second ON first.app_id = second.second_column



joins from `patents-public-data:uspto_oce_office_actions.match_app::app_id` on **OCE OA app_id** (98.55%, 2,156,513 rows)

joins from `patents-public-data:uspto_oce_office_actions.office_actions::app_id` on **OCE OA app_id** (99.03%, 4,342,080 rows)

joins from `patents-public-data:uspto_oce_office_actions.rejections::app_id` on **OCE OA app_id** (99.04%, 10,036,303 rows)






#### parsed

joins to `patents-public-data:uspto_oce_office_actions.match_pub::parsed` on **OCE OA pub_id** (99.35%, 58,477,933 rows)

| Key | Percent | Rows | Sample values |
|------|-----|--------|--------------------------------------------------------|
| `all` | 99.35% | 58,477,933 | `['20110059422', '20030055619', '20020065907', '7659971', '20120041673']` |


    #standardSQL
    SELECT
      COUNT(*) AS cnt,
      COUNT(second.second_column) AS second_cnt,
      ARRAY_AGG(first.parsed IGNORE NULLS ORDER BY RAND() LIMIT 5) AS sample_value
    FROM `patents-public-data.uspto_oce_office_actions.citations`AS first
    LEFT JOIN (
      SELECT parsed AS second_column, COUNT(*) AS cnt
      FROM `patents-public-data.uspto_oce_office_actions.match_pub`
      GROUP BY 1
    ) AS second ON first.parsed = second.second_column



joins from `patents-public-data:uspto_oce_office_actions.match_pub::parsed` on **OCE OA pub_id** (100.00%, 7,547,458 rows)


















*****
## patents-public-data:uspto_oce_office_actions.match_app



> The Office Action Research Dataset for Patents contains detailed information derived from the Office actions issued by patent examiners to applicants during the patent examination process. The “Office action” is a written notification to the applicant of the examiner’s decision on patentability and generally discloses the grounds for a rejection, the claims affected, and the pertinent prior art. This initial release consists of three files derived from 4.4 million Office actions mailed during the 2008 to mid-2017 period from USPTO examiners to the applicants of 2.2 million unique patent applications.
> 
> A working paper describing this dataset is available and can be cited as Lu, Qiang and Myers, Amanda F. and Beliveau, Scott, USPTO Patent Prosecution Research Data: Unlocking Office Action Traits (November 20, 2017). USPTO Economic Working Paper No. 2017-10. Available at SSRN: https://ssrn.com/abstract=3024621 (link is external).
> 
> This effort is made possible by the USPTO Digital Services & Big Data portfolio and collaboration with the USPTO Office of the Chief Economist (OCE). The OCE provides these data files for public use and encourages users to identify fixes and improvements. Please provide all feedback to: EconomicsData@uspto.gov.





| Stat | Value |
|----------|----------|
| Last updated | 2017-12-06 |
| Rows | 2,188,195 |
| Size | 60.4 MB |

### Schema
[View in BigQuery](https://bigquery.cloud.google.com/table/patents-public-data:uspto_oce_office_actions.match_app)

* `app_id` STRING NULLABLE  joins on **OCE OA app_id**

* `application_number` STRING NULLABLE  joins on **application_number**



### Join columns


#### app_id

joins to `patents-public-data:uspto_oce_office_actions.citations::app_id` on **OCE OA app_id** (98.55%, 2,156,513 rows)

| Key | Percent | Rows | Sample values |
|------|-----|--------|--------------------------------------------------------|
| `all` | 98.55% | 2,156,513 | `['13586532', '13690256', '12432671', '13944913', '13414382']` |


    #standardSQL
    SELECT
      COUNT(*) AS cnt,
      COUNT(second.second_column) AS second_cnt,
      ARRAY_AGG(first.app_id IGNORE NULLS ORDER BY RAND() LIMIT 5) AS sample_value
    FROM `patents-public-data.uspto_oce_office_actions.match_app`AS first
    LEFT JOIN (
      SELECT app_id AS second_column, COUNT(*) AS cnt
      FROM `patents-public-data.uspto_oce_office_actions.citations`
      GROUP BY 1
    ) AS second ON first.app_id = second.second_column


joins to `patents-public-data:uspto_oce_office_actions.office_actions::app_id` on **OCE OA app_id** (100.00%, 2,188,195 rows)

| Key | Percent | Rows | Sample values |
|------|-----|--------|--------------------------------------------------------|
| `all` | 100.00% | 2,188,195 | `['13668165', '13265829', '14520062', '14800161', '14894592']` |


    #standardSQL
    SELECT
      COUNT(*) AS cnt,
      COUNT(second.second_column) AS second_cnt,
      ARRAY_AGG(first.app_id IGNORE NULLS ORDER BY RAND() LIMIT 5) AS sample_value
    FROM `patents-public-data.uspto_oce_office_actions.match_app`AS first
    LEFT JOIN (
      SELECT app_id AS second_column, COUNT(*) AS cnt
      FROM `patents-public-data.uspto_oce_office_actions.office_actions`
      GROUP BY 1
    ) AS second ON first.app_id = second.second_column


joins to `patents-public-data:uspto_oce_office_actions.rejections::app_id` on **OCE OA app_id** (100.00%, 2,188,195 rows)

| Key | Percent | Rows | Sample values |
|------|-----|--------|--------------------------------------------------------|
| `all` | 100.00% | 2,188,195 | `['14224520', '13876889', '13570477', '14099771', '13793838']` |


    #standardSQL
    SELECT
      COUNT(*) AS cnt,
      COUNT(second.second_column) AS second_cnt,
      ARRAY_AGG(first.app_id IGNORE NULLS ORDER BY RAND() LIMIT 5) AS sample_value
    FROM `patents-public-data.uspto_oce_office_actions.match_app`AS first
    LEFT JOIN (
      SELECT app_id AS second_column, COUNT(*) AS cnt
      FROM `patents-public-data.uspto_oce_office_actions.rejections`
      GROUP BY 1
    ) AS second ON first.app_id = second.second_column



joins from `patents-public-data:uspto_oce_office_actions.citations::app_id` on **OCE OA app_id** (99.46%, 58,545,451 rows)

joins from `patents-public-data:uspto_oce_office_actions.office_actions::app_id` on **OCE OA app_id** (100.00%, 4,384,532 rows)

joins from `patents-public-data:uspto_oce_office_actions.rejections::app_id` on **OCE OA app_id** (100.00%, 10,133,179 rows)




#### application_number

joins to `patents-public-data:patents.publications::application_number` on **application_number** (99.80%, 2,183,770 rows)

| Key | Percent | Rows | Sample values |
|------|-----|--------|--------------------------------------------------------|
| `all` | 99.80% | 2,183,770 | `['US-201414579396-A', 'US-47277609-A', 'US-201213534241-A', 'US-5834908-A', 'US-201314044354-A']` |


    #standardSQL
    SELECT
      COUNT(*) AS cnt,
      COUNT(second.second_column) AS second_cnt,
      ARRAY_AGG(first.application_number IGNORE NULLS ORDER BY RAND() LIMIT 5) AS sample_value
    FROM `patents-public-data.uspto_oce_office_actions.match_app`AS first
    LEFT JOIN (
      SELECT application_number AS second_column, COUNT(*) AS cnt
      FROM `patents-public-data.patents.publications`
      GROUP BY 1
    ) AS second ON first.application_number = second.second_column



joins from `patents-public-data:patents.publications::application_number` on **application_number** (3.62%, 3,555,089 rows)






*****
## patents-public-data:uspto_oce_office_actions.match_pub



> The Office Action Research Dataset for Patents contains detailed information derived from the Office actions issued by patent examiners to applicants during the patent examination process. The “Office action” is a written notification to the applicant of the examiner’s decision on patentability and generally discloses the grounds for a rejection, the claims affected, and the pertinent prior art. This initial release consists of three files derived from 4.4 million Office actions mailed during the 2008 to mid-2017 period from USPTO examiners to the applicants of 2.2 million unique patent applications.
> 
> A working paper describing this dataset is available and can be cited as Lu, Qiang and Myers, Amanda F. and Beliveau, Scott, USPTO Patent Prosecution Research Data: Unlocking Office Action Traits (November 20, 2017). USPTO Economic Working Paper No. 2017-10. Available at SSRN: https://ssrn.com/abstract=3024621 (link is external).
> 
> This effort is made possible by the USPTO Digital Services & Big Data portfolio and collaboration with the USPTO Office of the Chief Economist (OCE). The OCE provides these data files for public use and encourages users to identify fixes and improvements. Please provide all feedback to: EconomicsData@uspto.gov.





| Stat | Value |
|----------|----------|
| Last updated | 2017-12-06 |
| Rows | 7,547,458 |
| Size | 197.0 MB |

### Schema
[View in BigQuery](https://bigquery.cloud.google.com/table/patents-public-data:uspto_oce_office_actions.match_pub)

* `parsed` STRING NULLABLE  joins on **OCE OA pub_id**

* `publication_number` STRING NULLABLE 



### Join columns


#### parsed

joins to `patents-public-data:uspto_oce_office_actions.citations::parsed` on **OCE OA pub_id** (100.00%, 7,547,458 rows)

| Key | Percent | Rows | Sample values |
|------|-----|--------|--------------------------------------------------------|
| `all` | 100.00% | 7,547,458 | `['3727953', '6533845', '2875312', '8118645', '8449785']` |


    #standardSQL
    SELECT
      COUNT(*) AS cnt,
      COUNT(second.second_column) AS second_cnt,
      ARRAY_AGG(first.parsed IGNORE NULLS ORDER BY RAND() LIMIT 5) AS sample_value
    FROM `patents-public-data.uspto_oce_office_actions.match_pub`AS first
    LEFT JOIN (
      SELECT parsed AS second_column, COUNT(*) AS cnt
      FROM `patents-public-data.uspto_oce_office_actions.citations`
      GROUP BY 1
    ) AS second ON first.parsed = second.second_column



joins from `patents-public-data:uspto_oce_office_actions.citations::parsed` on **OCE OA pub_id** (99.35%, 58,477,933 rows)








*****
## patents-public-data:uspto_oce_office_actions.office_actions



> The Office Action Research Dataset for Patents contains detailed information derived from the Office actions issued by patent examiners to applicants during the patent examination process. The “Office action” is a written notification to the applicant of the examiner’s decision on patentability and generally discloses the grounds for a rejection, the claims affected, and the pertinent prior art. This initial release consists of three files derived from 4.4 million Office actions mailed during the 2008 to mid-2017 period from USPTO examiners to the applicants of 2.2 million unique patent applications.
> 
> A working paper describing this dataset is available and can be cited as Lu, Qiang and Myers, Amanda F. and Beliveau, Scott, USPTO Patent Prosecution Research Data: Unlocking Office Action Traits (November 20, 2017). USPTO Economic Working Paper No. 2017-10. Available at SSRN: https://ssrn.com/abstract=3024621 (link is external).
> 
> This effort is made possible by the USPTO Digital Services & Big Data portfolio and collaboration with the USPTO Office of the Chief Economist (OCE). The OCE provides these data files for public use and encourages users to identify fixes and improvements. Please provide all feedback to: EconomicsData@uspto.gov.





| Stat | Value |
|----------|----------|
| Last updated | 2017-12-06 |
| Rows | 4,384,532 |
| Size | 490.4 MB |

### Schema
[View in BigQuery](https://bigquery.cloud.google.com/table/patents-public-data:uspto_oce_office_actions.office_actions)

* `app_id` STRING   joins on **OCE OA app_id**

* `ifw_number` STRING  

* `document_cd` STRING  

* `mail_dt` STRING  

* `art_unit` STRING  

* `uspc_class` STRING  

* `uspc_subclass` STRING  

* `header_missing` STRING  

* `fp_missing` STRING  

* `rejection_fp_mismatch` STRING  

* `closing_missing` STRING  

* `rejection_101` STRING  

* `rejection_102` STRING  

* `rejection_103` STRING  

* `rejection_112` STRING  

* `rejection_dp` STRING  

* `objection` STRING  

* `allowed_claims` STRING  

* `cite102_gt1` STRING  

* `cite103_gt3` STRING  

* `cite103_eq1` STRING  

* `cite103_max` STRING  

* `signature_type` STRING  



### Join columns


#### app_id

joins to `patents-public-data:uspto_oce_office_actions.match_app::app_id` on **OCE OA app_id** (100.00%, 4,384,532 rows)

| Key | Percent | Rows | Sample values |
|------|-----|--------|--------------------------------------------------------|
| `all` | 100.00% | 4,384,532 | `['12136988', '13827446', '12438429', '13288647', '14801848']` |


    #standardSQL
    SELECT
      COUNT(*) AS cnt,
      COUNT(second.second_column) AS second_cnt,
      ARRAY_AGG(first.app_id IGNORE NULLS ORDER BY RAND() LIMIT 5) AS sample_value
    FROM `patents-public-data.uspto_oce_office_actions.office_actions`AS first
    LEFT JOIN (
      SELECT app_id AS second_column, COUNT(*) AS cnt
      FROM `patents-public-data.uspto_oce_office_actions.match_app`
      GROUP BY 1
    ) AS second ON first.app_id = second.second_column


joins to `patents-public-data:uspto_oce_office_actions.citations::app_id` on **OCE OA app_id** (99.03%, 4,342,080 rows)

| Key | Percent | Rows | Sample values |
|------|-----|--------|--------------------------------------------------------|
| `all` | 99.03% | 4,342,080 | `['12091669', '14475290', '14274413', '12777261', '13974079']` |


    #standardSQL
    SELECT
      COUNT(*) AS cnt,
      COUNT(second.second_column) AS second_cnt,
      ARRAY_AGG(first.app_id IGNORE NULLS ORDER BY RAND() LIMIT 5) AS sample_value
    FROM `patents-public-data.uspto_oce_office_actions.office_actions`AS first
    LEFT JOIN (
      SELECT app_id AS second_column, COUNT(*) AS cnt
      FROM `patents-public-data.uspto_oce_office_actions.citations`
      GROUP BY 1
    ) AS second ON first.app_id = second.second_column


joins to `patents-public-data:uspto_oce_office_actions.rejections::app_id` on **OCE OA app_id** (100.00%, 4,384,532 rows)

| Key | Percent | Rows | Sample values |
|------|-----|--------|--------------------------------------------------------|
| `all` | 100.00% | 4,384,532 | `['12683218', '14899516', '14426381', '13426526', '12576050']` |


    #standardSQL
    SELECT
      COUNT(*) AS cnt,
      COUNT(second.second_column) AS second_cnt,
      ARRAY_AGG(first.app_id IGNORE NULLS ORDER BY RAND() LIMIT 5) AS sample_value
    FROM `patents-public-data.uspto_oce_office_actions.office_actions`AS first
    LEFT JOIN (
      SELECT app_id AS second_column, COUNT(*) AS cnt
      FROM `patents-public-data.uspto_oce_office_actions.rejections`
      GROUP BY 1
    ) AS second ON first.app_id = second.second_column



joins from `patents-public-data:uspto_oce_office_actions.match_app::app_id` on **OCE OA app_id** (100.00%, 2,188,195 rows)

joins from `patents-public-data:uspto_oce_office_actions.citations::app_id` on **OCE OA app_id** (99.46%, 58,545,451 rows)

joins from `patents-public-data:uspto_oce_office_actions.rejections::app_id` on **OCE OA app_id** (100.00%, 10,133,179 rows)


















































*****
## patents-public-data:uspto_oce_office_actions.rejections



> The Office Action Research Dataset for Patents contains detailed information derived from the Office actions issued by patent examiners to applicants during the patent examination process. The “Office action” is a written notification to the applicant of the examiner’s decision on patentability and generally discloses the grounds for a rejection, the claims affected, and the pertinent prior art. This initial release consists of three files derived from 4.4 million Office actions mailed during the 2008 to mid-2017 period from USPTO examiners to the applicants of 2.2 million unique patent applications.
> 
> A working paper describing this dataset is available and can be cited as Lu, Qiang and Myers, Amanda F. and Beliveau, Scott, USPTO Patent Prosecution Research Data: Unlocking Office Action Traits (November 20, 2017). USPTO Economic Working Paper No. 2017-10. Available at SSRN: https://ssrn.com/abstract=3024621 (link is external).
> 
> This effort is made possible by the USPTO Digital Services & Big Data portfolio and collaboration with the USPTO Office of the Chief Economist (OCE). The OCE provides these data files for public use and encourages users to identify fixes and improvements. Please provide all feedback to: EconomicsData@uspto.gov.





| Stat | Value |
|----------|----------|
| Last updated | 2017-12-06 |
| Rows | 10,133,179 |
| Size | 763.2 MB |

### Schema
[View in BigQuery](https://bigquery.cloud.google.com/table/patents-public-data:uspto_oce_office_actions.rejections)

* `app_id` STRING   joins on **OCE OA app_id**

* `ifw_number` STRING  

* `action_type` STRING  

* `action_subtype` STRING  

* `claim_numbers` STRING  

* `alice_in` STRING  

* `bilski_in` STRING  

* `mayo_in` STRING  

* `myriad_in` STRING  



### Join columns


#### app_id

joins to `patents-public-data:uspto_oce_office_actions.match_app::app_id` on **OCE OA app_id** (100.00%, 10,133,179 rows)

| Key | Percent | Rows | Sample values |
|------|-----|--------|--------------------------------------------------------|
| `all` | 100.00% | 10,133,179 | `['13905975', '12151211', '12661909', '15015613', '12123920']` |


    #standardSQL
    SELECT
      COUNT(*) AS cnt,
      COUNT(second.second_column) AS second_cnt,
      ARRAY_AGG(first.app_id IGNORE NULLS ORDER BY RAND() LIMIT 5) AS sample_value
    FROM `patents-public-data.uspto_oce_office_actions.rejections`AS first
    LEFT JOIN (
      SELECT app_id AS second_column, COUNT(*) AS cnt
      FROM `patents-public-data.uspto_oce_office_actions.match_app`
      GROUP BY 1
    ) AS second ON first.app_id = second.second_column


joins to `patents-public-data:uspto_oce_office_actions.citations::app_id` on **OCE OA app_id** (99.04%, 10,036,303 rows)

| Key | Percent | Rows | Sample values |
|------|-----|--------|--------------------------------------------------------|
| `all` | 99.04% | 10,036,303 | `['12765824', '12507639', '13290107', '13686749', '14797829']` |


    #standardSQL
    SELECT
      COUNT(*) AS cnt,
      COUNT(second.second_column) AS second_cnt,
      ARRAY_AGG(first.app_id IGNORE NULLS ORDER BY RAND() LIMIT 5) AS sample_value
    FROM `patents-public-data.uspto_oce_office_actions.rejections`AS first
    LEFT JOIN (
      SELECT app_id AS second_column, COUNT(*) AS cnt
      FROM `patents-public-data.uspto_oce_office_actions.citations`
      GROUP BY 1
    ) AS second ON first.app_id = second.second_column


joins to `patents-public-data:uspto_oce_office_actions.office_actions::app_id` on **OCE OA app_id** (100.00%, 10,133,179 rows)

| Key | Percent | Rows | Sample values |
|------|-----|--------|--------------------------------------------------------|
| `all` | 100.00% | 10,133,179 | `['13603783', '14178681', '12469121', '14187472', '13531058']` |


    #standardSQL
    SELECT
      COUNT(*) AS cnt,
      COUNT(second.second_column) AS second_cnt,
      ARRAY_AGG(first.app_id IGNORE NULLS ORDER BY RAND() LIMIT 5) AS sample_value
    FROM `patents-public-data.uspto_oce_office_actions.rejections`AS first
    LEFT JOIN (
      SELECT app_id AS second_column, COUNT(*) AS cnt
      FROM `patents-public-data.uspto_oce_office_actions.office_actions`
      GROUP BY 1
    ) AS second ON first.app_id = second.second_column



joins from `patents-public-data:uspto_oce_office_actions.match_app::app_id` on **OCE OA app_id** (100.00%, 2,188,195 rows)

joins from `patents-public-data:uspto_oce_office_actions.citations::app_id` on **OCE OA app_id** (99.46%, 58,545,451 rows)

joins from `patents-public-data:uspto_oce_office_actions.office_actions::app_id` on **OCE OA app_id** (100.00%, 4,384,532 rows)






















*****
## patents-public-data:uspto_oce_pair.all_inventors



> USPTO Patent Examination Research Data (PatEx) contains detailed information on millions of publicly viewable patent applications filed with the USPTO. The data are sourced from the Public Patent Application Information Retrieval system (Public PAIR).
> 
> “USPTO Patent Examination Research Dataset” by the USPTO, for public use.
> Graham, S. Marco, A., and Miller, A. (2015). “The USPTO Patent Examination Research Dataset: A Window on the Process of Patent Examination.”





| Stat | Value |
|----------|----------|
| Last updated | 2017-10-12 |
| Rows | 26,673,121 |
| Size | 1.5 GB |

### Schema
[View in BigQuery](https://bigquery.cloud.google.com/table/patents-public-data:uspto_oce_pair.all_inventors)

* `application_number` STRING  

* `inventor_name_first` STRING  

* `inventor_name_middle` STRING  

* `inventor_name_last` STRING  

* `inventor_rank` STRING  

* `inventor_region_code` STRING  

* `inventor_country_code` STRING  

* `inventor_country_name` STRING  

* `inventor_address_type` STRING  


























*****
## patents-public-data:uspto_oce_pair.all_inventors_2015


Old table version `2015`, schema skipped.





*****
## patents-public-data:uspto_oce_pair.application_data



> USPTO Patent Examination Research Data (PatEx) contains detailed information on millions of publicly viewable patent applications filed with the USPTO. The data are sourced from the Public Patent Application Information Retrieval system (Public PAIR).
> 
> “USPTO Patent Examination Research Dataset” by the USPTO, for public use.
> Graham, S. Marco, A., and Miller, A. (2015). “The USPTO Patent Examination Research Dataset: A Window on the Process of Patent Examination.”





| Stat | Value |
|----------|----------|
| Last updated | 2017-10-12 |
| Rows | 9,817,693 |
| Size | 2.3 GB |

### Schema
[View in BigQuery](https://bigquery.cloud.google.com/table/patents-public-data:uspto_oce_pair.application_data)

* `application_number` STRING   joins on **OCE PAIR app_num**

* `filing_date` STRING  

* `invention_subject_matter` STRING  

* `application_type` STRING  

* `examiner_name_last` STRING  

* `examiner_name_first` STRING  

* `examiner_name_middle` STRING  

* `examiner_id` STRING  

* `examiner_art_unit` STRING  

* `uspc_class` STRING  

* `uspc_subclass` STRING  

* `confirm_number` STRING  

* `customer_number` STRING  

* `atty_docket_number` STRING  

* `appl_status_code` STRING  

* `appl_status_date` STRING  

* `file_location` STRING  

* `file_location_date` STRING  

* `earliest_pgpub_number` STRING  

* `earliest_pgpub_date` STRING  

* `wipo_pub_number` STRING  

* `wipo_pub_date` STRING  

* `patent_number` STRING  

* `patent_issue_date` STRING  

* `abandon_date` STRING  

* `disposal_type` STRING  

* `invention_title` STRING  

* `small_entity_indicator` STRING  

* `aia_first_to_file` STRING  



### Join columns


#### application_number

joins to `patents-public-data:uspto_oce_pair.match::application_number_pair` on **OCE PAIR app_num** (85.95%, 8,438,063 rows)

| Key | Percent | Rows | Sample values |
|------|-----|--------|--------------------------------------------------------|
| `all` | 85.95% | 8,438,063 | `['07955102', '14143090', '13785658', '12429026', '08908593']` |


    #standardSQL
    SELECT
      COUNT(*) AS cnt,
      COUNT(second.second_column) AS second_cnt,
      ARRAY_AGG(first.application_number IGNORE NULLS ORDER BY RAND() LIMIT 5) AS sample_value
    FROM `patents-public-data.uspto_oce_pair.application_data`AS first
    LEFT JOIN (
      SELECT application_number_pair AS second_column, COUNT(*) AS cnt
      FROM `patents-public-data.uspto_oce_pair.match`
      GROUP BY 1
    ) AS second ON first.application_number = second.second_column



joins from `patents-public-data:uspto_oce_pair.match::application_number_pair` on **OCE PAIR app_num** (100.00%, 8,438,063 rows)






























































*****
## patents-public-data:uspto_oce_pair.application_data_2015


Old table version `2015`, schema skipped.





*****
## patents-public-data:uspto_oce_pair.continuity_children



> USPTO Patent Examination Research Data (PatEx) contains detailed information on millions of publicly viewable patent applications filed with the USPTO. The data are sourced from the Public Patent Application Information Retrieval system (Public PAIR).
> 
> “USPTO Patent Examination Research Dataset” by the USPTO, for public use.
> Graham, S. Marco, A., and Miller, A. (2015). “The USPTO Patent Examination Research Dataset: A Window on the Process of Patent Examination.”





| Stat | Value |
|----------|----------|
| Last updated | 2017-10-12 |
| Rows | 5,580,744 |
| Size | 213.1 MB |

### Schema
[View in BigQuery](https://bigquery.cloud.google.com/table/patents-public-data:uspto_oce_pair.continuity_children)

* `application_number` STRING  

* `child_application_number` STRING  

* `child_filing_date` STRING  

* `continuation_type` STRING  
















*****
## patents-public-data:uspto_oce_pair.continuity_children_2015


Old table version `2015`, schema skipped.





*****
## patents-public-data:uspto_oce_pair.continuity_parents



> USPTO Patent Examination Research Data (PatEx) contains detailed information on millions of publicly viewable patent applications filed with the USPTO. The data are sourced from the Public Patent Application Information Retrieval system (Public PAIR).
> 
> “USPTO Patent Examination Research Dataset” by the USPTO, for public use.
> Graham, S. Marco, A., and Miller, A. (2015). “The USPTO Patent Examination Research Dataset: A Window on the Process of Patent Examination.”





| Stat | Value |
|----------|----------|
| Last updated | 2017-10-12 |
| Rows | 6,618,673 |
| Size | 259.6 MB |

### Schema
[View in BigQuery](https://bigquery.cloud.google.com/table/patents-public-data:uspto_oce_pair.continuity_parents)

* `application_number` STRING  

* `parent_application_number` STRING  

* `parent_filing_date` STRING  

* `continuation_type` STRING  
















*****
## patents-public-data:uspto_oce_pair.continuity_parents_2015


Old table version `2015`, schema skipped.





*****
## patents-public-data:uspto_oce_pair.correspondence_address



> USPTO Patent Examination Research Data (PatEx) contains detailed information on millions of publicly viewable patent applications filed with the USPTO. The data are sourced from the Public Patent Application Information Retrieval system (Public PAIR).
> 
> “USPTO Patent Examination Research Dataset” by the USPTO, for public use.
> Graham, S. Marco, A., and Miller, A. (2015). “The USPTO Patent Examination Research Dataset: A Window on the Process of Patent Examination.”





| Stat | Value |
|----------|----------|
| Last updated | 2017-10-12 |
| Rows | 9,306,818 |
| Size | 1.1 GB |

### Schema
[View in BigQuery](https://bigquery.cloud.google.com/table/patents-public-data:uspto_oce_pair.correspondence_address)

* `application_number` STRING  

* `correspondence_name_line_1` STRING  

* `correspondence_name_line_2` STRING  

* `correspondence_street_line_1` STRING  

* `correspondence_street_line_2` STRING  

* `correspondence_city` STRING  

* `correspondence_postal_code` STRING  

* `correspondence_region_code` STRING  

* `correspondence_region_name` STRING  

* `correspondence_country_code` STRING  

* `correspondence_country_name` STRING  

* `customer_number` STRING  
































*****
## patents-public-data:uspto_oce_pair.correspondence_address_2015


Old table version `2015`, schema skipped.





*****
## patents-public-data:uspto_oce_pair.event_codes



> USPTO Patent Examination Research Data (PatEx) contains detailed information on millions of publicly viewable patent applications filed with the USPTO. The data are sourced from the Public Patent Application Information Retrieval system (Public PAIR).
> 
> “USPTO Patent Examination Research Dataset” by the USPTO, for public use.
> Graham, S. Marco, A., and Miller, A. (2015). “The USPTO Patent Examination Research Dataset: A Window on the Process of Patent Examination.”





| Stat | Value |
|----------|----------|
| Last updated | 2017-10-12 |
| Rows | 1,983 |
| Size | 88.2 kB |

### Schema
[View in BigQuery](https://bigquery.cloud.google.com/table/patents-public-data:uspto_oce_pair.event_codes)

* `event_code` STRING  

* `event_description` STRING  












*****
## patents-public-data:uspto_oce_pair.event_codes_2015


Old table version `2015`, schema skipped.





*****
## patents-public-data:uspto_oce_pair.foreign_priority



> USPTO Patent Examination Research Data (PatEx) contains detailed information on millions of publicly viewable patent applications filed with the USPTO. The data are sourced from the Public Patent Application Information Retrieval system (Public PAIR).
> 
> “USPTO Patent Examination Research Dataset” by the USPTO, for public use.
> Graham, S. Marco, A., and Miller, A. (2015). “The USPTO Patent Examination Research Dataset: A Window on the Process of Patent Examination.”





| Stat | Value |
|----------|----------|
| Last updated | 2017-10-12 |
| Rows | 4,001,307 |
| Size | 199.3 MB |

### Schema
[View in BigQuery](https://bigquery.cloud.google.com/table/patents-public-data:uspto_oce_pair.foreign_priority)

* `application_number` STRING  

* `foreign_parent_id` STRING  

* `foreign_parent_date` STRING  

* `parent_country_code` STRING  

* `parent_country` STRING  


















*****
## patents-public-data:uspto_oce_pair.foreign_priority_2015


Old table version `2015`, schema skipped.





*****
## patents-public-data:uspto_oce_pair.match



> USPTO Patent Examination Research Data (PatEx) contains detailed information on millions of publicly viewable patent applications filed with the USPTO. The data are sourced from the Public Patent Application Information Retrieval system (Public PAIR).
> 
> “USPTO Patent Examination Research Dataset” by the USPTO, for public use.
> Graham, S. Marco, A., and Miller, A. (2015). “The USPTO Patent Examination Research Dataset: A Window on the Process of Patent Examination.”





| Stat | Value |
|----------|----------|
| Last updated | 2017-10-23 |
| Rows | 8,438,063 |
| Size | 223.1 MB |

### Schema
[View in BigQuery](https://bigquery.cloud.google.com/table/patents-public-data:uspto_oce_pair.match)

* `application_number_pair` STRING NULLABLE  joins on **OCE PAIR app_num**

* `application_number` STRING NULLABLE  joins on **application_number**



### Join columns


#### application_number_pair

joins to `patents-public-data:uspto_oce_pair.application_data::application_number` on **OCE PAIR app_num** (100.00%, 8,438,063 rows)

| Key | Percent | Rows | Sample values |
|------|-----|--------|--------------------------------------------------------|
| `all` | 100.00% | 8,438,063 | `['09337997', '11113306', 'PCT/US01/04923', '09403019', 'PCT/US10/38796']` |


    #standardSQL
    SELECT
      COUNT(*) AS cnt,
      COUNT(second.second_column) AS second_cnt,
      ARRAY_AGG(first.application_number_pair IGNORE NULLS ORDER BY RAND() LIMIT 5) AS sample_value
    FROM `patents-public-data.uspto_oce_pair.match`AS first
    LEFT JOIN (
      SELECT application_number AS second_column, COUNT(*) AS cnt
      FROM `patents-public-data.uspto_oce_pair.application_data`
      GROUP BY 1
    ) AS second ON first.application_number_pair = second.second_column



joins from `patents-public-data:uspto_oce_pair.application_data::application_number` on **OCE PAIR app_num** (85.95%, 8,438,063 rows)




#### application_number

joins to `patents-public-data:patents.publications::application_number` on **application_number** (100.00%, 8,437,907 rows)

| Key | Percent | Rows | Sample values |
|------|-----|--------|--------------------------------------------------------|
| `all` | 100.00% | 8,437,907 | `['US-2005029746-W', 'US-201514622664-A', 'US-201113810864-A', 'US-78529204-A', 'US-76099910-A']` |


    #standardSQL
    SELECT
      COUNT(*) AS cnt,
      COUNT(second.second_column) AS second_cnt,
      ARRAY_AGG(first.application_number IGNORE NULLS ORDER BY RAND() LIMIT 5) AS sample_value
    FROM `patents-public-data.uspto_oce_pair.match`AS first
    LEFT JOIN (
      SELECT application_number AS second_column, COUNT(*) AS cnt
      FROM `patents-public-data.patents.publications`
      GROUP BY 1
    ) AS second ON first.application_number = second.second_column



joins from `patents-public-data:patents.publications::application_number` on **application_number** (11.95%, 11,727,859 rows)






*****
## patents-public-data:uspto_oce_pair.match_2015


Old table version `2015`, schema skipped.





*****
## patents-public-data:uspto_oce_pair.status_codes



> USPTO Patent Examination Research Data (PatEx) contains detailed information on millions of publicly viewable patent applications filed with the USPTO. The data are sourced from the Public Patent Application Information Retrieval system (Public PAIR).
> 
> “USPTO Patent Examination Research Dataset” by the USPTO, for public use.
> Graham, S. Marco, A., and Miller, A. (2015). “The USPTO Patent Examination Research Dataset: A Window on the Process of Patent Examination.”





| Stat | Value |
|----------|----------|
| Last updated | 2017-10-12 |
| Rows | 233 |
| Size | 11.7 kB |

### Schema
[View in BigQuery](https://bigquery.cloud.google.com/table/patents-public-data:uspto_oce_pair.status_codes)

* `appl_status_code` STRING  

* `status_description` STRING  












*****
## patents-public-data:uspto_oce_pair.status_codes_2015


Old table version `2015`, schema skipped.





*****
## patents-public-data:uspto_oce_pair.transactions



> USPTO Patent Examination Research Data (PatEx) contains detailed information on millions of publicly viewable patent applications filed with the USPTO. The data are sourced from the Public Patent Application Information Retrieval system (Public PAIR).
> 
> “USPTO Patent Examination Research Dataset” by the USPTO, for public use.
> Graham, S. Marco, A., and Miller, A. (2015). “The USPTO Patent Examination Research Dataset: A Window on the Process of Patent Examination.”





| Stat | Value |
|----------|----------|
| Last updated | 2017-10-12 |
| Rows | 306,492,155 |
| Size | 10.4 GB |

### Schema
[View in BigQuery](https://bigquery.cloud.google.com/table/patents-public-data:uspto_oce_pair.transactions)

* `application_number` STRING  

* `event_code` STRING  

* `recorded_date` STRING  

* `sequence_number` STRING  

* `status_code` STRING  


















*****
## patents-public-data:uspto_oce_pair.transactions_2015


Old table version `2015`, schema skipped.





*****
## patents-public-data:uspto_peds.applications



> USPTO Patent Examiner Data System (PEDS) API Data contains data from the examination process of USPTO patent applications. PEDS contains the bibliographic, published document and patent term extension data tabs in Public PAIR from 1981 to present. There is also some data dating back to 1935.
> 
> "Patent Examination Data System" by the USPTO, for public use.





| Stat | Value |
|----------|----------|
| Last updated | 2017-10-12 |
| Rows | 13,179,987 |
| Size | 21.3 GB |

### Schema
[View in BigQuery](https://bigquery.cloud.google.com/table/patents-public-data:uspto_peds.applications)

* `patentCaseMetadata` RECORD NULLABLE 

* `patentCaseMetadata.applicantFileReference` STRING NULLABLE 

* `patentCaseMetadata.applicationConfirmationNumber` STRING NULLABLE 

* `patentCaseMetadata.applicationNumberText` RECORD NULLABLE 

* `patentCaseMetadata.applicationNumberText.electronicText` STRING NULLABLE  joins on **PEDS app_num**

* `patentCaseMetadata.applicationNumberText.value` STRING NULLABLE 

* `patentCaseMetadata.applicationStatusCategory` STRING NULLABLE 

* `patentCaseMetadata.applicationStatusDate` STRING NULLABLE 

* `patentCaseMetadata.applicationTypeCategory` STRING NULLABLE 

* `patentCaseMetadata.businessEntityStatusCategory` STRING NULLABLE 

* `patentCaseMetadata.filingDate` STRING NULLABLE 

* `patentCaseMetadata.firstInventorToFileIndicator` BOOLEAN NULLABLE 

* `patentCaseMetadata.groupArtUnitNumber` RECORD NULLABLE 

* `patentCaseMetadata.groupArtUnitNumber.electronicText` STRING NULLABLE 

* `patentCaseMetadata.groupArtUnitNumber.value` STRING NULLABLE 

* `patentCaseMetadata.hagueAgreementData` RECORD NULLABLE 

* `patentCaseMetadata.hagueAgreementData.internationalFilingDate` STRING NULLABLE 

* `patentCaseMetadata.hagueAgreementData.internationalRegistrationNumber` STRING NULLABLE 

* `patentCaseMetadata.inventionTitle` RECORD NULLABLE 

* `patentCaseMetadata.inventionTitle.content` STRING REPEATED 

* `patentCaseMetadata.officialFileLocationCategory` STRING NULLABLE 

* `patentCaseMetadata.officialFileLocationDate` STRING NULLABLE 

* `patentCaseMetadata.partyBag` RECORD NULLABLE 

* `patentCaseMetadata.partyBag.applicantBagOrInventorBagOrOwnerBag` RECORD REPEATED 

* `patentCaseMetadata.partyBag.applicantBagOrInventorBagOrOwnerBag.primaryExaminerOrAssistantExaminerOrAuthorizedOfficer` RECORD REPEATED 

* `patentCaseMetadata.partyBag.applicantBagOrInventorBagOrOwnerBag.primaryExaminerOrAssistantExaminerOrAuthorizedOfficer.name` RECORD NULLABLE 

* `patentCaseMetadata.partyBag.applicantBagOrInventorBagOrOwnerBag.primaryExaminerOrAssistantExaminerOrAuthorizedOfficer.name.personNameOrOrganizationNameOrEntityName` RECORD REPEATED 

* `patentCaseMetadata.partyBag.applicantBagOrInventorBagOrOwnerBag.primaryExaminerOrAssistantExaminerOrAuthorizedOfficer.name.personNameOrOrganizationNameOrEntityName.personFullName` STRING NULLABLE 

* `patentCaseMetadata.patentClassificationBag` RECORD NULLABLE 

* `patentCaseMetadata.patentClassificationBag.cpcClassificationBagOrIPCClassificationOrECLAClassificationBag` RECORD REPEATED 

* `patentCaseMetadata.patentClassificationBag.cpcClassificationBagOrIPCClassificationOrECLAClassificationBag.mainNationalClassification` RECORD NULLABLE 

* `patentCaseMetadata.patentClassificationBag.cpcClassificationBagOrIPCClassificationOrECLAClassificationBag.mainNationalClassification.nationalClass` STRING NULLABLE 

* `patentCaseMetadata.patentClassificationBag.cpcClassificationBagOrIPCClassificationOrECLAClassificationBag.mainNationalClassification.nationalSubclass` STRING NULLABLE 

* `patentCaseMetadata.patentGrantIdentification` RECORD NULLABLE 

* `patentCaseMetadata.patentGrantIdentification.grantDate` STRING NULLABLE 

* `patentCaseMetadata.patentGrantIdentification.patentNumber` STRING NULLABLE 

* `patentCaseMetadata.relatedPatentPublicationIdentification` RECORD NULLABLE 

* `patentCaseMetadata.relatedPatentPublicationIdentification.publicationDate` STRING NULLABLE 

* `patentCaseMetadata.relatedPatentPublicationIdentification.publicationNumber` STRING NULLABLE 

* `prosecutionHistoryDataOrPatentTermData` RECORD REPEATED 

* `prosecutionHistoryDataOrPatentTermData.caseActionDescriptionText` STRING NULLABLE 

* `prosecutionHistoryDataOrPatentTermData.recordedDate` STRING NULLABLE 



### Join columns










#### patentCaseMetadata.applicationNumberText.electronicText

joins to `patents-public-data:uspto_peds.match::applicationNumberText` on **PEDS app_num** (69.52%, 9,162,425 rows)

| Key | Percent | Rows | Sample values |
|------|-----|--------|--------------------------------------------------------|
| `all` | 69.52% | 9,162,425 | `['08960693', '12727656', '12054764', '29386609', '08889454']` |


    #standardSQL
    SELECT
      COUNT(*) AS cnt,
      COUNT(second.second_column) AS second_cnt,
      ARRAY_AGG(first.patentCaseMetadata.applicationNumberText.electronicText IGNORE NULLS ORDER BY RAND() LIMIT 5) AS sample_value
    FROM `patents-public-data.uspto_peds.applications`AS first
    LEFT JOIN (
      SELECT applicationNumberText AS second_column, COUNT(*) AS cnt
      FROM `patents-public-data.uspto_peds.match`
      GROUP BY 1
    ) AS second ON first.patentCaseMetadata.applicationNumberText.electronicText = second.second_column



joins from `patents-public-data:uspto_peds.match::applicationNumberText` on **PEDS app_num** (100.00%, 9,162,425 rows)
















































































*****
## patents-public-data:uspto_peds.applications_201710


Old table version `201710`, schema skipped.





*****
## patents-public-data:uspto_peds.match



> USPTO Patent Examiner Data System (PEDS) API Data contains data from the examination process of USPTO patent applications. PEDS contains the bibliographic, published document and patent term extension data tabs in Public PAIR from 1981 to present. There is also some data dating back to 1935.
> 
> "Patent Examination Data System" by the USPTO, for public use.





| Stat | Value |
|----------|----------|
| Last updated | 2017-10-23 |
| Rows | 9,162,425 |
| Size | 244.5 MB |

### Schema
[View in BigQuery](https://bigquery.cloud.google.com/table/patents-public-data:uspto_peds.match)

* `applicationNumberText` STRING NULLABLE  joins on **PEDS app_num**

* `application_number` STRING NULLABLE  joins on **application_number**



### Join columns


#### applicationNumberText

joins to `patents-public-data:uspto_peds.applications::patentCaseMetadata.applicationNumberText.electronicText` on **PEDS app_num** (100.00%, 9,162,425 rows)

| Key | Percent | Rows | Sample values |
|------|-----|--------|--------------------------------------------------------|
| `all` | 100.00% | 9,162,425 | `['13434120', '11431563', '15383658', '10086983', '14195460']` |


    #standardSQL
    SELECT
      COUNT(*) AS cnt,
      COUNT(second.second_column) AS second_cnt,
      ARRAY_AGG(first.applicationNumberText IGNORE NULLS ORDER BY RAND() LIMIT 5) AS sample_value
    FROM `patents-public-data.uspto_peds.match`AS first
    LEFT JOIN (
      SELECT patentCaseMetadata.applicationNumberText.electronicText AS second_column, COUNT(*) AS cnt
      FROM `patents-public-data.uspto_peds.applications`
      GROUP BY 1
    ) AS second ON first.applicationNumberText = second.second_column



joins from `patents-public-data:uspto_peds.applications::patentCaseMetadata.applicationNumberText.electronicText` on **PEDS app_num** (69.52%, 9,162,425 rows)




#### application_number

joins to `patents-public-data:patents.publications::application_number` on **application_number** (100.00%, 9,162,229 rows)

| Key | Percent | Rows | Sample values |
|------|-----|--------|--------------------------------------------------------|
| `all` | 100.00% | 9,162,229 | `['US-81374905-A', 'US-94464801-A', 'US-1568598-A', 'US-201515504234-A', 'US-82286201-A']` |


    #standardSQL
    SELECT
      COUNT(*) AS cnt,
      COUNT(second.second_column) AS second_cnt,
      ARRAY_AGG(first.application_number IGNORE NULLS ORDER BY RAND() LIMIT 5) AS sample_value
    FROM `patents-public-data.uspto_peds.match`AS first
    LEFT JOIN (
      SELECT application_number AS second_column, COUNT(*) AS cnt
      FROM `patents-public-data.patents.publications`
      GROUP BY 1
    ) AS second ON first.application_number = second.second_column



joins from `patents-public-data:patents.publications::application_number` on **application_number** (13.86%, 13,603,596 rows)






*****
## patents-public-data:uspto_peds.match_201710


Old table version `201710`, schema skipped.





*****
## patents-public-data:uspto_ptab.match



> USPTO Patent Trial and Appeal Board (PTAB) API Data contains data from the PTAB E2E (end-to-end) system making public America Invents Action (AIA) Trials information and documents available.
> 
> “USPTO PTAB API” by the USPTO, for public use.





| Stat | Value |
|----------|----------|
| Last updated | 2017-10-23 |
| Rows | 4,610 |
| Size | 119.9 kB |

### Schema
[View in BigQuery](https://bigquery.cloud.google.com/table/patents-public-data:uspto_ptab.match)

* `ApplicationNumber` STRING NULLABLE  joins on **PTAB app_num**

* `application_number` STRING NULLABLE  joins on **application_number**



### Join columns


#### ApplicationNumber

joins to `patents-public-data:uspto_ptab.trials::ApplicationNumber` on **PTAB app_num** (100.00%, 4,610 rows)

| Key | Percent | Rows | Sample values |
|------|-----|--------|--------------------------------------------------------|
| `all` | 100.00% | 4,610 | `['10975409', '13374942', '11971183', '10706513', '10443342']` |


    #standardSQL
    SELECT
      COUNT(*) AS cnt,
      COUNT(second.second_column) AS second_cnt,
      ARRAY_AGG(first.ApplicationNumber IGNORE NULLS ORDER BY RAND() LIMIT 5) AS sample_value
    FROM `patents-public-data.uspto_ptab.match`AS first
    LEFT JOIN (
      SELECT ApplicationNumber AS second_column, COUNT(*) AS cnt
      FROM `patents-public-data.uspto_ptab.trials`
      GROUP BY 1
    ) AS second ON first.ApplicationNumber = second.second_column



joins from `patents-public-data:uspto_ptab.trials::ApplicationNumber` on **PTAB app_num** (99.95%, 7,601 rows)




#### application_number

joins to `patents-public-data:patents.publications::application_number` on **application_number** (100.00%, 4,610 rows)

| Key | Percent | Rows | Sample values |
|------|-----|--------|--------------------------------------------------------|
| `all` | 100.00% | 4,610 | `['US-201213441092-A', 'US-201213484854-A', 'US-201313750744-A', 'US-39754206-A', 'US-65423707-A']` |


    #standardSQL
    SELECT
      COUNT(*) AS cnt,
      COUNT(second.second_column) AS second_cnt,
      ARRAY_AGG(first.application_number IGNORE NULLS ORDER BY RAND() LIMIT 5) AS sample_value
    FROM `patents-public-data.uspto_ptab.match`AS first
    LEFT JOIN (
      SELECT application_number AS second_column, COUNT(*) AS cnt
      FROM `patents-public-data.patents.publications`
      GROUP BY 1
    ) AS second ON first.application_number = second.second_column



joins from `patents-public-data:patents.publications::application_number` on **application_number** (0.01%, 7,832 rows)






*****
## patents-public-data:uspto_ptab.match_201710


Old table version `201710`, schema skipped.





*****
## patents-public-data:uspto_ptab.trials



> USPTO Patent Trial and Appeal Board (PTAB) API Data contains data from the PTAB E2E (end-to-end) system making public America Invents Action (AIA) Trials information and documents available.
> 
> “USPTO PTAB API” by the USPTO, for public use.





| Stat | Value |
|----------|----------|
| Last updated | 2017-10-11 |
| Rows | 7,605 |
| Size | 71.7 MB |

### Schema
[View in BigQuery](https://bigquery.cloud.google.com/table/patents-public-data:uspto_ptab.trials)

* `InventorName` STRING NULLABLE 

* `PatentOwnerName` STRING NULLABLE 

* `LastModifiedDatetime` STRING NULLABLE 

* `InstitutionDecisionDate` STRING NULLABLE 

* `ProsecutionStatus` STRING NULLABLE 

* `AccordedFilingDate` STRING NULLABLE 

* `PatentNumber` STRING NULLABLE 

* `PetitionerPartyName` STRING NULLABLE 

* `TrialNumber` STRING NULLABLE 

* `ApplicationNumber` STRING NULLABLE  joins on **PTAB app_num**

* `FilingDate` STRING NULLABLE 

* `Documents` RECORD REPEATED 

* `Documents.SizeInBytes` INTEGER NULLABLE 

* `Documents.TrialNumber` STRING NULLABLE 

* `Documents.DocumentNumber` STRING NULLABLE 

* `Documents.Title` STRING NULLABLE 

* `Documents.FilingDatetime` STRING NULLABLE 

* `Documents.LastModifiedDatedime` STRING NULLABLE 

* `Documents.FilingParty` STRING NULLABLE 

* `Documents.MediaType` STRING NULLABLE 

* `Documents.Id` INTEGER NULLABLE 

* `Documents.Type` STRING NULLABLE 



### Join columns




















#### ApplicationNumber

joins to `patents-public-data:uspto_ptab.match::ApplicationNumber` on **PTAB app_num** (99.95%, 7,601 rows)

| Key | Percent | Rows | Sample values |
|------|-----|--------|--------------------------------------------------------|
| `all` | 99.95% | 7,601 | `['11712175', '13906645', '09449695', '10510550', '09567013']` |


    #standardSQL
    SELECT
      COUNT(*) AS cnt,
      COUNT(second.second_column) AS second_cnt,
      ARRAY_AGG(first.ApplicationNumber IGNORE NULLS ORDER BY RAND() LIMIT 5) AS sample_value
    FROM `patents-public-data.uspto_ptab.trials`AS first
    LEFT JOIN (
      SELECT ApplicationNumber AS second_column, COUNT(*) AS cnt
      FROM `patents-public-data.uspto_ptab.match`
      GROUP BY 1
    ) AS second ON first.ApplicationNumber = second.second_column



joins from `patents-public-data:uspto_ptab.match::ApplicationNumber` on **PTAB app_num** (100.00%, 4,610 rows)






























*****
## patents-public-data:uspto_ptab.trials_201710


Old table version `201710`, schema skipped.




