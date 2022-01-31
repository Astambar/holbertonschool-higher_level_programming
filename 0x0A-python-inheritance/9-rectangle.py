#!/usr/bin/python3
"""[summary]

Returns:
    [type]: [description]
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """[summary]

    Args:
        BaseGeometry ([type]): [description]
    """

    def __init__(self, width, height):
        """[summary]

        Args:
            width ([type]): [description]
            height ([type]): [description]
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """[summary]

        Returns:
            [type]: [description]
        """
        return (self.__width * self.__height)

    def __str__(self):
        """[summary]

        Returns:
            [type]: [description]
        """
        return "[Rectangle] " + str(self.__width) + "/" + str(self.__height)
