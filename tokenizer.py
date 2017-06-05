import re
import string

class TextTokenizer:
    punct_regex = re.compile('([%s])' % (string.punctuation + '‘’'))
    spaces_regex = re.compile(r'\s{2,}')
    number_regex = re.compile(r'\d+')

    def tokenize(
        self,
        text,
        normalize_numbers=True,
        lowercase=True,
        remove_punct=True,
        lemmatize=False):

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

        return text_series.apply(self.tokenize)

