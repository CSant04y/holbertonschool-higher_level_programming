#!/usr/bin/python3
"""defines function that adds a new attribute to an object if it’s possible""


def add_attribute(obj, name, value):
    """checks to see if attribute can be added"""
    if '__dict__' not in dir(obj):
        raise TypeError("can't add new attribute")
    else:
        setattr(obj, name, value)
