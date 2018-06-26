# Patent analysis using the Google Patents Public Datasets on BigQuery

The contents of this repository are not an official Google product.

[Google Patents Public Datasets](https://console.cloud.google.com/launcher/browse?q=google%20patents%20public%20datasets&filter=solution-type:dataset) is a collection of compatible BigQuery database tables from government, research and private companies for conducting statistical analysis of patent data. The data is available to be queried with SQL through BigQuery, joined with private datasets you upload, and exported and processed using many other compatible analysis tools. This repository is a centralized source for examples which use the data.

Currently the repo contains two examples:

1. [Patent Landscaping](https://github.com/google/patents-public-data/blob/master/models/landscaping/README.md):  A demo of an automated process of finding patents related to a particular topic given an initial seed set of patents. Based on the paper by Dave Feltenberger and Aaron Abood, [Automated Patent Landscaping](models/landscaping/AutomatedPatentLandscaping.pdf).

2. [Claim Text Extraction](https://github.com/google/patents-public-data/blob/master/examples/claim-text/claim_text_extraction.ipynb): A demo of interacting with patent claim text data using BigQuery and python.

3. [Claim Breadth Model](https://github.com/google/patents-public-data/blob/master/models/claim_breadth/README.md): A machine learning method for estimating patent claim breadth using data from BigQuery.

