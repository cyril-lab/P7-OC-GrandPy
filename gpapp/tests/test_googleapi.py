#!/usr/bin/python3
from gpapp.googleapi import GoogleApi
import requests


class TestGoogleApi:
    GOOGLE = GoogleApi("openclassrooms", "key")

    @staticmethod
    def json():
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
                               'political']}, {'long_name': 'France',
                                               'short_name': 'FR',
                                               'types': ['country',
                                                         'political']},
                    {'long_name': '75019', 'short_name': '75019',
                     'types': ['postal_code']}],
                'formatted_address': '10 Quai de la Charente,'
                                     ' 75019 Paris, France',
                'geometry': {'location': {'lat': 48.8975156,
                                          'lng': 2.3833993}, }}]}


    def test_send_request(self, monkeypatch):
        def mock_get(*args, **kwargs):
            return TestGoogleApi()

        monkeypatch.setattr(requests, "get", mock_get)

        result = self.GOOGLE.send_request()
        assert result['results'][0]['formatted_address'] == \
            "10 Quai de la Charente, 75019 Paris, France"

    def test_set_coordinate_latitude(self):
        self.GOOGLE.coordinate_latitude = 44
        assert self.GOOGLE.coordinate_latitude == 44

    def test_get_coordinate_latitude(self):
        assert self.GOOGLE.coordinate_latitude == 44

    def test_set_coordinate_longitude(self):
        self.GOOGLE.coordinate_longitude = 2
        assert self.GOOGLE.coordinate_longitude == 2

    def test_get_coordinate_longitude(self):
        assert self.GOOGLE.coordinate_longitude == 2

    def test_set_address(self):
        self.GOOGLE.adress = "Address"
        assert self.GOOGLE.adress == "Address"

    def test_get_address(self):
        assert self.GOOGLE.adress == "Address"

    def test_set_place(self):
        self.GOOGLE.place = "OpenClassrooms"
        assert self.GOOGLE.place  == "OpenClassrooms"

    def test_get_place(self):
        assert self.GOOGLE.place  == "OpenClassrooms"