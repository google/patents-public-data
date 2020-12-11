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

import argparse

import apache_beam as beam

from rdkit import Chem
from rdkit.Chem import rdMolDescriptors

def index_row(key, smiles):
  err = ''
  morgan_fp = ''

  try:
    mol = Chem.MolFromSmiles(smiles)
    fp = rdMolDescriptors.GetMorganFingerprintAsBitVect(mol, radius=2)
    morgan_fp = fp.ToBase64()
  except Exception as e:
    err = f'Exception {e} processing {smiles}'
  return {'key': key, 'morgan_fp': morgan_fp, 'error': err}


def run(argv=None):  # pylint: disable=missing-docstring
  parser = argparse.ArgumentParser()

  parser.add_argument(
      '--input_sql',
      dest='input_sql',
      default='',
      help='SQL statement to extract SMILES and row ID from. These values must be labeled `smiles` and `id`.')
  parser.add_argument(
      '--output_table',
      dest='output_table',
      required=True,
      help='Output BigQuery table with indexed chemistry.')
  known_args, pipeline_args = parser.parse_known_args(argv)

  with beam.Pipeline(argv=pipeline_args) as p:
    (
    p
    | 'Read' >> beam.io.Read(beam.io.BigQuerySource(
        query=known_args.input_sql,
        use_standard_sql=True))
    # Each row is a dictionary where the keys are the BigQuery columns
    | beam.Map(lambda row: index_row(row['key'], row['smiles']))
    | 'Write' >> beam.io.WriteToBigQuery(
        known_args.output_table,
        schema='key:STRING, morgan_fp:BYTES, error:STRING',
        write_disposition=beam.io.BigQueryDisposition.WRITE_TRUNCATE,
        create_disposition=beam.io.BigQueryDisposition.CREATE_IF_NEEDED))

