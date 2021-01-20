#!/usr/bin/python3
"""Class my list has a method that prints a sorted list
"""


class MyList(list):
    """Public instance method That prints out list in sorted order

    Args:
        list ([list]): [list of arbitrary numbers that is passed]
    """
    def print_sorted(self):
        print(sorted(self))
