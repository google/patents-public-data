# Copyright 2018 Google Inc. All Rights Reserved. Licensed under the Apache
# License, Version 2.0 (the "License"); you may not use this file except in
# compliance with the License. You may obtain a copy of the License at
# http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations under
# the License.

"""End-to-end test for the patent claim breadth model preprocessing code."""
import logging
import os
import shutil
import time
import unittest
from apache_beam.metrics.metric import MetricsFilter
from apache_beam.testing.pipeline_verifiers import PipelineStateMatcher
from apache_beam.testing.test_pipeline import TestPipeline
from hamcrest.core.core.allof import all_of
from nose.plugins.attrib import attr
import preprocess
import tensorflow as tf

# Assumes you've set an environmental variable for your GCP project. See README.
PROJECT = os.environ['GCP_PROJECT']


def read_example_proto(test_dir):
  filenames = tf.gfile.Glob(os.path.join(test_dir, '*.tfrecord.gz'))
  tf_opt = tf.python_io.TFRecordOptions(
      tf.python_io.TFRecordCompressionType.GZIP)
  record = next(tf.python_io.tf_record_iterator(filenames[0], options=tf_opt))
  example = tf.train.Example()
  example.ParseFromString(record)
  return example


def get_pipeline_metric(results, metric_name, index=0, result_type='counters'):
  metric_filter = MetricsFilter().with_name(metric_name)
  query_result = results.metrics().query(metric_filter)
  try:
    return query_result[result_type][index].committed
  except IndexError:
    logging.info(
        'No key in metrics for %s at index %s, returning 0', metric_name, index)
    return 0


def get_tf_feature(proto, feature_name, feature_type='float_list'):
  """Helper method to retrieve named features from a TF example proto."""
  return getattr(proto.features.feature[feature_name], feature_type).value[0]


def get_test_query(max_records):
  return '''
    #standardSQL
    with fake_applications as (
      SELECT
      'US-1234567-A1' as publication_number,
      substr(claims.text, 0, 2000) as fullclaim,
      2000 as priority_yr,
      'C08F' as cpc4,
      2003 as median_priority_yr
      FROM `patents-public-data.patents.publications` p
      ,UNNEST(claims_localized) claims
      WHERE claims.language = 'en'
      AND country_code = 'US'
      AND claims.text is not null
      AND FLOOR(priority_date / 10000) > 2005
      limit {half_max}
    )

    , fake_issued as (
      SELECT
      'US-1234567-B2' as publication_number,
      substr(claims.text, 0, 2000) as fullclaim,
      2012 as priority_yr,
      'C08F' as cpc4,
      2003 as median_priority_yr
      FROM `patents-public-data.patents.publications` p
      ,UNNEST(claims_localized) claims
      WHERE claims.language = 'en'
      AND country_code = 'US'
      AND claims.text is not null
      AND FLOOR(priority_date / 10000) > 2005
      limit {half_max}
    )

    select * from fake_applications
    union all
    select * from fake_issued
    '''.format(half_max=(max_records // 2))


class PreProcessE2E(unittest.TestCase):
  # Enable nose tests running in parallel
  _multiprocess_can_split_ = True
  OUTPUT_DIR = os.getcwd()
  TOTAL_RECORDS = 500
  TEST_QUERY = get_test_query(TOTAL_RECORDS)

  @attr('IT')
  def test_train_mode(self):
    """Runs pipeline in train mode outputting train, test and eval filesets."""
    test_pipeline = TestPipeline()
    # Set extra options to the pipeline for test purpose
    test_dir = os.path.join(self.OUTPUT_DIR, str(int(time.time())))
    self.addCleanup(shutil.rmtree, test_dir)

    # Checks that pipeline reaches state "Done"
    pipeline_verifiers = [PipelineStateMatcher()]
    extra_opts = {
        'project': PROJECT,
        'output_path': test_dir,
        'on_success_matcher': all_of(*pipeline_verifiers),
        'runner': 'DirectRunner',
    }

    res = preprocess.main(
        test_pipeline.get_full_options_as_args(**extra_opts),
        query=self.TEST_QUERY,
        await_completion=True
    )

    # Check counts coming out of GetFirstClaim step.
    parse_first_claim_cnt = get_pipeline_metric(res, 'parse_firstclaim_success')
    self.assertEqual(self.TOTAL_RECORDS, parse_first_claim_cnt)

    # Check counts coming out of AddFeatures step.
    add_features_cnt = get_pipeline_metric(res, 'create_features_success')
    self.assertEqual(self.TOTAL_RECORDS, add_features_cnt)

    # Check counts coming out of AddLabel step.
    broad_cnt = get_pipeline_metric(res, 'add_label_broad')
    narrow_cnt = get_pipeline_metric(res, 'add_label_narrow')
    self.assertEqual(self.TOTAL_RECORDS, broad_cnt + narrow_cnt)

    # Check if the number of records coming out of Train/Test = limit step.
    splits = ['train_cnt', 'eval_cnt', 'test_cnt']
    train_test_split_cnt = sum(
        [get_pipeline_metric(res, m) for m in splits]
    )
    self.assertEqual(self.TOTAL_RECORDS, train_test_split_cnt)

    # Check if number of protos created matched output of train/test split.
    create_proto_success = sum(
        [get_pipeline_metric(res, 'create_proto_success', index=i)
         for i in range(3)]
    )
    self.assertEqual(self.TOTAL_RECORDS, create_proto_success)

    # Open a tf Example and check fields.
    example = read_example_proto(test_dir)
    for feature_name in preprocess.FEATURE_NAMES:
      self.assertGreaterEqual(get_tf_feature(example, feature_name), 0)
    # Make sure label feature is present.
    labels = ['broad', 'narrow']
    self.assertIn(get_tf_feature(example, 'label', 'bytes_list'), labels)

  @attr('IT')
  def test_inference_mode(self):
    """Runs a pipeline in inference mode which should output one fileset."""
    test_pipeline = TestPipeline()
    # Set extra options to the pipeline for test purpose
    test_dir = os.path.join(self.OUTPUT_DIR, str(int(time.time())))
    self.addCleanup(shutil.rmtree, test_dir)

    # Checks that pipeline reaches state "Done"
    pipeline_verifiers = [PipelineStateMatcher()]
    extra_opts = {
        'project': PROJECT,
        'output_path': test_dir,
        'on_success_matcher': all_of(*pipeline_verifiers),
        'runner': 'DirectRunner',
        'pipeline_mode': 'inference',
    }

    res = preprocess.main(
        test_pipeline.get_full_options_as_args(**extra_opts),
        query=self.TEST_QUERY,
        await_completion=True
    )

    # Check counts coming out of GetFirstClaim step.
    parse_first_claim_cnt = get_pipeline_metric(res, 'parse_firstclaim_success')
    self.assertEqual(self.TOTAL_RECORDS, parse_first_claim_cnt)

    # Ensure a proto is created for all input records
    create_proto_success = get_pipeline_metric(res, 'create_proto_success')
    self.assertEqual(self.TOTAL_RECORDS, create_proto_success)

    # Open a tf Example and check fields.
    example = read_example_proto(test_dir)
    for feature_name in preprocess.FEATURE_NAMES:
      self.assertGreaterEqual(get_tf_feature(example, feature_name), 0)

    # Make sure label feature is not present since we are in inference.
    with self.assertRaises(IndexError):
      get_tf_feature(example, 'label', 'bytes_list')


if __name__ == '__main__':
  logging.getLogger().setLevel(logging.DEBUG)
  unittest.main()
