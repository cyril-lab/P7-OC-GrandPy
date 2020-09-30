#!/usr/bin/python3

import requests


class GoogleApi:
    """This class sends requests to the Google API
    This class retrieves the address which corresponds to a place.
    """
    def __init__(self, place, google_key_api):
        self._place = place
        self.google_key_api = google_key_api
        self.coordinate_latitude = ""
        self.coordinate_longitude = ""
        self.address = ""

    def send_request(self):
        """method to send request"""
        google_response = requests.get(
                f"https://maps.googleapis.com/maps/api/geocode/json?address="
                f"{self._place}&key={self.google_key_api}")

        google_response_dic = google_response.json()
        return google_response_dic

    def parse(self):
        """method to get coordinate and address"""
        google_response_dic = self.send_request()
        self.address = google_response_dic[
            'results'][0]['formatted_address']
        self.coordinate_latitude = google_response_dic[
            'results'][0]['geometry']['location']['lat']
        self.coordinate_longitude = google_response_dic[
            'results'][0]['geometry']['location']['lng']

    def get_coordinate_latitude(self):
        """method to get coordinate latitude"""
        return self.coordinate_latitude

    def get_coordinate_longitude(self):
        """method to get coordinate longitude"""
        return self.coordinate_longitude

    def get_address(self):
        """method to get address"""
        return self.address

    def get_place(self):
        """method to get place"""
        return self.place

    def set_place(self, place):
        """method to set place"""
        self.place = place
