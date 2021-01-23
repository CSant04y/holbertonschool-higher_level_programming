#!/usr/bin/python3
"""[Class Square that inherits from Rectangle]
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """[The Class Rectangle inherits from class rectangle]
    """
    def __init__(self, size, x=0, y=0, id=None):
        """[This initilizies the square instance]

        Args:
            size ([int]): [The size of the sides of square]
            x (int): Defaults to 0.
            y (int): Defaults to 0.
            id ([int]): Defaults to None.
        """
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        """Overloading with __str__ method
        [Square] (<id>) <x>/<y> - <size>"""
        str_format = "[Square] ({}) {}/{} - {}".format(
            str(self.id), str(self.x), str(self.y), str(self.width))
        return (str_format)
