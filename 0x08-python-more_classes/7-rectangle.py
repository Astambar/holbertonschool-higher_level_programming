#!/usr/bin/python3
"""
    Module contains of a single class
"""


class Rectangle:
    """[summary]

    Raises:
        TypeError: [description]
        ValueError: [description]
        TypeError: [description]
        ValueError: [description]
        TypeError: [description]
        ValueError: [description]
        TypeError: [description]
        ValueError: [description]

    Returns:
        [type]: [description]
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """[summary]

        Args:
            width (int, optional): [description]. Defaults to 0.
            height (int, optional): [description]. Defaults to 0.

        Raises:
            TypeError: [description]
            ValueError: [description]
            TypeError: [description]
            ValueError: [description]
        """
        if not isinstance(width, (int, float)):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        if not isinstance(height, (int, float)):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1

    def __str__(self):
        """[summary]

        Returns:
            [type]: [description]
        """
        string = []
        if self.__width == 0 or self.__height == 0:
            return ""

        if not isinstance(self.print_symbol, str):
            self.print_symbol = str(self.print_symbol)
        for i in range(self.__height):
            for _ in range(self.__width):
                string.append(self.print_symbol)
            if i < (self.__height - 1):
                string.append("\n")
        return "".join(string)

    def __repr__(self):
        """[summary]

        Returns:
            [type]: [description]
        """
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """[summary]
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @property
    def width(self):
        """[summary]

        Returns:
            [type]: [description]
        """
        return self.__width

    @property
    def height(self):
        """[summary]

        Returns:
            [type]: [description]
        """
        return self.__height

    @width.setter
    def width(self, value):
        """[summary]

        Args:
            value ([type]): [description]

        Raises:
            TypeError: [description]
            ValueError: [description]
        """
        if not isinstance(value, (int, float)):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """[summary]

        Args:
            value ([type]): [description]

        Raises:
            TypeError: [description]
            ValueError: [description]
        """
        if not isinstance(value, (int, float)):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """[summary]

        Returns:
            [type]: [description]
        """
        return (self.__width * self.__height)

    def perimeter(self):
        """[summary]

        Returns:
            [type]: [description]
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return ((self.__width + self.__height) * 2)
