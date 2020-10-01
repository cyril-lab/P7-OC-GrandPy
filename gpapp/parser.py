#!/usr/bin/python3
from gpapp.stopwords import StopWords
import nltk


class Parser:
    """This class analyze a sentence.
    This class retrieves a sentence and returns a word
    that matches a searched location.
    """
    def __init__(self, sentence):
        self.sentence = sentence.lower()

    def get_location(self):
        """method to retrieve the location"""
        tokenizer = nltk.RegexpTokenizer(r'\w+')
        words = tokenizer.tokenize(self.sentence)
        stop_words = StopWords()
        stop_words = set(stop_words.get_stop_words())
        new_sentence = " "
        for word in words:
            if word not in stop_words:
                new_sentence += word
                if word != words[-1]:
                    new_sentence += " "
        return new_sentence
