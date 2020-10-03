#!/usr/bin/python3
from gpapp.stopwords import StopWords
import nltk
from fuzzywuzzy import process


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
        location = " "
        for word in words:
            if word not in stop_words:
                location += word
                if word != words[-1]:
                    location += " "
        return location

    def get_verification(self):
        """method to check if the question corresponds to sentences"""
        sentences_test = [
            "bonjour papy, coment vas tu ?",
            "salut grandpybot, comment tu vas ?",
            "bonjour grandpy, tu vas bien ? ",
            "salut grandpy ! tu vas bien ?",
            "salut, tu vas bien",
            "bonjour, tu vas bien ?",
            "bonjour, comment vas-tu ?",
            "salut, comment vas-tu ?",
            "bonjour, comment ça va ?"
                    ]
        question_chosen = \
            process.extract(self.sentence, sentences_test, limit=1)
        if question_chosen[0][1] > 90:
            return False
        else:
            return True
