#!/usr/bin/python3
"""defines function to check if you can add attribute"""


def add_attribute(obj, name, value):
    """checks to see if you can add atrribute"""
    if '__dict__' not in dir(obj):
        raise TypeError("can't add new attribute")
    else:
        setattr(obj, name, value)
