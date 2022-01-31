#!/usr/bin/python3
"""[summary]

Returns:
    [type]: [description]
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """[summary]

    Args:
        Rectangle ([type]): [description]
    """

    def __init__(self, size):
        """[summary]

        Args:
            size ([type]): [description]
        """
        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        return "[Square] " + str(self.__size) + "/" + str(self.__size)
