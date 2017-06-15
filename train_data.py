import tokenizer
import importlib
import random
import numpy as np

from keras.preprocessing import sequence

importlib.reload(tokenizer)

class LandscapeTrainingData:
    RAND_SEED=314159
    refs_vocab_size = 50000
    training_df = None
    series_text_to_embed = None
    prepped_embedding_train = None
    prepped_refs = None
    prepped_labels = None
    w2v_runtime = None
    ref_to_id = None
    id_to_ref = None
    tokenizer = None

    def __init__(
        self, training_df, w2v_runtime):
        '''
        '''

        self.w2v_runtime = w2v_runtime
        self.training_df = training_df

        self.tokenizer = tokenizer.TextTokenizer()

    def label_text_to_id(self, label_name):
        if label_name == 'antiseed':
            return 1
        else:
            return 0

    def label_id_to_text(self, label_idx):
        if label_idx == 1:
            return 'antiseed'
        else:
            return 'seed'

    def label_series_to_index(self, labels_series):
        labels_indexed = []
        for idx in range(0, len(labels_series)):
            label = labels_series[idx]
            # 'tokenize' on the label is basically normalizing it
            tokenized_label = self.tokenizer.tokenize(label)[0]
            label_idx = self.label_text_to_id(tokenized_label)
            labels_indexed.append(label_idx)

        return labels_indexed
        
    def text_series_to_embeddings(self, raw_series_text):
        '''
        Takes as input a series of text and associated labels
        '''

        tokenized_text = self.tokenizer.tokenize_series(raw_series_text)
        word_to_index_dict = self.w2v_runtime.word_to_index
        tokenized_indexed_text = []

        for idx in range(0, len(tokenized_text)):
            text = tokenized_text[idx]
            text_word_indexes = []
            for word in text:
                if word in word_to_index_dict:
                    word_idx = word_to_index_dict[word]
                else:
                    word_idx = word_to_index_dict['UNK']
                # this skips 'the' so it can be used for dynamic rnn
                if word_idx > 0:
                    text_word_indexes.append(word_idx)

            tokenized_indexed_text.append(text_word_indexes)

        return tokenized_indexed_text

    def to_text(self, integerized):
        words = []
        for word_int in integerized:
            words.append(self.w2v_runtime.index_to_word[word_int])
        return ' '.join(words)

    def randomize(self, percent_train):
        training_data_to_shuffle = list(
            zip(
                self.prepped_embedding_train,
                self.refs_one_hot,
                self.cpc_one_hot,
                self.prepped_labels))

        print('Randomizing training data')
        random.seed(self.RAND_SEED)
        random.shuffle(training_data_to_shuffle)

        train_embed_arr, refs_one_hot, cpc_one_hot, label_arr = zip(*training_data_to_shuffle)

        train_idx = int(len(train_embed_arr) * percent_train)

        print('Creating NumPy arrays for train/test set out of randomized training data.')
        self.trainEmbedX = np.array(train_embed_arr[:train_idx])
        self.trainRefsOneHotX = np.array(refs_one_hot[:train_idx])
        self.trainCpcOneHotX = np.array(cpc_one_hot[:train_idx])

        self.testEmbedX = np.array(train_embed_arr[train_idx:])
        self.testRefsOneHotX = np.array(refs_one_hot[train_idx:])
        self.testCpcOneHotX = np.array(cpc_one_hot[train_idx:])

        self.trainY = np.array(label_arr[:train_idx])
        self.testY = np.array(label_arr[train_idx:])
    
    def prepare_training_data(
        self, series_text_to_embed, percent_train, refs_vocab_size, cpc_vocab_size):

        self.series_text_to_embed = series_text_to_embed
        self.prepped_embedding_train = self.text_series_to_embeddings(self.series_text_to_embed)
        self.prepped_labels = self.label_series_to_index(self.training_df.ExpansionLevel)
        self.refs_tokenizer, self.refs_one_hot = \
            self.tokenizer.tokenize_to_onehot_matrix(self.training_df.refs, refs_vocab_size)
        self.cpc_tokenizer, self.cpc_one_hot = \
            self.tokenizer.tokenize_to_onehot_matrix(self.training_df.cpcs, cpc_vocab_size)

        self.randomize(percent_train)

        print('Train (embed) data shapes: train: {}, train labels shape: {}'.format(
            self.trainEmbedX.shape, self.trainY.shape))
        print('Test (embed) data shape: {}, test labels shape: {}'.format(
            self.testEmbedX.shape, self.testY.shape))

        doc_lengths = list(map(len, self.trainEmbedX))
        median_doc_length = int(np.median(doc_lengths))
        max_doc_length = np.max(doc_lengths)
        print('doc lengths for embedding layer: median: {}, mean: {}, max: {}'.format(
            median_doc_length, np.mean(doc_lengths), max_doc_length))

        sequence_len = max_doc_length

        print('Using sequence length of {} to pad LSTM sequences.'.format(sequence_len))
        self.padded_train_embed_x = sequence.pad_sequences(
            self.trainEmbedX, maxlen=sequence_len, padding='pre', truncating='post')
        self.padded_test_embed_x = sequence.pad_sequences(
            self.testEmbedX, maxlen=sequence_len, padding='pre', truncating='post')

        print('Training data ready.')

        return self
