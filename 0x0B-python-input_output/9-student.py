#!/usr/bin/python3
"""defines Class Student"""


class Student():
    """class Student that that initilizes vars"""

    def __init__(self, first_name, last_name, age):
        """initializes student instances"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """returns dictionary descript for JSON serialization of info"""
        return self.__dict__
