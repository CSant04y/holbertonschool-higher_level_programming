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

    @classmethod
    def save_to_file(cls, list_objs):
        """[This saves a json string into a file]

        Args:
            list_objs ([list]): [This is a list of objects]
        """
        if list_objs is None:
            list_objs = []

        filename = cls.__name__ + ".json"
        list_dict = []

        for item in list_objs:
                list_dict.append(item.to_dictionary())


        with open(filename, "w") as file:
            file.write(cls.to_json_string(list_dict))


    def from_json_string(json_string):
        """[This makes a json string into a python dictonary]

        Args:
            json_string ([json string]): [This is the sting
            that is to get truned into python dictonary]
        """
        if json_string is None:
            return []
        else:
            return json.loads(json_string)
