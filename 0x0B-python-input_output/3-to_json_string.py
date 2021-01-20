#!/usr/bin/python3
""" function that returns the JSON representation of an object (string):
"""


import json


def to_json_string(my_obj):
    """This function generates an object string in json

    Args:
        my_obj ([type]): The object that is going to be serilized into JSON str
    """
    return json.dumps(my_obj)
