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

    def _send_request(self):
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
        if request.status_code == 200 and 'query' in request_wikipedia:
            return request_wikipedia

    def parse(self):
        """method to get title and abstract"""
        info_wikipedia = self._send_request()
        if info_wikipedia is not None:
            article_title = \
                info_wikipedia['query']['pages'][0]['title']
            article_abstract = \
                info_wikipedia['query']['pages'][0]['extract']
            return {
                'article_title': article_title,
                'history': article_abstract
                }
        else:
            return {
                'article_title': "",
                'history': "Je n'arrive pas à "
                "trouver des informations sur Wikipedia"
                }
