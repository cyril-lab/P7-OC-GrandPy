#!/usr/bin/python3
import requests


class TestRoutes():
    BASE_URL = "http://127.0.0.1:5000/"

    def test_index(self):
        response = requests.get(self.BASE_URL)
        assert response.status_code == 200
