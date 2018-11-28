
---
geometry: margin=0.6in
---

# Other


*****
## patents-public-data:cpc.definitions



> Cooperative Patent Classification Data contains the scheme and definitions of the Cooperative Patent Classification system for classifying patent documents.
> 
> “Cooperative Patent Classification” by the EPO and USPTO, for public use. Modifications have been made to parse the XML description sections to extract references to other classification symbols.





| Stat | Value |
|----------|----------|
| Last updated | 2017-10-12 |
| Rows | 259,839 |
| Size | 123.0 MB |

### Schema
[View in BigQuery](https://bigquery.cloud.google.com/table/patents-public-data:cpc.definitions)

* `symbol` STRING NULLABLE 

* `title_full` STRING NULLABLE 

* `title_part` STRING REPEATED 

* `parents` STRING REPEATED 

* `children` STRING REPEATED 

* `child_groups` RECORD REPEATED 

* `child_groups.description` STRING NULLABLE 

* `child_groups.symbols` STRING REPEATED 

* `definition` STRING REPEATED 

* `breakdown_code` BOOLEAN NULLABLE 

* `not_allocatable` BOOLEAN NULLABLE 

* `additional_only` BOOLEAN NULLABLE 

* `level` INTEGER NULLABLE 

* `date_revised` INTEGER NULLABLE 

* `status` STRING NULLABLE 

* `ipc_concordant` STRING NULLABLE 

* `limiting_references` RECORD REPEATED 

* `limiting_references.description` STRING NULLABLE 

* `limiting_references.target` STRING REPEATED 

* `informative_references` RECORD REPEATED 

* `informative_references.description` STRING NULLABLE 

* `informative_references.target` STRING REPEATED 

* `residual_references` RECORD REPEATED 

* `residual_references.description` STRING NULLABLE 

* `residual_references.target` STRING REPEATED 

* `application_references` RECORD REPEATED 

* `application_references.description` STRING NULLABLE 

* `application_references.target` STRING REPEATED 

* `glossary` RECORD REPEATED 

* `glossary.description` STRING NULLABLE 

* `glossary.target` STRING REPEATED 

* `synonyms` RECORD REPEATED 

* `synonyms.description` STRING NULLABLE 

* `synonyms.target` STRING REPEATED 












































































*****
## patents-public-data:cpc.definitions_201710


Old table version `201710`, schema skipped.





*****
## patents-public-data:dsep.disclosures_13



> Disclosed Standard Essential Patents (dSEP) Data provides a full overview of disclosed intellectual property rights at setting organizations worldwide.
> 
> “Disclosed Standard Essential Patents Database” by Bekkers, R., Catalini, C., Martinelli, A., & Simcoe, T. (2012). Intellectual Property Disclosure in Standards Development. Proceedings from NBER conference on Standards, Patents & Innovation, Tucson (AZ), January 20 and 21, 2012.





| Stat | Value |
|----------|----------|
| Last updated | 2017-02-07 |
| Rows | 45,349 |
| Size | 6.7 MB |

### Schema
[View in BigQuery](https://bigquery.cloud.google.com/table/patents-public-data:dsep.disclosures_13)

* `family_id` STRING NULLABLE  joins on **family_id**

    > Family ID (simple family). Grouping on family ID will return all publications associated with a simple patent family (all publications share the same priority claims). This is empty if the disclosure could not be matched to any patents.

* `record_id` STRING NULLABLE 

    > Unique ID for each record in the database

* `disclosure_event` STRING NULLABLE 

    > A disclosure event refers to one or more IPR discloses from a given firm to a given SSO on a given date. A disclosure event may include multiple patents and/or blankets, referring to one or more standards. While some SSO archives are organized around disclosure events and other are not, our disclosure events are constructed from the data in a uniform way.

* `sso` STRING NULLABLE 

    > Standard setting organization (SSO) at which the disclosure was made

* `patent_owner_harmonized` STRING NULLABLE 

    > Harmonised and cleaned name of the company or organisation that made the disclosure. Accounts for different spellings of a firm name within or across SSOs. But does not account for mergers and acquisitions after the data od diclosure. Note that, in the case of a third party disclosure, the patent owner is not the one that also submitted the seclaration

* `patent_owner_unharmonized` STRING NULLABLE 

    > Name of the company, as it appears in the original disclosure, before harminization.

* `date` INTEGER NULLABLE 

    > Date of the original statement submitted to the SSO

* `standard` STRING NULLABLE 

    > Name of the standard for which the IPR is disclosed (if provided in the original disclosure)

* `committee_project` STRING NULLABLE 

    > Name of the committee for which the IPR is disclosed (if provided in the original disclosure)

* `tc_name` STRING NULLABLE 

    > Technical committee relevant for the disclosure (if provided in the original disclosure)

* `sc_name` STRING NULLABLE 

    > Standard committee relevant for the disclosure (if provided in the original disclosure)

* `wg_name` STRING NULLABLE 

    > Working Group relevant for the disclosure (if provided in the original disclosure)

* `licensing_commitment` STRING NULLABLE 

    > Licensing commitment with respect to the disclosed patents

* `copyright` STRING NULLABLE 

    > Equal to 1 if the disclosed IPR is a copyright instead of a patent

* `blanket_type` STRING NULLABLE 

    > A blanket disclosure (sometimes called 'generic disclosure) is a disclosure in which a party indicates it believes it may own relevant IP, but does not provide the identity of any patents or pending patent applications.This field  indicates whether this is the case, and if so, for which specific activity or standard this blanket is submitted. It can take the following values: (0) No blanket, (1) Blanket for all SDO activities, (2) Blanket for a project, committee, subcommitee or technical committee, (3) Blanket for a specific standard or specific technical specification

* `blanket_scope` STRING NULLABLE 

    > Indicates to which specific project, subproject, specific standard or specific technical specification the blanket claim refers. Only exists if BLANKET_TYPE has the value 2 or 3.

* `third_party` STRING NULLABLE 

    > It indicates wheather the disclosure was made by a third party

* `reciprocity` STRING NULLABLE 

    > Indicates whether the disclosure explicitely indicates the licensing commitment is on the condition of reciprocity. Please note that some SSOs may have differerent rules on whether such a condition is 'automatically' implied

* `serial_cleaned` STRING NULLABLE 

    > For all US or EP patents, this field shows the serial number of the patent application that was provided in the original disclosure (if any). It is cleaned in the sense that it uses a standardised format (field length, comma's, slashes, etc.) Note that to related these numbers to the serial numbers in years, a translation was used as found on http://www.uspto.gov/web/offices/ac/ido/oeip/taf/filingyr.htm

* `pub_cleaned` STRING NULLABLE 

    > For all US or EP patents, this field shows the publication number that was provided in the original disclosure (if any). It is cleaned in the sense that it uses a standardised format



### Join columns


#### family_id

joins to `patents-public-data:patents.publications::family_id` on **family_id** (29.46%, 13,358 rows)

| Key | Percent | Rows | Sample values |
|------|-----|--------|--------------------------------------------------------|
| `all` | 29.46% | 13,358 | `['16400664', '', '21798855', '', '35529745']` |


    #standardSQL
    SELECT
      COUNT(*) AS cnt,
      COUNT(second.second_column) AS second_cnt,
      ARRAY_AGG(first.family_id IGNORE NULLS ORDER BY RAND() LIMIT 5) AS sample_value
    FROM `patents-public-data.dsep.disclosures_13`AS first
    LEFT JOIN (
      SELECT family_id AS second_column, COUNT(*) AS cnt
      FROM `patents-public-data.patents.publications`
      GROUP BY 1
    ) AS second ON first.family_id = second.second_column



joins from `patents-public-data:patents.publications::family_id` on **family_id** (0.06%, 61,139 rows)












































*****
## patents-public-data:marec.publications



> MAREC Data is a static collection of over 19 million patent applications and granted patents in a unified file format normalized from EP, WO, US, and JP sources, spanning a range from 1976 to June 2008.
> 
> “The MAtrixware REsearch Collection” by cortical.io, used under CC BY 4.0.





| Stat | Value |
|----------|----------|
| Last updated | 2017-10-10 |
| Rows | 19,101,548 |
| Size | 547.0 GB |

### Schema
[View in BigQuery](https://bigquery.cloud.google.com/table/patents-public-data:marec.publications)

* `publication_number` STRING NULLABLE  joins on **publication_number**

    > DOCDB-format publication number, such as 'WO-1978000002-A2'.

* `publication_number_original` STRING NULLABLE 

    > Publication number (differs for WO and US from DOCDB).

* `xml` STRING NULLABLE 

    > The publication XML content, including the metadata, title, abstract, claims and description. This is truncated at 9MB.

* `truncated` BOOLEAN NULLABLE 

    > True if the XML has been truncated at 9MB.



### Join columns


#### publication_number

joins to `patents-public-data:patents.publications::publication_number` on **publication_number** (71.12%, 13,585,005 rows)

| Key | Percent | Rows | Sample values |
|------|-----|--------|--------------------------------------------------------|
| `all` | 71.12% | 13,585,005 | `['EP-1846381-B1', 'EP-0538783-B1', 'JP-11006748-A', 'EP-0739715-A3', 'WO-2007094082-A1']` |


    #standardSQL
    SELECT
      COUNT(*) AS cnt,
      COUNT(second.second_column) AS second_cnt,
      ARRAY_AGG(first.publication_number IGNORE NULLS ORDER BY RAND() LIMIT 5) AS sample_value
    FROM `patents-public-data.marec.publications`AS first
    LEFT JOIN (
      SELECT publication_number AS second_column, COUNT(*) AS cnt
      FROM `patents-public-data.patents.publications`
      GROUP BY 1
    ) AS second ON first.publication_number = second.second_column



joins from `patents-public-data:patents.publications::publication_number` on **publication_number** (13.83%, 13,577,285 rows)












*****
## patents-public-data:usitc_investigations.investigations



> US International Trade Commission 337Info Unfair Import Investigations Information System contains data on investigations done under Section 337. Section 337 declares the infringement of certain statutory intellectual property rights and other forms of unfair competition in import trade to be unlawful practices. Most Section 337 investigations involve allegations of patent or registered trademark infringement.
> 
> "US International Trade Commission 337Info Unfair Import Investigations Information System" by the USITC, for public use.





| Stat | Value |
|----------|----------|
| Last updated | 2017-10-12 |
| Rows | 486 |
| Size | 2.7 MB |

### Schema
[View in BigQuery](https://bigquery.cloud.google.com/table/patents-public-data:usitc_investigations.investigations)

* `actualEndDateEvidHear` STRING NULLABLE 

* `actualStartDateEvidHear` STRING NULLABLE 

* `aljAssigned` RECORD REPEATED 

* `aljAssigned.active` BOOLEAN NULLABLE 

* `aljAssigned.class` STRING NULLABLE 

* `aljAssigned.id` FLOAT NULLABLE 

* `aljAssigned.userName` STRING NULLABLE 

* `aljAssigned.userName_m` STRING NULLABLE 

* `cafcAppeals` RECORD REPEATED 

* `cafcAppeals.amicus` STRING NULLABLE 

* `cafcAppeals.appealLitStatus` STRING NULLABLE 

* `cafcAppeals.appellant` STRING NULLABLE 

* `cafcAppeals.caseName` STRING NULLABLE 

* `cafcAppeals.caseNumber` STRING NULLABLE 

* `cafcAppeals.class` STRING NULLABLE 

* `cafcAppeals.courtOpinion` STRING NULLABLE 

* `cafcAppeals.dateAppealPettionFiled` STRING NULLABLE 

* `cafcAppeals.dateCommDecRemand` STRING NULLABLE 

* `cafcAppeals.dateCourtOpinion` STRING NULLABLE 

* `cafcAppeals.dateItcBrief` STRING NULLABLE 

* `cafcAppeals.dateMandateIssued` STRING NULLABLE 

* `cafcAppeals.dateOralArgument` STRING NULLABLE 

* `cafcAppeals.dateOrderRemandAlj` STRING NULLABLE 

* `cafcAppeals.dateRemandIdDue` STRING NULLABLE 

* `cafcAppeals.dateRemandIdIssued` STRING NULLABLE 

* `cafcAppeals.id` FLOAT NULLABLE 

* `cafcAppeals.intervenor` STRING NULLABLE 

* `cafcAppeals.participants` RECORD REPEATED 

* `cafcAppeals.participants.active` BOOLEAN NULLABLE 

* `cafcAppeals.participants.cafcAppeal` RECORD NULLABLE 

* `cafcAppeals.participants.cafcAppeal.class` STRING NULLABLE 

* `cafcAppeals.participants.cafcAppeal.id` FLOAT NULLABLE 

* `cafcAppeals.participants.cafcAppeal.ref` STRING NULLABLE 

* `cafcAppeals.participants.class` STRING NULLABLE 

* `cafcAppeals.participants.id` FLOAT NULLABLE 

* `cafcAppeals.participants.outsideParty` RECORD NULLABLE 

* `cafcAppeals.participants.outsideParty.address1` STRING NULLABLE 

* `cafcAppeals.participants.outsideParty.address2` STRING NULLABLE 

* `cafcAppeals.participants.outsideParty.city` STRING NULLABLE 

* `cafcAppeals.participants.outsideParty.class` STRING NULLABLE 

* `cafcAppeals.participants.outsideParty.country` STRING NULLABLE 

* `cafcAppeals.participants.outsideParty.email` STRING NULLABLE 

* `cafcAppeals.participants.outsideParty.fax` STRING NULLABLE 

* `cafcAppeals.participants.outsideParty.id` FLOAT NULLABLE 

* `cafcAppeals.participants.outsideParty.partyName` STRING NULLABLE 

* `cafcAppeals.participants.outsideParty.phone` STRING NULLABLE 

* `cafcAppeals.participants.outsideParty.state` STRING NULLABLE 

* `cafcAppeals.participants.outsideParty.webSite` STRING NULLABLE 

* `cafcAppeals.participants.outsideParty.zip` STRING NULLABLE 

* `cafcAppeals.participants.participantType` STRING NULLABLE 

* `cafcAppeals.rehearingType` STRING NULLABLE 

* `cafcAppeals.remandToAlj` BOOLEAN NULLABLE 

* `complainant` RECORD REPEATED 

* `complainant.activeDate` STRING NULLABLE 

* `complainant.class` STRING NULLABLE 

* `complainant.complainantRep` RECORD REPEATED 

* `complainant.complainantRep.class` STRING NULLABLE 

* `complainant.complainantRep.dateCreated` STRING NULLABLE 

* `complainant.complainantRep.id` FLOAT NULLABLE 

* `complainant.complainantRep.lastUpdated` STRING NULLABLE 

* `complainant.complainantRep.reportNotes` STRING NULLABLE 

* `complainant.complainantRep.reportTitle` STRING NULLABLE 

* `complainant.complainantRep.requirement` BOOLEAN NULLABLE 

* `complainant.id` FLOAT NULLABLE 

* `complainant.inactiveDate` STRING NULLABLE 

* `complainant.leadCounsel` STRING NULLABLE 

* `complainant.outsideParty` RECORD NULLABLE 

* `complainant.outsideParty.address1` STRING NULLABLE 

* `complainant.outsideParty.address2` STRING NULLABLE 

* `complainant.outsideParty.city` STRING NULLABLE 

* `complainant.outsideParty.class` STRING NULLABLE 

* `complainant.outsideParty.country` STRING NULLABLE 

* `complainant.outsideParty.id` FLOAT NULLABLE 

* `complainant.outsideParty.partyName` STRING NULLABLE 

* `complainant.outsideParty.phone` STRING NULLABLE 

* `complainant.outsideParty.state` STRING NULLABLE 

* `complainant.outsideParty.webSite` STRING NULLABLE 

* `complainant.outsideParty.zip` STRING NULLABLE 

* `copyrightNumbers` RECORD REPEATED 

* `copyrightNumbers.activeDate` STRING NULLABLE 

* `copyrightNumbers.class` STRING NULLABLE 

* `copyrightNumbers.copyrightNumber` STRING NULLABLE 

* `copyrightNumbers.id` FLOAT NULLABLE 

* `copyrightNumbers.inactiveDate` STRING NULLABLE 

* `currentActiveALJ` STRING NULLABLE 

* `currentStatus` STRING NULLABLE 

* `dateComplaintFiled` STRING NULLABLE 

* `dateCreated` STRING NULLABLE 

* `dateOfPublicationFrNotice` STRING NULLABLE 

* `docketNo` STRING NULLABLE 

* `endDateMarkmanHearing` STRING NULLABLE 

* `finalDetNoViolation` STRING NULLABLE 

* `finalDetViolation` STRING NULLABLE 

* `finalIdOnViolationDue` STRING NULLABLE 

* `finalIdOnViolationIssue` STRING NULLABLE 

* `gcAttorney` RECORD REPEATED 

* `gcAttorney.active` BOOLEAN NULLABLE 

* `gcAttorney.class` STRING NULLABLE 

* `gcAttorney.id` FLOAT NULLABLE 

* `gcAttorney.userName` STRING NULLABLE 

* `gcAttorney.userName_m` STRING NULLABLE 

* `htsNumbers` RECORD REPEATED 

* `htsNumbers.categoryBasket` STRING NULLABLE 

* `htsNumbers.class` STRING NULLABLE 

* `htsNumbers.hts8` STRING NULLABLE 

* `htsNumbers.id` FLOAT NULLABLE 

* `id` STRING NULLABLE 

* `internalRemand` RECORD REPEATED 

* `internalRemand.class` STRING NULLABLE 

* `internalRemand.id` FLOAT NULLABLE 

* `internalRemand.remandIdDueDate` STRING NULLABLE 

* `internalRemand.remandIdIssueDate` STRING NULLABLE 

* `invUnfairAct` RECORD REPEATED 

* `invUnfairAct.activeDate` STRING NULLABLE 

* `invUnfairAct.class` STRING NULLABLE 

* `invUnfairAct.dateCreated` STRING NULLABLE 

* `invUnfairAct.id` FLOAT NULLABLE 

* `invUnfairAct.inactiveDate` STRING NULLABLE 

* `invUnfairAct.lastUpdated` STRING NULLABLE 

* `invUnfairAct.unfairActInNotice` STRING NULLABLE 

* `invUnfairAct.unfairActInNotice_a` STRING NULLABLE 

* `investigationNo` STRING NULLABLE 

* `investigationTermDate` STRING NULLABLE 

* `investigationType` STRING NULLABLE 

* `issueDateOtherNonFinal` STRING NULLABLE 

* `lastUpdated` STRING NULLABLE 

* `markmanHearing` BOOLEAN NULLABLE 

* `ouiiAttorney` RECORD REPEATED 

* `ouiiAttorney.active` BOOLEAN NULLABLE 

* `ouiiAttorney.class` STRING NULLABLE 

* `ouiiAttorney.id` FLOAT NULLABLE 

* `ouiiAttorney.userName` STRING NULLABLE 

* `ouiiAttorney.userName_m` STRING NULLABLE 

* `ouiiParticipation` RECORD REPEATED 

* `ouiiParticipation.class` STRING NULLABLE 

* `ouiiParticipation.id` FLOAT NULLABLE 

* `ouiiParticipation.ouiiParticipationLevel` STRING NULLABLE 

* `patentNumbers` RECORD REPEATED 

* `patentNumbers.activeDate` STRING NULLABLE 

* `patentNumbers.class` STRING NULLABLE 

* `patentNumbers.id` FLOAT NULLABLE 

* `patentNumbers.inactiveDate` STRING NULLABLE 

* `patentNumbers.patentNumber` STRING NULLABLE 

* `respondent` RECORD REPEATED 

* `respondent.activeDate` STRING NULLABLE 

* `respondent.class` STRING NULLABLE 

* `respondent.id` FLOAT NULLABLE 

* `respondent.inactiveDate` STRING NULLABLE 

* `respondent.leadCounsel` STRING NULLABLE 

* `respondent.outsideParty` RECORD NULLABLE 

* `respondent.outsideParty.address1` STRING NULLABLE 

* `respondent.outsideParty.address2` STRING NULLABLE 

* `respondent.outsideParty.city` STRING NULLABLE 

* `respondent.outsideParty.class` STRING NULLABLE 

* `respondent.outsideParty.country` STRING NULLABLE 

* `respondent.outsideParty.id` FLOAT NULLABLE 

* `respondent.outsideParty.partyName` STRING NULLABLE 

* `respondent.outsideParty.phone` STRING NULLABLE 

* `respondent.outsideParty.state` STRING NULLABLE 

* `respondent.outsideParty.webSite` STRING NULLABLE 

* `respondent.outsideParty.zip` STRING NULLABLE 

* `respondent.respondentDisposition` RECORD REPEATED 

* `respondent.respondentDisposition.class` STRING NULLABLE 

* `respondent.respondentDisposition.dateDispositionByUnfairAct` STRING NULLABLE 

* `respondent.respondentDisposition.dateDispositionRespondent` STRING NULLABLE 

* `respondent.respondentDisposition.dateOfRemedialOrder` STRING NULLABLE 

* `respondent.respondentDisposition.dateStatusChanged` STRING NULLABLE 

* `respondent.respondentDisposition.dispositionByRespondent` STRING NULLABLE 

* `respondent.respondentDisposition.dispositionByRespondent_a` STRING NULLABLE 

* `respondent.respondentDisposition.dispositionByUnfairAct` STRING NULLABLE 

* `respondent.respondentDisposition.dispositionByUnfairAct_a` STRING NULLABLE 

* `respondent.respondentDisposition.id` FLOAT NULLABLE 

* `respondent.respondentDisposition.statusOfRemedialOrder` STRING NULLABLE 

* `respondent.respondentDisposition.statusOfRemedialOrder_a` STRING NULLABLE 

* `respondent.respondentDisposition.typeOfRemedialOrder` STRING NULLABLE 

* `respondent.respondentDisposition.typeOfRemedialOrder_a` STRING NULLABLE 

* `respondent.respondentRep` RECORD REPEATED 

* `respondent.respondentRep.class` STRING NULLABLE 

* `respondent.respondentRep.dateCreated` STRING NULLABLE 

* `respondent.respondentRep.id` FLOAT NULLABLE 

* `respondent.respondentRep.lastUpdated` STRING NULLABLE 

* `respondent.respondentRep.reportNotes` STRING NULLABLE 

* `respondent.respondentRep.reportTitle` STRING NULLABLE 

* `respondent.respondentRep.respondentRequirement` BOOLEAN NULLABLE 

* `scheduledEndDateEvidHear` STRING NULLABLE 

* `scheduledStartDateEvidHear` STRING NULLABLE 

* `startDateMarkmanHearing` STRING NULLABLE 

* `targetDate` STRING NULLABLE 

* `teoIdDueDate` STRING NULLABLE 

* `teoIdIssueDate` STRING NULLABLE 

* `teoProceedingInvolved` BOOLEAN NULLABLE 

* `teoReliefGranted` BOOLEAN NULLABLE 

* `title` STRING NULLABLE 

* `trademarkNumbers` RECORD REPEATED 

* `trademarkNumbers.activeDate` STRING NULLABLE 

* `trademarkNumbers.class` STRING NULLABLE 

* `trademarkNumbers.id` FLOAT NULLABLE 

* `trademarkNumbers.inactiveDate` STRING NULLABLE 

* `trademarkNumbers.trademarkNumber` STRING NULLABLE 






















































































































































































































































































































































































































*****
## patents-public-data:usitc_investigations.investigations_201710


Old table version `201710`, schema skipped.





*****
## patents-public-data:usitc_investigations.match



> US International Trade Commission 337Info Unfair Import Investigations Information System contains data on investigations done under Section 337. Section 337 declares the infringement of certain statutory intellectual property rights and other forms of unfair competition in import trade to be unlawful practices. Most Section 337 investigations involve allegations of patent or registered trademark infringement.
> 
> "US International Trade Commission 337Info Unfair Import Investigations Information System" by the USITC, for public use.





| Stat | Value |
|----------|----------|
| Last updated | 2017-10-22 |
| Rows | 1,420 |
| Size | 36.5 kB |

### Schema
[View in BigQuery](https://bigquery.cloud.google.com/table/patents-public-data:usitc_investigations.match)

* `patentNumber` STRING NULLABLE 

* `publication_number` STRING NULLABLE  joins on **publication_number**



### Join columns




#### publication_number

joins to `patents-public-data:patents.publications::publication_number` on **publication_number** (99.93%, 1,419 rows)

| Key | Percent | Rows | Sample values |
|------|-----|--------|--------------------------------------------------------|
| `all` | 99.93% | 1,419 | `['US-7828090-B2', 'US-6590365-B2', 'US-6459130-B1', 'US-7495453-B2', 'US-6674464-B1']` |


    #standardSQL
    SELECT
      COUNT(*) AS cnt,
      COUNT(second.second_column) AS second_cnt,
      ARRAY_AGG(first.publication_number IGNORE NULLS ORDER BY RAND() LIMIT 5) AS sample_value
    FROM `patents-public-data.usitc_investigations.match`AS first
    LEFT JOIN (
      SELECT publication_number AS second_column, COUNT(*) AS cnt
      FROM `patents-public-data.patents.publications`
      GROUP BY 1
    ) AS second ON first.publication_number = second.second_column



joins from `patents-public-data:patents.publications::publication_number` on **publication_number** (0.00%, 1,419 rows)






*****
## patents-public-data:usitc_investigations.match_201710


Old table version `201710`, schema skipped.





*****
## patents-public-data:worldbank_wdi.wdi_2016



> World Development Indicators Data is the primary World Bank collection of development indicators, compiled from officially-recognized international sources. It presents the most current and accurate global development data available, and includes national, regional and global estimates.
> 
> “World Development Indicators” by the World Bank, used under CC BY 3.0 IGO.





| Stat | Value |
|----------|----------|
| Last updated | 2017-02-07 |
| Rows | 21,759,408 |
| Size | 2.4 GB |

### Schema
[View in BigQuery](https://bigquery.cloud.google.com/table/patents-public-data:worldbank_wdi.wdi_2016)

* `year` INTEGER NULLABLE 

* `country_name` STRING NULLABLE 

* `country_code` STRING NULLABLE 

* `indicator_name` STRING NULLABLE 

* `indicator_code` STRING NULLABLE 

* `indicator_value` FLOAT NULLABLE 



















