#!/usr/bin/python3
"""[summary]
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
