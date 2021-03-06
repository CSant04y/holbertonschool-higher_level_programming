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

    @property
    def size(self):
        """[This is width being set to size]
        """
        return self.width

    @size.setter
    def size(self, value):
        """[This sets the size using the setter method]

        Args:
            value ([type]): [description]
        """
        self.width = value
        self.height = value

    def __str__(self):
        """Overloading with __str__ method
        [Square] (<id>) <x>/<y> - <size>"""
        str_format = "[Square] ({}) {}/{} - {}".format(
            str(self.id), str(self.x), str(self.y), str(self.width))
        return (str_format)

    def update(self, *args, **kwargs):
        """[[This method assigns an argument for each attribute]
        attr_list = ["id", "size", "x", "y"]]
        """
        if args and len(args) != 0:
            for itr in range(len(args)):
                if itr == 0:
                    self.id = args[itr]
                if itr == 1:
                    self.size = args[itr]
                if itr == 2:
                    self.x = args[itr]
                if itr == 3:
                    self.y = args[itr]
        else:
            for itr2 in kwargs:
                if itr2 == "id":
                    self.id = (kwargs[itr2])
                if itr2 == "size":
                    self.size = (kwargs[itr2])
                if itr2 == "x":
                    self.x = (kwargs[itr2])
                if itr2 == "y":
                    self.y = (kwargs[itr2])

    def to_dictionary(self):
            """[This makes a dictonary that is then returned for square]
            """
            sqr_dict = {}

            sqr_dict["id"] = self.id
            sqr_dict["size"] = self.size
#            sqr_dict["height"] = self.height
            sqr_dict["x"] = self.x
            sqr_dict["y"] = self.y

            return sqr_dict
