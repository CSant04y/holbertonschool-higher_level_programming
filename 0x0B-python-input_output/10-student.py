#!/usr/bin/python3
"""defines Class Student"""


class Student():
    """class Student that that initilizes vars"""

    def __init__(self, first_name, last_name, age):
        """initializes student instances"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """returns dictionary descript for JSON serialization of info"""
        if type(attrs) is list:
            dictonaryVal = {}

            for k in self.__dict__:
                for v in attrs:
                    if k == v:
                        dictonaryVal[k] = self.__dict__[k]
            return dictonaryVal
        else:
            return self.__dict__
