# #!/usr/bin/python3
from gpapp.wikiapi import WikiApi


class TestWikiApi:
    WIKI = WikiApi(44, 2)

    def test_parse_wiki(self, monkeypatch):
        class MockResponseWiki():
            def __init__(self, url, params=None):
                self.status_code = 200

            def json(self):
                return {
                    'batchcomplete': True,
                    'query': {
                        'pages':
                            [{'pageid': 3120649,
                              'ns': 0,
                              'title': 'Quai de la Gironde',
                              'index': -1,
                              'extract': 'Le quai de la Gironde'
                              ' est un quai situé le long du canal '
                              'Saint-Denis, à Paris, dans le 19e '
                              'arrondissement.…'}]
                                  }
                        }

        monkeypatch.setattr('requests.get', MockResponseWiki)
        result = self.WIKI._send_request()
        assert result['query']['pages'][0]['title'] == 'Quai de la Gironde'
