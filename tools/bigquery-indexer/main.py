"""
Copyright 2020 Google LLC

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    https://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

"""
Index/normalize/match various columns in BigQuery tables.

Supports:
* chemistry (SMILES) column fingerprinting for similarity search
* (future) patent publication and application number normalization
* (future) OCID matching


$ python3 -m main   --region us-west1   --input_sql "SELECT DISTINCT smiles AS key, smiles FROM patents-public-data.google_patents_research.annotations_grouped WHERE inchi_key != ''"   --output_table <BigQuery.table.path>   --runner DataflowRunner   --project <project_id>   --temp_location gs://<cloud storage bucket>/tmp/ --setup_file ./setup.py --disk_size_gb=50 --machine_type=n2-highcpu-16
"""

import sys

import indexer

if __name__ == "__main__":
  indexer.run(sys.argv)

