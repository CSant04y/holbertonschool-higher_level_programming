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

    def integer_validator(self, name, value):
        """Public Instance Method that validates value

        Args:
            name (string): Will always be a string
            value (integer): Value is supposed to be a string
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
