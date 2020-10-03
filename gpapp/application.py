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
        latitude = 0
        longitude = 0
        address = "Bonjour, je vais bien merci !"
        history = self._get_papy_sentence()
        article_title = ""
        location = question.get_location()
        google = GoogleApi(location, self.google_key)
        google_response = google.parse()
        if question.get_verification():
            latitude = google_response['latitude']
            longitude = google_response['longitude']
            address = google_response['address']
        if google_response['status'] == "OK":
            wiki = WikiApi(google_response['latitude'],
                           google_response['longitude'])
            wiki_response = wiki.parse()
            if wiki_response['status'] == "OK":
                history = wiki_response['history']
                article_title = wiki_response['article_title']

        self.response_grandpy = {
            'latitude': latitude,
            'longitude': longitude,
            'address': address,
            'history': history,
            'article_title': article_title
            }
        return self.response_grandpy

    def _get_papy_sentence(self):
        """this method returns a random sentence"""
        sentences = [
            "un crayon basique peut écrire jusqu’à 45 000 mots. ",
            "la troisième langue officielle de la "
            "Nouvelle-Zélande est le langage des signes.",
            "si la Terre faisait la taille d’un grain de sable, "
            "le Soleil ferait la taille d’une orange.",
            "à la base, le papier bulle a été inventé "
            "pour servir de papier peint.",
        ]
        chosen_sentence = random.choice(sentences)
        response = "J'ai une histoire à te raconter : " + chosen_sentence
        return response
