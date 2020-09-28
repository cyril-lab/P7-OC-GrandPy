#!/usr/bin/python3
from gpapp.wikiapi import WikiApi
import requests


class TestWikiApi:
    WIKI = WikiApi(44, 2)
    
    @staticmethod
    def json():
        return {'batchcomplete': True, 'query':
                {'pages': [{'pageid': 3120649,
                            'ns': 0,
                            'title': 'Quai de la Gironde',
                            'index': -1,
                            'extract': 'Le quai de la Gironde'
                            ' est un quai situé le long du canal '
                            'Saint-Denis, à Paris, dans le 19e '
                            'arrondissement.…'}]}}


    def test_send_request(self, monkeypatch):
        def mock_get(*args, **kwargs):
            return TestWikiApi()

        monkeypatch.setattr(requests, "get", mock_get)

        result = self.WIKI.send_request()
        assert result['query']['pages'][0]['title'] == 'Quai de la Gironde'

    def test_set_article_title(self):
        self.WIKI.article_title = "titre"
        assert self.WIKI.article_title == "titre"

    def test_get_article_title(self):
        assert self.WIKI.article_title == "titre"

    def test_set_article_abstract(self):
        self.WIKI.article_abstract = "abstract"
        assert self.WIKI.article_abstract == "abstract"

    def test_get_article_abstract(self):
        assert self.WIKI.article_abstract == "abstract"