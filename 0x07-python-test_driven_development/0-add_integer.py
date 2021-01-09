#!/usr/bin/python3
"""This Function gives the sum of integers or floats"""


def add_integer(a, b=98):
    """ adds two integers or floats which are cast as ints"""
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
