#!/usr/bin/python3
"""
module that contain the base Rectangle
Class:
    Rectangle: this is the Rectangle class
"""

from models.base import Base


class Rectangle(Base):
    """
    this is the Rectangle class
    Functions:
        __init__: init a rectangle
        __str__: print the Rectangle as:
            [Rectangle] (<id>) <x>/<y> - <width>/<height>
        check_value: function that check if value has good parameters
        area: function that returns the Rectangle area
        display: function that print the Rectangle with the character #
            by taking care of x and y
        update: assigns an argument to each attribute
        to_dictionary: function that returns the dictionary representation
            of a Rectangle
    Getter:
        width: access to width
        height: access to height
        x: access to x
        y: access to y
    Setter:
        width: change the width
        height: change the height
        x: change the x
        y: change the y
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        init a rectangle
        Arguments:
            width: width of the Rectangle
            height: height of the Rectangle
            x: x of the Rectangle
            y: y of the Rectangle
        Returns:
            None
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
