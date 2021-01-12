#!/usr/bin/python3
"""This is a function that defines a rectangle"""


class Rectangle:
    """This is an class called Rectangle"""

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    def area(self):
        """returns the Area of h * w"""
        return (self.width * self.height)

    def perimeter(self):
        """calculates perimeter of the rectangle"""
        if self.width == 0 or self.height == 0:
            return 0
        return ((2 * self.width) + (2 * self.height))

    def __str__(self):
        """ Returns string representaion of rectange"""
        empty_str = ""
        if self.width == 0 or self.height == 0:
            return (empty_str)
        for w in range(self.height):
            for h in range(self.width):
                empty_str += str(self.print_symbol)
            empty_str += "\n"
        empty_str = empty_str[:-1]
        return empty_str

    def __repr__(self):
        """ returns representaion of a string"""
        return "Rectangle(%s, %s)" % (self.width, self.height)

    def __del__(self):
        """This delete an instance"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
