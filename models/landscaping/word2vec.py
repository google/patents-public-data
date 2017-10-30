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

from collections import Counter, OrderedDict
import pandas as pd
import numpy as np
import random
import os
import pickle
import time

import tensorflow as tf

import matplotlib.pyplot as plt
from sklearn.manifold import TSNE
from scipy.spatial import distance


# this ensures TensorFlow doesn't use all GPU memory with a
# single graph (thus preventing other TF graphs from utilizing GPU)
GPU_MEM_CONFIG = tf.ConfigProto(gpu_options={'allow_growth': True})

class W2VModelDownload:
    def __init__(self, bq_project):
        # no-op
        self.bq_project = bq_project

    def download_w2v_model(self, landscape_bucket, model_name):
        from google.cloud import storage

        """
        Download a pre-trained Word2Vec model.
        :param models_url: The URL where models are stored
        :param model_name: The name of the model to download
        """

        checkpoint_list_file = '/'.join(['models', model_name, 'checkpoints', 'checkpoint'])
        if os.path.exists(checkpoint_list_file):
            print('Model {} already exists. Using local copy.'.format(model_name))
            return

        client = storage.Client(project=self.bq_project)
        bucket = client.bucket('patent_landscapes')
        blob = bucket.blob(checkpoint_list_file)
        checkpoints = blob.download_as_string(client=client).decode()
        checkpoint_file = 'n/a'

        for checkpoint in checkpoints.split('\n'):
            if checkpoint.startswith('model_checkpoint_path'):
                checkpoint_file = checkpoint.split(': ')[1].replace('"', '')
                break

        blobs_list = bucket.list_blobs(prefix='/'.join(['models', model_name, 'checkpoints', checkpoint_file]))
        checkpoints_files = []
        for blob_item in blobs_list:
            checkpoints_files.append(blob_item.name)

        if checkpoint_file == 'n/a':
            raise ValueError('Unable to find checkpoint for model {}!'.format(model_name))

        checkpoint_path = '/'.join(['checkpoints', checkpoint_file])

        model_base_local_path = '/'.join(['models', model_name])
        local_dirs = ['checkpoints', 'vocab']
        files = checkpoints_files + [
            '/'.join(['models', model_name, 'train_words.pkl']),
            '/'.join(['models', model_name, 'checkpoints/checkpoint']),
            '/'.join(['models', model_name, 'vocab/config.csv']),
            '/'.join(['models', model_name, 'vocab/vocab.csv']),
        ]

        for storage_dir in local_dirs:
            local_model_storage_dir = '/'.join([model_base_local_path, storage_dir])
            if not os.path.exists(local_model_storage_dir):
                os.makedirs(local_model_storage_dir)

        for file_path in files:
            #file_path = os.path.join('models', model_name, file)
            if os.path.exists(file_path):
                print('Not downloading {}; already exists'.format(file_path))
                continue

            blob_file = bucket.blob(file_path)
            print('Downloading {}'.format(file_path))
            blob_file.download_to_filename(file_path)

        print('Completed downloading {} files'.format(model_name))
    

class TrainedW2VRuntime:
    w2v_graph = None
    index_to_word = None
    word_to_index = None
    embedding_weights = None
    normed_embedding_weights = None

    def __init__(
        self,
        w2v_graph,
        index_to_word,
        word_to_index,
        embedding_weights,
        normed_embedding_weights):
        '''
        '''

        self.w2v_graph = w2v_graph
        self.index_to_word = index_to_word
        self.word_to_index = word_to_index
        self.embedding_weights = embedding_weights
        self.normed_embedding_weights = normed_embedding_weights

    def visualize_embeddings(self, num_words=500):
        '''
        Creates a matplotlib plot of the first 'num_words' words using TSNE to see how 'close'
        each of the words are in the embedding space.

        Note that TSNE uses SGD and therefore this method will not always produce the
        exact same visualization even on identical input.
        '''

        tsne = TSNE()
        embed_tsne = tsne.fit_transform(self.normed_embedding_weights[:num_words, :])

        fig, ax = plt.subplots(figsize=(14, 14))
        for idx in range(num_words):
            plt.scatter(*embed_tsne[idx, :], color='steelblue')
            plt.annotate(self.index_to_word[idx], (embed_tsne[idx, 0], embed_tsne[idx, 1]), alpha=0.7)        

    def find_similar(self, word, top_k):
        '''
        Finds the top_k most similar words to the provided word, as determined by calculating
        the cosine distance between the word and the rest of the embedded words, sorting the
        distance, and finally taking only the top_k results.
        
        Note: this should be used for debugging or illustrative purposes only; it's slow!
        '''
        distances = {}

        word1_index = self.word_to_index[word]
        word1_embed = self.embedding_weights[word1_index]
        for index in range(0, len(self.embedding_weights)):
            if index != word1_index:
                word2_embed = self.embedding_weights[index]
                word_dist = distance.cosine(word1_embed, word2_embed)
                distances[index] = word_dist

        top_k_similar = sorted(distances.items(), key=lambda x:x[1])[:top_k]

        similar_words = []
        for i in range(0, len(top_k_similar)):
            similar_word_index = top_k_similar[i][0]
            similar_word_dist = top_k_similar[i][1]
            similar_word = self.index_to_word[similar_word_index]
            similar_words.append(
                {'word': similar_word,
                 'index': similar_word_index,
                 'distance': similar_word_dist})

        return similar_words

    def load_embedding(self, word):
        '''
        '''

        if word in self.word_to_index:
            word_idx = self.word_to_index[word]
        else:
            print("Couldn't find {}. Using UNK instead. If this sounds wrong, consider normalizing text.".format(word))
            word_idx = self.word_to_index['UNK']

        return self.embedding_weights[word_idx]


class W2VGraph:
    train_graph = None
    inputs = None
    labels = None
    embedding = None
    normalized_embedding = None
    loss = None
    cost = None
    optimizer = None
    similarity = None
    valid_size = None
    valid_window = None
    valid_examples = None

    def __init__(
        self,
        train_graph, inputs, labels, embedding, normalized_embedding, loss, cost, optimizer,
        similarity,
        valid_size,
        valid_window,
        valid_examples):

        self.train_graph = train_graph
        self.inputs = inputs
        self.labels = labels
        self.embedding = embedding
        self.normalized_embedding = normalized_embedding
        self.loss = loss
        self.cost = cost
        self.optimizer = optimizer
        self.similarity = similarity
        self.valid_size = valid_size
        self.valid_window = valid_window
        self.valid_examples = valid_examples

class Word2Vec:
    models_path = 'models'
    checkpoint_file = None
    model_name = None
    checkpoints_path = None
    vocab_dir = None
    vocab_file = None
    config_file = None
    train_words_path = None

    vocabulary_size = 150
    subsample_threshold = 1e-5
    negative_samples = 750

    w2v_runtime = None

    def __init__(self, model_name, vocab_size=50000, subsample_threshold=1e-5):
        print('Will use models/{} directory to load/persist model information.'.format(model_name))

        self.model_name = model_name
        self.checkpoints_path = os.path.join(
            self.models_path, self.model_name, 'checkpoints')
        self.checkpoint_file = os.path.join(
            self.checkpoints_path, '{}.ckpt'.format(self.model_name))
        self.vocab_dir = os.path.join(
            self.models_path, self.model_name, 'vocab')
        self.vocab_file = os.path.join(self.vocab_dir, 'vocab.csv')
        self.config_file = os.path.join(self.vocab_dir, 'config.csv')
        self.train_words_path = os.path.join(self.models_path, self.model_name, 'train_words.pkl')

        if vocab_size > 0:
            self.vocabulary_size = vocab_size
        if subsample_threshold > 0:
            self.subsample_threshold = subsample_threshold

    def preprocess_sequential_words(
        self,
        sequential_words,
        min_wordcount=10):

        vocab_to_int, int_to_vocab, int_words, int_word_counts = \
            self.create_lookup_tables(words, vocabulary_size)

        total_wordcount = len(int_words)
        print('Most common words: ', [word for word in int_to_vocab.values()][0:5])

        train_words = self.subsample_words(
            self.subsample_threshold, int_words, int_word_counts, total_wordcount)
        print("Total words in corpus: {}, vocab size: {}, num words used for training: {}".format(
            total_wordcount, len(int_word_counts), len(train_words)))

        return vocab_to_int, int_to_vocab, int_words, int_word_counts, train_words

    def create_lookup_tables(self, words, vocab_size, min_wordcount=10):
        print('Generating wordcounts')
        word_counts = Counter(words)

        print('Filtering words with counts < {}'.format(min_wordcount))
        words = [word for word in words if word_counts[word] >= min_wordcount]

        word_counts = Counter(words)

        if len(word_counts) >= vocab_size:
            print('reducing word count from {} to top {} words'.format(len(word_counts), vocab_size))
            word_counts = OrderedDict(word_counts.most_common(vocab_size - 1))
            words = [word for word in words if word in word_counts]
        else:
            print('keeping word count at {} (max set as {})'.format(len(word_counts), vocab_size))

        word_counts['UNK'] = 1

        sorted_vocab = sorted(word_counts, key=word_counts.get, reverse=True)
        int_to_vocab = {ii: word for ii, word in enumerate(sorted_vocab)}
        vocab_to_int = {word: ii for ii, word in int_to_vocab.items()}

        int_words = [vocab_to_int[word] for word in words]

        int_word_counts = Counter(int_words)

        return vocab_to_int, int_to_vocab, int_words, int_word_counts

    # this taken from milikov et al paper
    def prob_keep(self, threshold, int_word, freqs):
        return 1 - np.sqrt(threshold / freqs[int_word])


    def subsample_words(self, threshold, int_words, int_word_counts, total_wordcount):
        # calculate relative frequencies of each word in the corpus
        freqs = {word: count/total_wordcount for word, count in int_word_counts.items()}

        # calculate the probability that we should keep a word, based on the threshold
        int_word_probs = [self.prob_keep(threshold, int_word, freqs) for int_word in set(int_words)]

        # generate the set of words to use for training data, taking into account the
        # probabilities generated for each word
        train_words = [int_word for int_word in int_words if (int_word_probs[int_word] < random.random())]

        return train_words

    def save_vocab_mapping(self, int_to_vocab):
        '''
        Saves the mapping from word index -> word string to disk. The reverse mapping can be
        derived from this data, so no need to persist both.
        '''
        if not os.path.isdir(self.vocab_dir):
            print('Creating directory to store vocab/config files: {}'.format(self.vocab_dir))
            os.makedirs(self.vocab_dir)

        vocab_df = pd.DataFrame.from_dict(int_to_vocab, orient='index')
        vocab_df.columns = ['word']
        vocab_df.to_csv(self.vocab_file)

    def save_model_config(self, config_dict):
        if not os.path.isdir(self.vocab_dir):
            print('Creating directory to store vocab/config files: {}'.format(self.vocab_dir))
            os.makedirs(self.vocab_dir)

        pd.DataFrame.from_dict(config_dict, orient='index').to_csv(self.config_file)

    def load_vocab_mappings(self):
        '''
        Loads a CSV with a mapping from 
        '''
        index_to_vocab_df = pd.read_csv(
            self.vocab_file, keep_default_na=False, na_values=[], encoding='latin-1')
        vocab_to_index_df = pd.read_csv(
            self.vocab_file, index_col='word', keep_default_na=False, na_values=[], encoding='latin-1')
        vocab_to_index_df.columns = ['index']

        return index_to_vocab_df.to_dict()['word'], vocab_to_index_df.to_dict()['index']

    def load_model_config(self):
        config_df = pd.read_csv(self.config_file)
        config_df.columns = ['name', 'value']
        config_df = config_df.set_index(config_df['name'])['value']

        return config_df.to_dict()

    def save_train_words(self, train_words_indexes):
        with open(self.train_words_path, 'wb') as fp:
            pickle.dump(train_words_indexes, fp)

    def load_train_words(self, file_path):
        with open(file_path, 'rb') as f:
            train_words_indexes = pickle.load(f)
        return train_words_indexes


    def get_target(self, words, idx, window_size=5):
        ''' Gets the window of words around a particular word (as referenced by its idx). '''

        r = random.randint(1, window_size+1)
        if (idx - r) < 0:
            return words[0:idx+r+1]
        return words[idx-r:idx+r+1]


    def get_batches(self, words, batch_size, window_size=5):
        ''' Create a generator of word batches as a tuple (inputs, targets) '''

        n_batches = len(words) // batch_size

        # only full batches
        words = words[:n_batches * batch_size]

        for idx in range(0, len(words), batch_size):
            x, y = [], []
            batch = words[idx:idx + batch_size]
            for ii in range(len(batch)):
                batch_x = batch[ii]
                batch_y = self.get_target(batch, ii, window_size)
                y.extend(batch_y)
                x.extend([batch_x] * len(batch_y))
            yield x, y

################ TensorFlow-related Code ############################

    def create_graph(self, vocab_size, embedding_size, negative_samples_for_loss):
        '''
        Creates the Word2Vec graph for use in training and restoring checkpoint files to
        load embeddings. The method returns the graph, the embedding variable and the normalized
        embedding variables that can be used to restore the embedding weights from the TF graph.
        
        You should call this function like this:
        graph, embedding, normalized_embedding = word2vec.create_graph(...params...)
        '''
        train_graph = tf.Graph()

        n_vocab = vocab_size
        n_embedding = embedding_size
        n_sampled = negative_samples_for_loss

        with train_graph.as_default():
            inputs = tf.placeholder(tf.int32, [None])
            labels = tf.placeholder(tf.int32, [None, None])

            # create embedding weight matrix
            embedding = tf.Variable(tf.random_uniform([n_vocab, n_embedding], minval=-1, maxval=1))
            # gets the hidden layer output (i.e. the embedding)
            embed = tf.nn.embedding_lookup(embedding, inputs)

            softmax_w = tf.Variable(tf.truncated_normal((n_vocab, n_embedding), stddev=0.1))
            softmax_b = tf.Variable(tf.zeros(n_vocab))

            # For each word, we need to sample for negative training data
            # (i.e., words not in window) for calculating loss and backprop
            # This calculates the loss using negative sampling
            loss = tf.nn.sampled_softmax_loss(softmax_w, softmax_b, labels, embed, n_sampled, n_vocab)

            cost = tf.reduce_mean(loss)
            optimizer = tf.train.AdamOptimizer().minimize(cost)

            # Validation dataset
            # TODO: parameterize this
            valid_size = 16 # Random set of words to evaluate similarity on.
            valid_window = 100
            # pick 8 samples from (0,100) and (1000,1100) each ranges. lower id implies more frequent 
            valid_examples = np.array(random.sample(range(valid_window), valid_size//2))
            valid_examples = np.append(valid_examples, 
                                       random.sample(range(1000,1000+valid_window), valid_size//2))

            valid_dataset = tf.constant(valid_examples, dtype=tf.int32)

            # Uses cosine distance to find similarity of matrix elements
            norm = tf.sqrt(tf.reduce_sum(tf.square(embedding), 1, keep_dims=True))
            normalized_embedding = embedding / norm
            valid_embedding = tf.nn.embedding_lookup(normalized_embedding, valid_dataset)
            similarity = tf.matmul(valid_embedding, tf.transpose(normalized_embedding))

        w2v_graph = W2VGraph(
            train_graph,
            inputs,
            labels,
            embedding,
            normalized_embedding,
            loss,
            cost,
            optimizer,
            similarity,
            valid_size,
            valid_window,
            valid_examples)
        return w2v_graph #train_graph, inputs, labels, embedding, normalized_embedding

    def restore_runtime(self):
        '''
        Loads the latest checkpoint file for this model into the provided graph,
        returning the embedding weights and normalized embedding weights.
        
        You should use the normalized embedding weights for your embeddings.
        '''

        index_to_word, word_to_index = self.load_vocab_mappings()
        model_config = self.load_model_config()
        embedding_size = int(model_config['embedding_size'])
        loss_sampling_size = int(model_config['loss_sampling_size'])

        w2v_graph = \
            self.create_graph(len(index_to_word), embedding_size, loss_sampling_size)

        with tf.Session(graph=w2v_graph.train_graph, config=GPU_MEM_CONFIG) as sess:
            saver = tf.train.Saver()
            saver.restore(sess, tf.train.latest_checkpoint(self.checkpoints_path))
            embedding_weights, normed_embedding_weights = \
                sess.run([w2v_graph.embedding, w2v_graph.normalized_embedding])

        return TrainedW2VRuntime(w2v_graph, index_to_word, word_to_index, embedding_weights, normed_embedding_weights)
        #return w2v_graph.train_graph, index_to_word, word_to_index, embedding_weights, normed_embedding_weights


    def train(self, w2v_graph, int_to_vocab, train_words, epochs, batch_size, window_size):
        if not os.path.isdir(self.checkpoints_path):
            print('Creating checkpoints directory to store model ckpt files.')
            os.makedirs(self.checkpoints_path)

        with w2v_graph.train_graph.as_default():
            saver = tf.train.Saver()

        iteration = 1
        with tf.Session(graph=w2v_graph.train_graph, config=GPU_MEM_CONFIG) as sess:
            loss = 0
            sess.run(tf.global_variables_initializer())

            for e in range(1, epochs+1):
                start_epoch = time.time()
                batches = self.get_batches(train_words, batch_size, window_size)
                start = time.time()
                for x, y in batches:

                    feed = {w2v_graph.inputs: x,
                            w2v_graph.labels: np.array(y)[:, None]}
                    train_loss, _ = sess.run([w2v_graph.cost, w2v_graph.optimizer], feed_dict=feed)

                    loss += train_loss

                    if iteration % 500 == 0: 
                        end = time.time()
                        print("Epoch {}/{}".format(e, epochs),
                              "Iteration: {}".format(iteration),
                              "Avg. Training loss: {:.4f}".format(loss/500),
                              "{:.4f} sec/batch".format((end-start)/500))
                        loss = 0
                        start = time.time()

                    if iteration % 2500 == 0:
                        ## From Thushan Ganegedara's implementation
                        # note that this is expensive (~20% slowdown if computed every 500 steps)
                        sim = w2v_graph.similarity.eval()
                        for i in range(w2v_graph.valid_size):
                            valid_word = int_to_vocab[w2v_graph.valid_examples[i]]
                            top_k = 8 # number of nearest neighbors
                            nearest = (-sim[i, :]).argsort()[1:top_k+1]
                            log = 'Nearest to %s:' % valid_word
                            for k in range(top_k):
                                close_word = int_to_vocab[nearest[k]]
                                log = '%s %s,' % (log, close_word)
                            print(log)
                    if iteration % 25000 == 0:
                        save_path = saver.save(sess, self.checkpoint_file, global_step=iteration)

                    iteration += 1
                epoch_time = time.time() - start_epoch
                print('{:.4f} seconds ({:.4f} minutes) for full epoch'.format(epoch_time, epoch_time/60))
            save_path = saver.save(sess, self.checkpoint_file, global_step=iteration)
            embed_mat = sess.run(w2v_graph.normalized_embedding)


    def prep_train_and_save_model(
        self,
        sequential_words_corpus,
        vocabulary_size,
        embedding_size,
        num_epochs,
        batch_size,
        window_size):
        '''
        TODO: document me
        '''

        words = sequential_words_corpus
        n_embedding = embedding_size
        n_sampled = self.negative_samples

        vocab_to_int, int_to_vocab, int_words, int_word_counts = \
            self.create_lookup_tables(words, vocabulary_size)
        total_wordcount = len(int_words)
        print('Most common words: ', [word for word in int_to_vocab.values()][0:10])
        print('Least common words: ', [word for word in int_to_vocab.values()][-10:])

        train_words = self.subsample_words(
            self.subsample_threshold, int_words, int_word_counts, total_wordcount)
        print("Total words in corpus: {}, vocab size: {}, num words used for training: {}".format(
            total_wordcount, len(int_word_counts), len(train_words)))
        
        # after preprocessing, save things off to disk so we can restore settings later
        print('Saving model config, vocab word-to-index mapping, and word corpus to models/{}.'.format(self.model_name))
        self.save_vocab_mapping(int_to_vocab)
        self.save_model_config({'embedding_size': n_embedding, 'loss_sampling_size': n_sampled})
        self.save_train_words(train_words)

        print('Creating TF graph.')
        w2v_graph = self.create_graph(vocabulary_size, embedding_size, n_sampled)

        print('Training model for {} epochs.'.format(num_epochs))
        self.train(w2v_graph, int_to_vocab, train_words, num_epochs, batch_size, window_size)
        
        return w2v_graph.train_graph, w2v_graph.embedding, w2v_graph.normalized_embedding
