#!/usr/bin/python3
"""creates class Square with private instance attribute size"""


class Square:
    """This Initilizes both variables"""
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.position = position

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

    @property
    def position(self):
        """This gets the __postion(private)"""
        return(self.__position)

    @position.setter
    def position(self, value):
        """sets the private instance attribute position"""
        num = 0
        while True:
            if type(value) is not tuple or len(value) is not 2:
                num += 1
                break
            if type(value[0]) is not int or type(value[1]) is not int:
                num += 1
                break
            if value[0] < 0 or value[1] < 0:
                num += 1
            break
        if num is 0:
            self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        """This calcs len * width = area of square"""
        return self.__size * self.__size

    def my_print(self):
        """Prints square using # signs"""
        if self.__size > 0:
            for column in range(self.__size):
                for x in range(self.__position[0]):
                    print(" ", end="")
                for row in range(self.__size):
                    print("#", end="")
                print()
        else:
            print()
