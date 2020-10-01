#!/usr/bin/python3
from gpapp.parser import Parser
from gpapp.googleapi import GoogleApi
from gpapp.wikiapi import WikiApi
import random


class Application:
    """this class returns the elements of the response.
    This class return the latitude, longitude, address,
    the wiki answer and the article title of wikipedia.
    """
    def __init__(self, question, google_key):
        self.question = question
        self.google_key = google_key
        self.response_GrandPy = ""

    def main(self):
        """the main method of the class"""
        question = Parser(self.question)
        location = question.get_location()
        google = GoogleApi(location, self.google_key)
        google_response = google.parse()
        wiki = WikiApi(google_response['latitude'],
                       google_response['longitude'])
        wiki_response = wiki.parse()
        self.response_GrandPy = {
            'latitude': google_response['latitude'],
            'longitude': google_response['longitude'],
            'address': google_response['address'],
            'history': self._get_papy_sentence() + wiki_response['history'],
            'article_title': wiki_response['article_title']
            }
        return self.response_GrandPy

    def _get_papy_sentence(self):
        """this method returns a random sentence"""
        sentences = [
            "Ah le bon vieux temps, ça me rappelle une histoire ! ",
            "J'ai une histoire à te dire ! ",
            "J'ai retrouvé mes lunettes, une histoire pour la route ! ",
            "Les jeunes ne savent plus s'amuser, laisse-moi te raconter ! ",
        ]
        chosen_sentence = random.choice(sentences)
        return chosen_sentence
