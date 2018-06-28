# Copyright 2018 Google Inc. All Rights Reserved. Licensed under the Apache
# License, Version 2.0 (the "License"); you may not use this file except in
# compliance with the License. You may obtain a copy of the License at
# http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations under
# the License.
"""A batch inference script to score a set of Patent publications."""
import argparse
import datetime
import logging
import os
import sys
import apache_beam as beam
from apache_beam.metrics import Metrics
from apache_beam.options.pipeline_options import PipelineOptions
from googleapiclient.discovery import build
import tensorflow as tf

NOW = datetime.datetime.now().strftime('%Y%m%d-%H%M%S')
FEATURE_NAMES = [
    'word_cnt', 'word_cnt_unique', 'char_cnt', 'char_cnt_unique',
    'limiting_words_cnt', 'digits_or_decimal_cnt', 'atleastoneofand_cnt',
    'atleastoneofor_cnt', 'counting_cnt', 'excluding_words_cnt',
    'groupconsistingof_cnt', 'element_cnt', 'adding_words_cnt',
]


def default_args(argv):
  """Provides default values for Workflow flags."""
  parser = argparse.ArgumentParser()
  parser.add_argument(
      '--model_version_str',
      required=True,
      type=str,
      help='Path to ML Engine model like `MODEL_NAME/versions/VERSION`')
  parser.add_argument(
      '--input_file_pattern',
      required=True,
      type=str,
      help='Glob style file pattern to use for selecting input files.')
  parser.add_argument(
      '--output_path',
      required=True,
      help='Output directory to write results to if write_to_bigquery is false.'
           'for DataflowRunner use a GCS bucket.')
  parser.add_argument(
      '--output_prefix',
      default='us_patent_claim_scores',
      help='Prefix to use on sharded output files.')
  parser.add_argument(
      '--write_to_bigquery',
      default=False,
      help='If `True` output will be written directly to a bigquery table as'
           'specified by args.output_dataset args.output_table.'
  )
  parser.add_argument(
      '--output_dataset',
      help='Bigquery Dataset where output should be written if'
           'write_to_bigquery is true. Will be ignored otherwise.'
  )
  parser.add_argument(
      '--output_table',
      help='Bigquery Table name where output should be written if'
           'write_to_bigquery is true. Will be ignored otherwise.'
  )
  parser.add_argument(
      '--output_shards',
      default=10,
      help='Number of shards to write in output_path.')
  parser.add_argument(
      '--job_name',
      type=str,
      default='patent-claims-inference' + NOW,
      help='A unique job identifier.')
  parser.add_argument(
      '--num_workers',
      default=5,
      type=int,
      help='The max number of workers to use.')
  parser.add_argument(
      '--autoscaling_algorithm',
      default='NONE',
      help='Options are `NONE` or `THROUGHPUT_BASED`. Use None to prevent GCP'
           'from scaling down to 1 worker due to API throughput.'
  )
  parser.add_argument(
      '--runner',
      default='DirectRunner',
      choices=['DataflowRunner', 'DirectRunner'],
      help='Option to run locally or on GCP, for other options see Beam docs.')
  parser.add_argument(
      '--project',
      type=str,
      help='The cloud project name to be used for running this pipeline with'
           'the DataflowRunner option')

  parsed_args, _ = parser.parse_known_args(argv)

  if parsed_args.runner == 'DataflowRunner':
    if not parsed_args.project:
      msg = 'If running with DataflowRunner please provide a GCP project.'
      raise argparse.ArgumentTypeError(msg)

  # Check the output flags when writing to BigQuery.
  if parsed_args.write_to_bigquery:
    if not parsed_args.output_dataset:
      msg = ('When writing to Bigquery, you must specify --output_dataset and '
             '--output_table flags.')
      raise argparse.ArgumentTypeError(msg)

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


def get_tf_feature(proto, feature_name, feature_type='float_list'):
  """Helper method to retrieve named features from a TF example proto."""
  return getattr(proto.features.feature[feature_name], feature_type).value[0]


class RunInference(beam.DoFn):
  """Loads saved model and scores inputs."""

  def __init__(self, model_endpoint):
    self.success_cnt = Metrics.counter('main', 'inference_success')
    self.model_endpoint = model_endpoint
    self.ml_service = build('ml', 'v1')

  def process(self, element):
    """Scores the model using the TF Example input."""
    ex = tf.train.Example.FromString(element)
    instance = {ftr: get_tf_feature(ex, ftr) for ftr in FEATURE_NAMES}
    instance['cpc4'] = get_tf_feature(ex, 'cpc4', 'bytes_list')

    response = self.ml_service.projects().predict(
        name=self.model_endpoint,
        body={'instances': [instance]}
    ).execute()

    broad_score = response['predictions'][0]['probabilities'][0]

    # Pull the publication number from the TF Example proto.
    pub_number = ex.features.feature['publication_number'].bytes_list.value[0]
    self.success_cnt.inc()
    yield {'publication_number': pub_number, 'broad_score': float(broad_score)}


def format_output(element):
  """Converts dictionary element into a CSV style output."""
  pub_number = element.get('publication_number')
  broad_score = element.get('broad_score')
  return '{0},{1:05f}'.format(pub_number, broad_score)


def main(argv, await_completion=False):
  """Runs the batch inference pipeline."""
  opt = default_args(argv)
  logging.info('Starting pipeline with args: %s', vars(opt))
  pipeline_options = PipelineOptions().from_dictionary(vars(opt))
  p = beam.Pipeline(options=pipeline_options)
  output_base = os.path.join(opt.output_path, opt.output_prefix)
  model_endpoint = 'projects/{}/models/{}'.format(
      opt.project, opt.model_version_str)
  data = (p
          | 'ReadTFRecords' >> beam.io.ReadFromTFRecord(opt.input_file_pattern)
          | 'RunInference' >> beam.ParDo(RunInference(model_endpoint))
         )

  if opt.write_to_bigquery:
    _ = data | 'WriteToBigquery' >> beam.io.gcp.bigquery.WriteToBigQuery(
        table=opt.output_table,
        dataset=opt.output_dataset,
        project=opt.project,
        write_disposition=beam.io.gcp.bigquery.BigQueryDisposition.WRITE_APPEND,
        schema='publication_number:STRING,broad_score:FLOAT'
    )
  else:
    # Format a CSV style output and write to text.
    formatted = data | 'FormatTextOutput' >> beam.Map(format_output)
    _ = formatted | 'WriteToText' >> beam.io.WriteToText(
        file_path_prefix=output_base,
        num_shards=int(opt.output_shards)
    )

  result = p.run()
  print('Pipeline running. visit https://console.cloud.google.com/dataflow to '
        'monitor progress.')
  if await_completion:
    result.wait_until_finish()
    return result


if __name__ == '__main__':
  main(sys.argv[1:])
