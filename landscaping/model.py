from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix

import keras
from keras.models import Sequential
from keras.layers import Dense, Embedding, BatchNormalization, ELU
from keras.layers import LSTM, Conv1D, MaxPooling1D, Merge
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

    def wire_model(self, lstm_size, dropout_pct):

        print('Building model graph...')

        refs = Sequential()
        refs.add(
            Dense(
                256,
                input_dim=self.td.trainRefsOneHotX.shape[1],
                name='refs',
                activation=None))
        refs.add(Dropout(dropout_pct))
        refs.add(BatchNormalization())
        refs.add(ELU())
        refs.add(Dense(64, activation=None))
        refs.add(Dropout(dropout_pct))
        refs.add(BatchNormalization())
        refs.add(ELU())

        cpcs = Sequential()
        cpcs.add(
            Dense(
                32,
                input_dim=self.td.trainCpcOneHotX.shape[1],
                name='cpcs',
                activation=None))
        cpcs.add(Dropout(.8))
        cpcs.add(BatchNormalization())
        cpcs.add(ELU())

        deep = Sequential()

        # Use pre-trained Word2Vec embeddings
        embedding_layer = Embedding(self.td.w2v_runtime.embedding_weights.shape[0],
                                    self.td.w2v_runtime.embedding_weights.shape[1],
                                    weights=[self.td.w2v_runtime.embedding_weights],
                                    #input_length=sequence_len,
                                    trainable=False,
                                    name='embed')
        deep.add(embedding_layer)
        '''
        model.add(Conv1D(filters,
                         kernel_size,
                         padding='valid',
                         activation='relu',
                         strides=1))
        model.add(MaxPooling1D(pool_size=pool_size))
        '''
        deep.add(LSTM(
            lstm_size,
            dropout=dropout_pct,
            recurrent_dropout=dropout_pct,
            return_sequences=False,
            name='LSTM_1'))
        #model.add(LSTM(256, dropout=0.2, recurrent_dropout=0.2, return_sequences=False, name='LSTM_2'))
        deep.add(Dense(300, activation=None))
        deep.add(Dropout(dropout_pct))
        deep.add(BatchNormalization())
        deep.add(ELU())


        model = Sequential()
        #model = deep
        #model.add(concatenate([refs, deep], axis=1))
        model.add(Merge([refs, deep], mode='concat', concat_axis=1))
        model.add(Dense(64, activation=None))
        model.add(Dropout(dropout_pct))
        model.add(BatchNormalization())
        model.add(ELU())
        model.add(Dense(1, activation='sigmoid'))

        # try using different optimizers and different optimizer configs
        model.compile(loss='binary_crossentropy',
                      optimizer='adam',
                      metrics=['accuracy', precision, recall, f1score])

        self.tf_model = model
        print('Done building graph.')
        print(self.tf_model.summary())


    def train_model(self, model, batch_size):
        print('Training model.')
        model.fit(x={
            'refs_input': self.td.trainRefsOneHotX,
            'embed_input': self.td.padded_train_embed_x,
            'cpcs_input': self.td.trainCpcOneHotX},
                  y=self.td.trainY,
                  batch_size=batch_size,
                  epochs=5,
                  validation_data=(
                      {
                          'refs_input': self.td.testRefsOneHotX,
                          'cpcs_input': self.td.testCpcOneHotX,
                          'embed_input': self.td.padded_test_embed_x},
                      self.td.testY))
        return model

    def train_or_load_model(self, batch_size):
        model_dir = os.path.join(self.data_path, self.seed_name)
        model_path = os.path.join(model_dir, 'model.pb')

        if os.path.exists(model_path):
            print('Model exists at {}; loading existing trained model.'.format(model_path))
            self.tf_model = keras.models.load_model(
                model_path,
                custom_objects={'precision': precision, 'recall': recall, 'fmeasure': f1score})
        else:
            print('Model has not been trained yet.')
            tf_model = self.train_model(self.tf_model, batch_size)
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
