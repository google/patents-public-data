# Copyright 2018 Google Inc. All Rights Reserved. Licensed under the Apache
# License, Version 2.0 (the "License"); you may not use this file except in
# compliance with the License. You may obtain a copy of the License at
# http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations under
# the License.
"""Model definition for the patent claim breadth model."""
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
import tensorflow as tf

# Count features created in ../preprocess.py
FEATURE_NAMES = [
    'word_cnt', 'word_cnt_unique', 'char_cnt', 'char_cnt_unique',
    'limiting_words_cnt', 'digits_or_decimal_cnt', 'atleastoneofand_cnt',
    'atleastoneofor_cnt', 'counting_cnt', 'excluding_words_cnt',
    'groupconsistingof_cnt', 'element_cnt', 'adding_words_cnt',
    'newline_tab_cnt'
]


def build_input_columns(embedding_dim, embedding_vocab_file):
  """Builds input columns for use with Tensorflow Estimator."""
  categorical = tf.feature_column.categorical_column_with_vocabulary_file(
      key='cpc4',
      vocabulary_file=embedding_vocab_file,
      num_oov_buckets=1,
  )
  cpc_embedding = tf.feature_column.embedding_column(
      categorical_column=categorical,
      dimension=embedding_dim
  )
  numeric_columns = [tf.feature_column.numeric_column(k) for k in FEATURE_NAMES]
  return [cpc_embedding] + numeric_columns


def build_estimator(config, hidden_units=None, learning_rate=0.001, dropout=0.1,
                    embedding_vocab_file=None, embedding_dim=25):
  """Builds an estimator for predicting patent claim complex."""
  input_columns = build_input_columns(embedding_dim, embedding_vocab_file)
  return tf.estimator.DNNClassifier(
      config=config,
      feature_columns=input_columns,
      hidden_units=hidden_units or [512, 256, 128],
      optimizer=tf.train.ProximalAdagradOptimizer(learning_rate=learning_rate),
      dropout=dropout
  )


def build_serving_fn():
  """Builds serving function based on Hparams."""
  def _json_serving_input_fn():
    inputs = {}
    for feat in FEATURE_NAMES:
      inputs[feat] = tf.placeholder(shape=[None], dtype=tf.float32)
    inputs['cpc4'] = tf.placeholder(shape=[None], dtype=tf.string)
    return tf.estimator.export.ServingInputReceiver(inputs, inputs)

  return _json_serving_input_fn


def input_fn(filespec, batch_size, num_epochs=None, shuffle=True):
  """Builds a TensorFlow input function for use with our model."""
  def _parse_example(example):
    """Parses a TF example protobuffer."""
    feature_spec = {
        'label': tf.FixedLenFeature([], tf.string),
        'cpc4': tf.FixedLenFeature([], tf.string),
        'publication_number': tf.FixedLenFeature([], tf.string),
    }
    for f in FEATURE_NAMES:
      feature_spec[f] = tf.FixedLenFeature([], tf.float32)
    features = tf.parse_single_example(example, feature_spec)
    labels = tf.to_int32(tf.equal(features.pop('label'), 'broad'))

    return features, labels

  filenames = tf.gfile.Glob(filespec)
  dataset = tf.data.TFRecordDataset(filenames, compression_type='GZIP')
  dataset = dataset.map(_parse_example)
  dataset = dataset.prefetch(batch_size * 5)
  dataset = dataset.batch(batch_size).repeat(num_epochs)
  if shuffle:
    dataset = dataset.shuffle(batch_size * 5)

  iterator = dataset.make_one_shot_iterator()
  batch_features, batch_labels = iterator.get_next()
  return batch_features, batch_labels
