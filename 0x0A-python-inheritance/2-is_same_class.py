#!/usr/bin/python3
""" function that returns True if the object is exactly an instance of the
    specified class ; otherwise False.
"""


def is_same_class(obj, a_class):
    """This check to see if object is inctance of. Defaults to True

    Args:
        obj (object): refering to the main object in pythons
        a_class ([Type]): Class type we are chcking for instance
    """
    if type(obj) is not a_class:
        return False

    return True
