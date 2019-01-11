# Copyright 2017 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix

import keras
from keras.models import Sequential, Model
from keras.layers import Dense, Input, Embedding, BatchNormalization, ELU, Concatenate
from keras.layers import LSTM, Conv1D, MaxPooling1D
from keras.layers.merge import concatenate
from keras.layers.core import Dropout
from keras_metrics import precision, recall, f1score

import matplotlib.pyplot as plt
import os
import pandas as pd
import seaborn as sn

class LandscapeModel:
    target_names = ['seed', 'antiseed']
    tf_model = None
    td = None
    data_path = None
    seed_name = None

    def __init__(self, training_data, data_path, seed_name):
        self.tf_model = None
        self.td = training_data
        self.data_path = data_path
        self.seed_name = seed_name

    def wire_model_functional(self, lstm_size, dropout_pct, sequence_len):
        print('Building Functional model.')

        refs_input = Input(shape=(self.td.trainRefsOneHotX.shape[1],), name='refs_input')
        refs = Dense(
                256,
                input_dim=self.td.trainRefsOneHotX.shape[1],
                activation=None)(refs_input)
        refs = Dropout(dropout_pct)(refs)
        refs = BatchNormalization()(refs)
        refs = ELU()(refs)
        refs = Dense(64, activation=None)(refs)
        refs = Dropout(dropout_pct)(refs)
        refs = BatchNormalization()(refs)
        refs = ELU()(refs)

        cpcs_input = Input(shape=(self.td.trainCpcOneHotX.shape[1],), name='cpcs_input')
        cpcs = Dense(
                32,
                input_dim=self.td.trainCpcOneHotX.shape[1],
                activation=None)(cpcs_input)
        cpcs = Dropout(dropout_pct)(cpcs)
        cpcs = BatchNormalization()(cpcs)
        cpcs = ELU()(cpcs)

        # Use pre-trained Word2Vec embeddings
        embedding_layer_input = Input(shape=(sequence_len,), name='embed_input')
        embedding_layer = Embedding(self.td.w2v_runtime.embedding_weights.shape[0],
                                    self.td.w2v_runtime.embedding_weights.shape[1],
                                    weights=[self.td.w2v_runtime.embedding_weights],
                                    input_length=sequence_len,
                                    trainable=False)(embedding_layer_input)
        deep = LSTM(
            lstm_size,
            dropout=dropout_pct,
            recurrent_dropout=dropout_pct,
            return_sequences=False,
            name='LSTM_1')(embedding_layer)
        deep = Dense(300, activation=None)(deep)
        deep = Dropout(dropout_pct)(deep)
        deep = BatchNormalization()(deep)
        deep = ELU()(deep)

        #model_inputs_to_concat = [cpcs, refs, deep]
        model_inputs_to_concat = [refs, deep]

        final_layer = Concatenate(name='concatenated_layer')(model_inputs_to_concat)
        output = Dense(64, activation=None)(final_layer)
        output = Dropout(dropout_pct)(output)
        output = BatchNormalization()(output)
        output = ELU()(output)
        output = Dense(1, activation='sigmoid')(output)

        #model = Model(inputs=[cpcs_input, refs_input, embedding_layer_input], outputs=output, name='model')
        model = Model(inputs=[refs_input, embedding_layer_input], outputs=output, name='model')
        model.compile(loss='binary_crossentropy',
                      optimizer='adam',
                      metrics=['accuracy', precision, recall, f1score])

        self.tf_model = model
        print('Done building graph.')
        print(self.tf_model.summary())

    def train_model(self, model, batch_size, num_epochs=5):
        print('Training model.')
        model.fit(x={
            'refs_input': self.td.trainRefsOneHotX,
            'embed_input': self.td.padded_train_embed_x,
            'cpcs_input': self.td.trainCpcOneHotX},
                  y=self.td.trainY,
                  batch_size=batch_size,
                  epochs=num_epochs,
                  validation_data=(
                      {
                          'refs_input': self.td.testRefsOneHotX,
                          'cpcs_input': self.td.testCpcOneHotX,
                          'embed_input': self.td.padded_test_embed_x},
                      self.td.testY))
        return model

    def train_or_load_model(self, batch_size, num_epochs=5):
        model_dir = os.path.join(self.data_path, self.seed_name)
        model_path = os.path.join(model_dir, 'model.pb')

        if os.path.exists(model_path):
            print('Model exists at {}; loading existing trained model.'.format(model_path))
            self.tf_model = keras.models.load_model(
                model_path,
                custom_objects={'precision': precision, 'recall': recall, 'fmeasure': f1score})
        else:
            print('Model has not been trained yet.')
            tf_model = self.train_model(self.tf_model, batch_size, num_epochs)
            print('Saving model to {}'.format(model_path))
            if not os.path.exists(model_dir):
                os.makedirs(model_dir)

            tf_model.save(model_path)
            print('Model persisted and ready for inference!')

    def evaluate_model(self, batch_size):
        score, acc, p, r, f1 = self.tf_model.evaluate(
            x={
                'refs_input': self.td.testRefsOneHotX,
                'cpcs_input': self.td.testCpcOneHotX,
                'embed_input': self.td.padded_test_embed_x
            },
            y=self.td.testY,
            batch_size=batch_size)

        print('')
        print('Test score: {:.4f}'.format(score))
        print('Test accuracy: {:.4f}'.format(acc))
        print('Test p/r (f1): {:.2f}/{:.2f} ({:.2f})'.format(p, r, f1))

        return (score, acc, p, r, f1)

    def batch_predict(self, padded_text_embeddings, refs_one_hot, cpcs_one_hot):
        return self.tf_model.predict(
            {
                'embed_input': padded_text_embeddings,
                'cpcs_input': cpcs_one_hot,
                'refs_input': refs_one_hot
            })

    def predict(self, train_data_util, text, refs, cpcs):
        '''
        '''

        adhoc_text = pd.Series([text])
        adhoc_refs = pd.Series([refs])
        adhoc_cpcs = pd.Series([cpcs])

        padded_text_embeddings, refs_one_hot, cpcs_one_hot = \
            train_data_util.prep_for_inference(adhoc_text, adhoc_refs, adhoc_cpcs)

        return self.batch_predict(padded_text_embeddings, refs_one_hot, cpcs_one_hot)

    def binary_prediction_idx(self, score):
        if score < .5:
            return 0
        return 1

    def label_to_idx(self, label):
        label = label.lower()
        for i in range(0, len(self.target_names)):
            if label == self.target_names[i]:
                return i
        raise ValueError('Label {} has no target name from [{}]'.format(label, self.target_names))

    def reports(self, prediction_df):
        binary_predictions_x = prediction_df.score.apply(self.binary_prediction_idx)
        actual_labels_y = prediction_df.label.apply(self.label_to_idx)

        cr = classification_report(binary_predictions_x, actual_labels_y, target_names=self.target_names)
        cm = confusion_matrix(binary_predictions_x, actual_labels_y)

        return cr, cm

    def show_confusion_matrix(self, confusion_matrix):
        cm_df = pd.DataFrame(confusion_matrix)
        plt.figure(figsize = (10,7))
        sn.heatmap(cm_df, xticklabels=self.target_names, yticklabels=self.target_names)
