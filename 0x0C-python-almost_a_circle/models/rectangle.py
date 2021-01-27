#!/usr/bin/python3
"""[Class Rectangle that inherits from Base]
"""


from models.base import Base


class Rectangle(Base):
    """[This is class rectangle and it sets width, height, x and y

    Args:
        Base ([Class]): [rectangle inhertits from base]
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """[This gets the private instance attribute __width]

        Args:
            width ([type]): [description]
        """
        return self.__width

    @width.setter
    def width(self, value):
        """This sets the private instance attribute to value

        Args:
            value ([int]): [Integer that is passed]
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        """[This gets the private instance attribute __height]

        Args:
            height ([int]): [intger that is passed as height]
        """
        return (self.__height)

    @height.setter
    def height(self, value):
        """[This sets the private instance attribute __height]

        Args:
            value ([int]): [integer that is passed in ]
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        """[This gets the private instance attribute x]

        Args:
            x ([type]): [description]
        """
        return (self.__x)

    @x.setter
    def x(self, value):
        """[This sets the private instance attribute __x]

        Args:
        value ([int]): [integer that is passed in ]
        """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        """[This gets the private instance attribute y]

        Args:
            y ([int]): [intger that is passed]
        """
        return (self.__y)

    @y.setter
    def y(self, value):
        """[This sets the private instance attribute __y]

        Args:
        value ([int]): [integer that is passed in ]
        """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def area(self):
        """[Finds and returns the area and returns it as int]

        Returns:
            [int]: [This Method returns the width times the height]
        """
        return (self.__width * self.__height)

    def display(self):
        """[This prints the Rectangle instance]
        """
        for verticle in range(self.__y):
            print("")
        for colum in range(self.__height):
            print(" "*self.__x, end="")
            print("#"*self.__width)

    def __str__(self):
        """[This updates the class by returning
        [Rectangle] (<id>) <x>/<y> - <width>/<height> ]
        """
        format_str = "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.__x, self.__y, self.__width, self.__height)

        return format_str

    def update(self, *args, **kwargs):
        """[[This method assigns an argument for each attribute]
        attr_list = ["id", "width", "height", "x", "y"]]
        """
        if args and len(args) != 0:
            for itr in range(len(args)):
                if itr == 0:
                    self.id = args[itr]
                if itr == 1:
                    self.width = args[itr]
                if itr == 2:
                    self.height = args[itr]
                if itr == 3:
                    self.x = args[itr]
                if itr == 4:
                    self.y = args[itr]

        else:
            for itr in kwargs:
                if itr == "id":
                    self.id = kwargs[itr]
                if itr == "width":
                    self.width = kwargs[itr]
                if itr == "height":
                    self.height = kwargs[itr]
                if itr == "x":
                    self.x = kwargs[itr]
                if itr == "y":
                    self.y = kwargs[itr]

    def to_dictionary(self):
        """[This makes a dictonary that is then returned]
        """
        update_dict = {}

        update_dict["id"] = self.id
        update_dict["width"] = self.width
        update_dict["height"] = self.height
        update_dict["x"] = self.x
        update_dict["y"] = self.y

        return update_dict
