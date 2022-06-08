#!/usr/bin/python3
"""
module that contain the base Rectangle
Class:
    Rectangle: this is the Rectangle class
"""

from base import Base


class Rectangle(Base):
    """[summary]

    Args:
        Base ([type]): [description]
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """[summary]

        Args:
            width ([type]): [description]
            height ([type]): [description]
            x (int, optional): [description]. Defaults to 0.
            y (int, optional): [description]. Defaults to 0.
            id ([type], optional): [description]. Defaults to None.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def __str__(self):
        """
        print the Rectangle as: [Rectangle] (<id>) <x>/<y> - <width>/<height>
        Returns:
            [Rectangle] (<id>) <x>/<y> - <width>/<height>
        """
        return "[{:s}] ({:d}) {:d}/{:d} - {:d}/{:d}".format(
            __class__.__name__,
            self.id,
            self.x,
            self.y,
            self.width,
            self.height
            )

    def check_value(self, name, value):
        """[summary]

        Args:
            name ([type]): [description]
            value ([type]): [description]

        Raises:
            TypeError: [description]
            ValueError: [description]
            ValueError: [description]
        """
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if name in ["width", "height"] and value <= 0:
            raise ValueError("{:s} must be > 0".format(name))
        if name in ["x", "y"] and value < 0:
            raise ValueError("{:s} must be >= 0".format(name))

    def area(self):
        """[summary]

        Returns:
            [type]: [description]
        """
        return self.height * self.width

    def display(self):
        """[summary]
        """
        for _ in range(self.y):
            print()

        for j in range(self.height):
            for _ in range(self.x):
                print(" ", end='')
            for _ in range(self.width):
                print("#", end='')
            if j < self.height - 1:
                print()
        print()

    def update(self, *args, **kwargs):
        """[summary]
        """
        rectangle_list = ["id", "width", "height", "x", "y", "\0"]

        for i in range(len(args)):
            setattr(self, rectangle_list[i], args[i])

        if not args:
            for i, Value in kwargs.items():
                if i in rectangle_list:
                    setattr(self, i, kwargs[i])

    def to_dictionary(self):
        """[summary]

        Returns:
            [type]: [description]
        """
        return {'id': self.id, "width": self.width, 'height': self.height,
                'x': self.x, 'y': self.y}

    @property
    def width(self):
        """[summary]

        Returns:
            [type]: [description]
        """
        return self.__width

    @width.setter
    def width(self, value):
        """[summary]

        Args:
            value ([type]): [description]
        """
        self.check_value("width", value)
        self.__width = value

    @property
    def height(self):
        """[summary]

        Returns:
            [type]: [description]
        """
        return self.__height

    @height.setter
    def height(self, value):
        """[summary]

        Args:
            value ([type]): [description]
        """
        self.check_value("height", value)
        self.__height = value

    @property
    def x(self):
        """[summary]

        Returns:
            [type]: [description]
        """
        return self.__x

    @x.setter
    def x(self, value):
        """[summary]

        Args:
            value ([type]): [description]
        """
        self.check_value("x", value)
        self.__x = value

    @property
    def y(self):
        """[summary]

        Returns:
            [type]: [description]
        """
        return self.__y

    @y.setter
    def y(self, value):
        """[summary]

        Args:
            value ([type]): [description]
        """
        self.check_value("y", value)
        self.__y = value
