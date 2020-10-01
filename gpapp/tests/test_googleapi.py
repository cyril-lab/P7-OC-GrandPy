#!/usr/bin/python3
from gpapp.googleapi import GoogleApi


class TestGoogleApi:
    GOOGLE = GoogleApi("openclassrooms", "key")

    def test_parse_google(self, monkeypatch):
        class MockResponseGoogle():
            def __init__(self, url, params=None):
                self.status_code = 200

            def json(self):
                return {
                    'results': [{
                        'address_components': [{
                            'long_name': '10',
                            'short_name': '10',
                            'types': ['street_number']},
                            {'long_name': 'Quai de la Charente',
                                'short_name': 'Quai de la Charente',
                                'types': ['route']},
                            {'long_name': 'Paris',
                                'short_name': 'Paris',
                                'types': ['locality', 'political']},
                            {'long_name': 'Arrondissement de Paris',
                                'short_name': 'Arrondissement de Paris',
                                'types': ['administrative_area_level_2',
                                          'political']},
                            {'long_name': 'Île-de-France',
                                'short_name': 'IDF',
                                'types': ['administrative_area_level_1',
                                          'political']},
                            {'long_name': 'France',
                             'short_name': 'FR',
                             'types': ['country',
                                       'political']},
                            {'long_name': '75019', 'short_name': '75019',
                                'types': ['postal_code']}],
                        'formatted_address': '10 Quai de la Charente,'
                                             ' 75019 Paris, France',
                        'geometry': {'location': {'lat': 48.8975156,
                                                  'lng': 2.3833993}, }}]}

        monkeypatch.setattr('requests.get', MockResponseGoogle)
        result = self.GOOGLE._send_request()
        assert result['results'][0]['formatted_address'] == \
            "10 Quai de la Charente, 75019 Paris, France"
