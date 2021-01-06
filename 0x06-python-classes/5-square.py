#!/usr/bin/python3
"""creates class Square with private instance attribute size"""


class Square:
    """defines class and instantiates private instance attribute size"""
    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        return(self.__size)

    @size.setter
    def size(self, val):

        if type(val) is not int:
            raise TypeError("size must be an integer")

        elif val < 0:
            raise ValueError("size must be >= 0")

        self.__size = val

    def area(self):
        """This calcs len * width = area of square"""
        return self.__size * self.__size

    def my_print(self):
        """Prints square using # signs"""
        if self.__size > 0:
            for column in range(self.__size):
                for row in range(self.__size):
                    print("#", end="")
                print()
        else:
            print()
