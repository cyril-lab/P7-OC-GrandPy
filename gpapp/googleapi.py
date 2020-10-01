#!/usr/bin/python3

import requests


class GoogleApi:
    """This class sends requests to the Google API
    This class retrieves the address which corresponds to a place.
    """
    def __init__(self, place, google_key_api):
        self._place = place
        self.google_key_api = google_key_api

    def _send_request(self):
        """method to send request"""
        request = requests.get(
                f"https://maps.googleapis.com/maps/api/geocode/json?address="
                f"{self._place}&key={self.google_key_api}")
        google_response = request.json()
        if request.status_code == 200:
            return google_response

    def parse(self):
        """method to get coordinate and address"""
        google_response_dic = self._send_request()
        address = ""
        latitude = ""
        longitude = ""
        if google_response_dic['status'] == 'OK' \
                and google_response_dic is not None:
            address = google_response_dic[
                'results'][0]['formatted_address']
            latitude = google_response_dic[
                'results'][0]['geometry']['location']['lat']
            longitude = google_response_dic[
                'results'][0]['geometry']['location']['lng']

            return {
                'address': address,
                'latitude': latitude,
                'longitude': longitude
            }
        else:
            return {
                'address': "Je n'ai pas compris, peux-tu répéter ?",
                'latitude': 44.4377,
                'longitude': 2.51295
            }
