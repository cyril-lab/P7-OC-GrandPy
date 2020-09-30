#!/usr/bin/python3
from nltk.corpus import stopwords
import nltk


class Parser:
    """This class analyze a sentence.
    This class retrieves a sentence and returns a word
    that matches a searched location.
    """
    def __init__(self, sentence):
        self.sentence = sentence
        nltk.download('stopwords')
        nltk.download('punkt')

    def get_location(self):
        """method to retrieve the location"""
        tokenizer = nltk.RegexpTokenizer(r'\w+')
        words = tokenizer.tokenize(self.sentence)
        stop_words = set(stopwords.words('french'))
        new_sentence = []
        for word in words:
            if word not in stop_words:
                new_sentence.append(word)
        return new_sentence[-1]
