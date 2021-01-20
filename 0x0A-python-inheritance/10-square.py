#!/usr/bin/python3
"""Class Square taht inhertis from Rectangle
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """class for Square that inherits from rectangle

    Args:
        Rectangle (class): [parent class]
    """
    def __init__(self, size):
        """initializes Square class"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """returns area of Square"""
        return (self.__size * self.__size)
