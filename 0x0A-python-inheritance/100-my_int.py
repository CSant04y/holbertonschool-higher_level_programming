#!/usr/bin/python3
""" Defines Reble int class
"""


class MyInt(int):
    """class myInt inhertits from int

    Args:
        int ([type]): [description]
    """
    def __eq__(self, other):
        """returns the oposit of equal"""
        return super().__ne__(other)

    def __ne__(self, other):
        """returns the oppistit on not equal"""
        return super().__eq__(other)
