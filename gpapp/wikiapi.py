#!/usr/bin/python3

import requests


class WikiApi:
    """This class sends requests to the Wikipedia API
    This class retrieves title and abstract of an artitle
     which corresponds to a place.
    """
    def __init__(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude
        self.article_title = ""
        self.article_abstract = ""

    def send_request(self):
        """method to send request"""
        url = "https://fr.wikipedia.org/w/api.php"
        setting = {
            "action": "query",
            "format": "json",
            "prop": "extracts",
            "generator": "geosearch",
            "formatversion": "2",
            "exchars": "150",
            "exintro": "1",
            "explaintext": "1",
            "ggslimit": "1",
            "ggscoord": "{}|{}".format(self.latitude, self.longitude)
        }
        request = requests.get(url=url, params=setting)
        request_wikipedia = request.json()
        return request_wikipedia

    def parse(self):
        """method to get title and abstract"""
        request_dic = self.send_request()
        self.article_title = request_dic['query']['pages'][0]['title']
        self.article_abstract = request_dic['query']['pages'][0]['extract']

    def get_article_title(self):
        """method to get article title"""
        return self.article_title

    def get_article_abstract(self):
        """method to get article abstract"""
        return self.article_abstract
