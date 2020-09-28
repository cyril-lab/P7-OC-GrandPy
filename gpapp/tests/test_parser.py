#!/usr/bin/python3
from gpapp.parser import Parser


def test_get_location():
    location = Parser("Salut GrandPy ! Est-ce que tu connais"
                      " l'adresse d'OpenClassrooms ?")
    assert location.get_location() == "OpenClassrooms"
