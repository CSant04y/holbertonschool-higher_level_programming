#!/usr/bin/python3
""" This generates a locked class
"""


class LockedClass:
    """ This prevents user from dynamically creating new instance attributes
    """
    __slots__ = ['first_name']
