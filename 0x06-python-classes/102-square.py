#!/usr/bin/python3
"""[summary]

    Raises:
        TypeError: [description]
        ValueError: [description]

    Returns:
        [type]: [description]
    """


class Square:
    """AI is creating summary for

    Raises:
        TypeError: [description]
        ValueError: [description]

    Returns:
        [type]: [description]
    """

    def __init__(self, size=0):
        """ constructor

        Args:
            size (int, optional): [description]. Defaults to 0.
        """
        self.size = size

    @property
    def size(self):
        """[summary]

        Returns:
            [int]: [size]
        """
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """area

        Returns:
            [int]: [carrée]
        """
        return self.__size ** 2

    def __eq__(self, other):
        return self.area() == other.area()

    def __ne__(self, other):
        return self.area() != other.area()

    def __gt__(self, other):
        return self.area() > other.area()

    def __ge__(self, other):
        return self.area() >= other.area()

    def __lt__(self, other):
        return self.area() < other.area()

    def __le__(self, other):
        return self.area() <= other.area()
s_5 = Square(5)
s_6 = Square(6)

if s_5 < s_6:
    print("Square 5 < Square 6")
if s_5 <= s_6:
    print("Square 5 <= Square 6")
if s_5 == s_6:
    print("Square 5 == Square 6")
if s_5 != s_6:
    print("Square 5 != Square 6")
if s_5 > s_6:
    print("Square 5 > Square 6")
if s_5 >= s_6:
    print("Square 5 >= Square 6")