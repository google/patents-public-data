
---
geometry: margin=0.6in
---

# CPA Global


*****
## innography-174118:technical_standards.etsi



> European Telecommunications Standards Institute (ETSI) IPR dataset for technical standards.
> These are the US assets disclosed by companies as related to technical standards in ETSI.  The two major ones included are 3GPP and LTE.


> “Innography ETSI Data” by Innography (through ETSI IPR) is licensed under a Creative Commons Attribution 4.0 International License.




| Stat | Value |
|----------|----------|
| Last updated | 2017-07-25 |
| Rows | 34,465 |
| Size | 1.0 MB |

### Schema
[View in BigQuery](https://bigquery.cloud.google.com/table/innography-174118:technical_standards.etsi)

* `PublicationNumber` STRING REQUIRED  joins on **publication_number**

* `StandardBody` STRING REQUIRED 

* `TechnicalStandard` STRING REQUIRED 



### Join columns


#### PublicationNumber

joins to `patents-public-data:patents.publications::publication_number` on **publication_number** (99.98%, 34,458 rows)

| Key | Percent | Rows | Sample values |
|------|-----|--------|--------------------------------------------------------|
| `3GPP, LTE` | 99.99% | 8,381 | `['US-2009141670-A1', 'US-9673942-B2', 'US-2003185390-A1', 'US-7489672-B2', 'US-8347177-B2']` |
| `LTE` | 99.99% | 7,071 | `['US-2011064120-A1', 'US-2009325504-A1', 'US-2014094175-A1', 'US-6163533-A', 'US-8009661-B2']` |
| `3GPP` | 99.97% | 19,006 | `['US-8594035-B2', 'US-2012014344-A1', 'US-2017012727-A1', 'US-9648048-B2', 'US-2005065801-A1']` |


    #standardSQL
    SELECT
      COUNT(*) AS cnt,
      COUNT(second.second_column) AS second_cnt,
      first.TechnicalStandard AS grouped,
      ARRAY_AGG(first.PublicationNumber IGNORE NULLS ORDER BY RAND() LIMIT 5) AS sample_value
    FROM `innography-174118.technical_standards.etsi`AS first
    LEFT JOIN (
      SELECT publication_number AS second_column, COUNT(*) AS cnt
      FROM `patents-public-data.patents.publications`
      GROUP BY 1
    ) AS second ON first.PublicationNumber = second.second_column
    GROUP BY 3



joins from `patents-public-data:patents.publications::publication_number` on **publication_number** (0.04%, 34,458 rows)









