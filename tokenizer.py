from keras.preprocessing import text

import re
import string

class TextTokenizer:
    punct_regex = re.compile('([%s])' % (string.punctuation + '‘’'))
    spaces_regex = re.compile(r'\s{2,}')
    number_regex = re.compile(r'\d+')
    keras_tokenizer = None

    def __init__(
        self):
        '''
        '''



    def tokenize_to_onehot_matrix(self, text_series, vocab_size, keras_tokenizer=None):
        '''
        '''
        if keras_tokenizer is None:
            print('No Keras tokenizer supplied so using vocab size ({}) and series to build new one'.format(vocab_size))

            keras_tokenizer = text.Tokenizer(
                num_words=vocab_size,
                split=",",
                # filter should be same as default, minus the '-'
                filters='!"#$%&()*+,./:;<=>?@[\\]^_`{|}~\t\n',
                lower=False)
            keras_tokenizer.fit_on_texts(text_series)
            keras_tokenizer.index_word = {idx: word for word, idx in keras_tokenizer.word_index.items()}

        text_one_hot = keras_tokenizer.texts_to_matrix(text_series)

        return keras_tokenizer, text_one_hot


    def tokenize(
        self,
        text,
        normalize_numbers=True,
        lowercase=True,
        remove_punct=True,
        lemmatize=False):
        '''
        '''

        #plain_text = html2text.html2text(text)
        plain_text = text
        if not isinstance(plain_text, str):
            raise Exception(plain_text, type(plain_text))

        preprocessed = plain_text.replace('\'', '')
        if lowercase:
            preprocessed = preprocessed.lower()

        # Replace punctuation with spaces which handles cases like "searching/filter",
        # "nothing:)" and "writing.like.this" very well.
        # The double spaces that often result are then collased by the next method
        if remove_punct:
            preprocessed = self.punct_regex.sub(' ', preprocessed)
        else:
            preprocessed = self.punct_regex.sub(r' \1 ', preprocessed)

        preprocessed = self.spaces_regex.sub(' ', preprocessed)
        if normalize_numbers:
            preprocessed = self.number_regex.sub('_NUMBER_', preprocessed)

        if lemmatize:
            preprocessed = shared_funcs.NltkLemmatize(
                preprocessed, stem_post_lemmatize=False
            )

        return preprocessed.split()


    def tokenize_series(
        self,
        text_series,
        normalize_numbers=True,
        lowercase=True,
        remove_punct=True,
        lemmatize=False):
        '''
        '''

        return text_series.apply(self.tokenize)

