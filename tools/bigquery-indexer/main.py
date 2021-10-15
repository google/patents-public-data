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
"""

import sys

import argparse

import apache_beam as beam

from google.cloud import bigquery

# The additional column suffixes added to each input row containing 'smiles'.
fingerprint_columns = set(['morgan_fp', 'rdkit_fp', 'atompair_fp', 'tt_fp'])

def index_row(row, skip_cols):
  orig_keys = list(row.keys())
  for key in orig_keys:
    if 'smiles' in key and key not in skip_cols:
      fingerprints = generate_fingeprints(row[key])
      for col, fp in fingerprints.items():
        if col not in fingerprint_columns:
          raise RuntimeError(f'fingerprints generated column {col} not in {fingerprint_columns}')
        row[f'{key}_{col}'] = fp
  return row

def generate_fingeprints(smiles):
  # Load these here so they're only needed on the worker machines.
  from rdkit import Chem
  from rdkit.Chem import rdFingerprintGenerator

  morgan_fp = ''
  rdkit_fp = ''
  atompair_fp = ''
  tt_fp = ''

  try:
    mol = Chem.MolFromSmiles(smiles)

    # Morgan
    morgan_fp = rdFingerprintGenerator.GetMorganGenerator().GetFingerprint(mol).ToBase64()

    # Feature Morgan
    # TODO

    # RDKit
    rdkit_fp = rdFingerprintGenerator.GetRDKitFPGenerator().GetFingerprint(mol).ToBase64()

    # Layered
    # TODO

    # Atom pairs
    atompair_fp = rdFingerprintGenerator.GetAtomPairGenerator().GetFingerprint(mol).ToBase64()

    # MACCS
    # TODO

    # Topological Torsion
    tt_fp = rdFingerprintGenerator.GetTopologicalTorsionGenerator().GetFingerprint(mol).ToBase64()

    # Pattern
    # TODO

    # E-state
    # TODO

  except Exception as e:
    print(f'Exception {e} processing {smiles}')
    return {}
  # NOTE: add any new fingerprints to fingerprint_columns.
  return {'morgan_fp': morgan_fp, 'rdkit_fp': rdkit_fp, 'atompair_fp': atompair_fp, 'tt_fp': tt_fp}

def get_query_output_schema(bq_client, query):
  try:
    # TODO: add support for accessing the schema to bq_client.query().
    result = bq_client._connection.api_request(
      method="POST",
      path="/projects/jefferson-1790/queries",
      data={
        "query": query,
        "dryRun": True,
        "useLegacySql": False,
      })
  except Exception as exc:
    raise ValueError(f'Error testing SQL query "{query}"') from exc
  return result['schema']

def add_fingerprint_schema(orig_schema, skip_cols):
  to_add = []
  for field in orig_schema['fields']:
    key = field['name']
    if 'smiles' in key and key not in skip_cols:
      for fp_col in fingerprint_columns:
        to_add.append({
          'name': f'{key}_{fp_col}',
          'type': 'BYTES',
          'mode': 'NULLABLE',
        })

  return {'fields': orig_schema['fields'] + to_add}

def run(argv=None):  # pylint: disable=missing-docstring
  parser = argparse.ArgumentParser()

  parser.add_argument(
      '--input_sql',
      dest='input_sql',
      default='',
      help='SQL statement to extract SMILES from. Fields containing `smiles` '
           'will generate fingerprints, and any additional fields will be '
           'passed through to the output row.')
  parser.add_argument(
      '--output_table',
      dest='output_table',
      required=True,
      help='Output BigQuery table with indexed chemistry.')
  parser.add_argument(
      '--skip_fingerprint_columns',
      dest='skip_fingerprint_columns',
      default=[],
      help='Column names to skip fingerprinting.')
  known_args, pipeline_args = parser.parse_known_args(argv)

  skip_cols = set(known_args.skip_fingerprint_columns.split(','))

  # Query the output schema first so we know the schema to set.
  bq_client = bigquery.Client()

  # Get the output schema.
  orig_schema = get_query_output_schema(bq_client, known_args.input_sql)
  # Add the new fingerprint columns to the schema.
  schema = add_fingerprint_schema(orig_schema, skip_cols)

  print(f'Output schema: {schema}')

  with beam.Pipeline(argv=pipeline_args) as p:
    input_rows = (p | 'Read' >> beam.io.Read(beam.io.ReadFromBigQuery(
        query=known_args.input_sql,
        use_standard_sql=True)))

    # Each row is a dictionary where the keys are the BigQuery columns
    fingerprints = input_rows | beam.Map(
        lambda row: index_row(row, skip_cols))

    (fingerprints | 'Write' >> beam.io.WriteToBigQuery(
        known_args.output_table,
        schema=schema,
        write_disposition=beam.io.BigQueryDisposition.WRITE_TRUNCATE,
        create_disposition=beam.io.BigQueryDisposition.CREATE_IF_NEEDED))


if __name__ == "__main__":
  run(sys.argv)
