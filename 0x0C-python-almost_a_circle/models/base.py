#!/usr/bin/python3
"""[This is the Base class]
"""

class Base:
    """[This is base class
    """
    __nb_objects = 0
    def __init__(self, id=None):
        """[summary]

        Args:
            id ([type], optional): [description]. Defaults to None.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
