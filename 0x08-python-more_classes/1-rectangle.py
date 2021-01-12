#!/usr/bin/python3
"""This is a function that defines a rectangle"""


class Rectangle:
    """This is an class called Rectangle"""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        """

        Args:
            value ([int]): [width of a rectangle]

        Raises:
            TypeError: width must be an integer
            ValueError: width must be >= 0
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        """

        Args:
            value ([int]): [height of a rectangle]

        Raises:
            TypeError: height must be an integer
            ValueError: width must be >= 0
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
