# Copyright 2018 Google Inc. All Rights Reserved. Licensed under the Apache
# License, Version 2.0 (the "License"); you may not use this file except in
# compliance with the License. You may obtain a copy of the License at
# http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations under
# the License.
"""End-to-end test for the patent claim model batch inference script."""
import logging
import os
import shutil
import time
import unittest
from apache_beam.metrics.metric import MetricsFilter
from apache_beam.testing.pipeline_verifiers import PipelineStateMatcher
from apache_beam.testing.test_pipeline import TestPipeline
import batch_inference
from hamcrest.core.core.allof import all_of
from nose.plugins.attrib import attr

# Assumes your project and model versions are set as ENV variables. See README.
PROJECT = os.environ['GCP_PROJECT']
MODEL_VERSION_STR = os.environ['MODEL_VERSION_STR']


def get_pipeline_metric(pipeline_results, metric_name, index=0,
                        result_type='counters'):
  """Attempts to return a metrics from an Apache Beam PipelineResults."""
  metrics_filter = MetricsFilter().with_name(metric_name)
  query_result = pipeline_results.metrics().query(metrics_filter)
  try:
    return query_result[result_type][index].committed
  except IndexError:
    logging.info(
        'No key in metrics for %s at index %s, returning 0', metric_name, index)
    return 0


class BatchInferenceE2E(unittest.TestCase):
  _multiprocess_can_split_ = True
  OUTPUT_DIR = os.getcwd()
  TEST_DATA_GLOB = os.path.join(OUTPUT_DIR, 'testdata', '*.tfrecord.gz')
  TOTAL_RECORDS_IN_TEST_DATA = 17

  @attr('IT')
  def test_text_file_output(self):
    test_pipeline = TestPipeline()
    # Checks that pipeline reaches state "Done"
    pipeline_verifiers = [PipelineStateMatcher()]

    # Set extra options to the pipeline for test purpose
    test_dir = os.path.join(self.OUTPUT_DIR, str(int(time.time())))
    extra_opts = {
        'project': PROJECT,
        'model_version_str': MODEL_VERSION_STR,
        'input_file_pattern': self.TEST_DATA_GLOB,
        'output_path': test_dir,
        'runner': 'DirectRunner',
        'output_shards': 1,
        'on_success_matcher': all_of(*pipeline_verifiers),
    }

    # Add cleanup for testdir
    self.addCleanup(shutil.rmtree, test_dir)

    result = batch_inference.main(
        test_pipeline.get_full_options_as_args(**extra_opts),
        await_completion=True
    )

    records_scored = get_pipeline_metric(result, 'inference_success')
    self.assertEqual(records_scored, self.TOTAL_RECORDS_IN_TEST_DATA)


if __name__ == '__main__':
  logging.getLogger().setLevel(logging.DEBUG)
  logging.info('Running with MODEL: %s', MODEL_VERSION_STR)
  unittest.main()
