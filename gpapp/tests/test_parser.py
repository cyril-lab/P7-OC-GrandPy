#!/usr/bin/python3
from gpapp.parser import Parser


def test_get_location_0():
    location = Parser("Salut GrandPy ! Est-ce que tu connais"
                      " l'adresse d'OpenClassrooms ?")
    assert location.get_location() == " openclassrooms"


def test_get_location_1():
    location = Parser("! ; : , ? / ")
    assert location.get_location() == " "


def test_get_location_2():
    location = Parser("bonjour ! Où se trouve"
                      " l'adresse d'OpenClassrooms ?")
    assert location.get_location() == " openclassrooms"


def test_get_location_3():
    location = Parser("Donnes-moi"
                      " l'adresse d'OpenClassrooms ?")
    assert location.get_location() == " openclassrooms"


def test_get_location_4():
    location = Parser("Indique moi"
                      " l'adresse d'OpenClassrooms ?")
    assert location.get_location() == " openclassrooms"


def test_get_location_5():
    location = Parser("Ou est situé"
                      " OpenClassrooms ?")
    assert location.get_location() == " openclassrooms"


def test_get_location_6():
    location = Parser("Dis-moi où se trouve"
                      " OpenClassrooms ?")
    assert location.get_location() == " openclassrooms"
