#!/usr/bin/python3
"""[This is the Base class]
"""


import json


class Base:
    """[This is base class]
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """[summary]

        Args:
            id ([int]): Defaults to None.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """[This is a static method that is to turn a dictornary
        to json string]

        Args:
            list_dictionaries ([List]): [This is a list of dictonaries]
        """
        if list_dictionaries is None or 0:
            return "[]"
        return json.dumps(list_dictionaries)
