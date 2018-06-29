# Copyright 2018 Google Inc. All Rights Reserved. Licensed under the Apache
# License, Version 2.0 (the "License"); you may not use this file except in
# compliance with the License. You may obtain a copy of the License at
# http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations under
# the License.
"""Experiment definition for the patent claim breadth model."""
import argparse
import tensorflow as tf
from tensorflow.contrib.training.python.training import hparam
import trainer.model as model


def parse_args():
  """Parses command line arguements."""
  parser = argparse.ArgumentParser()
  # Input Arguments
  parser.add_argument(
      '--train-files',
      help='GCS or local paths to training data',
      nargs='+',
      required=True
  )
  parser.add_argument(
      '--eval-files',
      help='GCS or local paths to evaluation data',
      nargs='+',
      required=True
  )
  parser.add_argument(
      '--job-dir',
      help='GCS location to write checkpoints and export models',
      required=True,
  )

  # Training arguments - hparams which can be tuned.
  parser.add_argument(
      '--dropout',
      help='Dropout between layers in DNN.',
      default=0.35,
      type=float
  )
  parser.add_argument(
      '--learning-rate',
      help='Learning rate for the optimizer.',
      default=0.01,
      type=float
  )
  parser.add_argument(
      '--first-layer-size',
      help='Number of nodes in the first layer of the DNN',
      default=7500,
      type=int
  )
  parser.add_argument(
      '--num-layers',
      help='Number of layers in the DNN',
      default=1,
      type=int
  )
  parser.add_argument(
      '--scale-factor',
      help='How quickly should the size of the layers in the DNN decay',
      default=0.8,
      type=float
  )
  parser.add_argument(
      '--cpc-embedding-vocab-file',
      help='GCS path to a text file with one CPC4 per line. Any CPC4 codes not'
           'included will be mapped to a single UNK bucket. See README.',
      required=True,
      type=str
  )
  parser.add_argument(
      '--cpc-embedding-dim',
      help='Size of the learned embedding column to represent CPC codes.',
      default=85,
      type=int
  )

  # Experiment arguments
  parser.add_argument(
      '--train-steps',
      help='Steps to run the training job before exiting.',
      type=int,
      default=30000
  )
  parser.add_argument(
      '--train-batch-size',
      help='Batch size for training steps',
      type=int,
      default=512
  )
  parser.add_argument(
      '--eval-batch-size',
      help='Batch size for evaluation steps',
      type=int,
      default=512
  )
  parser.add_argument(
      '--eval-secs',
      help='Time between evaluations.',
      type=int,
      default=120
  )
  parser.add_argument(
      '--eval-steps',
      help='Number of steps to run evalution for at each checkpoint',
      default=100,
      type=int
  )
  parser.add_argument(
      '--verbosity',
      choices=['DEBUG', 'ERROR', 'FATAL', 'INFO', 'WARN'],
      default='INFO',
  )
  return parser.parse_args()


def main(hparams):
  """Run the training and evaluate using the high level API."""

  trn_input = lambda: model.input_fn(
      hparams.train_files,
      batch_size=hparams.train_batch_size
  )
  train_spec = tf.estimator.TrainSpec(trn_input, max_steps=hparams.train_steps)

  eval_input = lambda: model.input_fn(
      hparams.eval_files,
      batch_size=hparams.eval_batch_size,
  )

  # Construct our JSON serving function for Online Predictions using GCP.
  exporter = tf.estimator.FinalExporter('model', model.build_serving_fn())
  eval_spec = tf.estimator.EvalSpec(
      eval_input,
      throttle_secs=hparams.eval_secs,
      steps=hparams.eval_steps,
      exporters=[exporter],
  )

  run_config = tf.estimator.RunConfig()
  run_config = run_config.replace(model_dir=hparams.job_dir)
  # Construct layers sizes with exponential decay
  hidden_units = [
      max(2, int(hparams.first_layer_size * hparams.scale_factor**i))
      for i in range(hparams.num_layers)
  ]
  estimator = model.build_estimator(
      config=run_config,
      hidden_units=hidden_units,
      learning_rate=hparams.learning_rate,
      dropout=hparams.dropout,
      embedding_vocab_file=hparams.cpc_embedding_vocab_file,
      embedding_dim=hparams.cpc_embedding_dim,
  )
  tf.estimator.train_and_evaluate(estimator, train_spec, eval_spec)


if __name__ == '__main__':
  args = parse_args()
  tf.logging.set_verbosity(args.verbosity)
  hyperparams = hparam.HParams(**args.__dict__)
  main(hyperparams)
