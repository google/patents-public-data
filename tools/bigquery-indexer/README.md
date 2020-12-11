# BigQuery column indexer

This tool supports indexing and normalizing various columns in BigQuery tables.
It reads an input BigQuery SQL statement to select the columns and outputs a new
BigQuery table with the indexed columns.

## Installation

See https://cloud.google.com/dataflow/docs/quickstarts/quickstart-python,
specifically setting GOOGLE_APPLICATION_CREDENTIALS is required.

# Running

This example indexes a column containing SMILES (the computer representation of a chemical).

```$ python3 -m main   --region us-west1   --input_sql "SELECT DISTINCT smiles AS key, smiles FROM patents-public-data.google_patents_research.annotations_grouped WHERE inchi_key != ''"   --output_table <BigQuery.table.path>   --runner DataflowRunner   --project <project_id>   --temp_location gs://<cloud storage bucket>/tmp/ --setup_file ./setup.py --disk_size_gb=50 --machine_type=n2-highcpu-16```
