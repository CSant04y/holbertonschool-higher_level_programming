#!/usr/bin/python3
"""This function prints out a square using ##"""


def print_square(size):
    """function check for integer values and errors out when not passed int"""
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if size is float and size < 0:
        raise TypeError("size must be an integer")
    for i in range(size):
        print("#" * size, end="")
        print()
