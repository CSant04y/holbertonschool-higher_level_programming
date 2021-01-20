#!/usr/bin/python3
"""This makes a class called base geometry
"""


class BaseGeometry:
    """ class with public instance method to raise exception
    """
    def area(self):
        """ This raises and exception

        Raises:
        Exception: area() is not implemented
        """
        raise Exception("area() is not implemented")
