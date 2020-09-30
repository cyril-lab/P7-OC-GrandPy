#!/usr/bin/python3
from gpapp.parser import Parser
from gpapp.googleapi import GoogleApi
from gpapp.wikiapi import WikiApi


class Application:
    """this class returns the elements of the response.
    This class return the latitude, longitude, address,
    the wiki answer and the article title of wikipedia.
    """
    def __init__(self, question, google_key):
        self.question = question
        self.response = {}
        self.google_key = google_key

    def main(self):
        """the main method of the class"""
        question = Parser(self.question)
        location = question.get_location()
        cordinate = GoogleApi(location, self.google_key)
        cordinate.parse()
        latitude = cordinate.coordinate_latitude
        self.response['latitude'] = cordinate.coordinate_latitude
        longitude = cordinate.coordinate_longitude
        self.response['longitude'] = longitude
        address = cordinate.address
        self.response['address'] = address
        article = WikiApi(latitude, longitude)
        article.parse()
        wiki_answer = article.article_abstract
        self.response['wiki_answer'] = wiki_answer
        article_title = article.article_title
        self.response['article_title'] = article_title
        return self.response
