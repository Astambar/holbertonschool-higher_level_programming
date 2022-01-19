#!/usr/bin/python3
"""[summary]
    """


class Square:
    """AI is creating summary for

    Raises:
        TypeError: [description]
        ValueError: [description]
        TypeError: [description]
        TypeError: [description]
        TypeError: [description]

    Returns:
        [type]: [description]
    """

    def __init__(self, size=0, position=(0, 0)):
        """[summary]

        Args:
            size (int, optional): [description]. Defaults to 0.
            position (tuple, optional): [description]. Defaults to (0, 0).
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """[summary]

        Returns:
            [type]: [description]
        """
        return self.__size

    @size.setter
    def size(self, value):
        """[summary]

        Args:
            value ([type]): [description]

        Raises:
            TypeError: [description]
            ValueError: [description]
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """[summary]

        Returns:
            [type]: [description]
        """
        return self.__position

    @position.setter
    def position(self, value):
        """[summary]

        Args:
            value ([type]): [description]

        Raises:
            TypeError: [description]
            TypeError: [description]
            TypeError: [description]
        """
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """[summary]

        Returns:
            [type]: [description]
        """
        return self.__size ** 2

    def my_print(self):
        """AI is creating summary for my_print
        """
        string = ""
        if self.__size == 0:
            string += "\n"
        else:
            for _ in range(self.__position[1]):
                string += "\n"
            for _ in range(self.__size):
                for x in range(self.__position[0]):
                    string += " "
                for j in range(self.__size):
                    string += "#"
                string += "\n"
        print(string, end="")

    def __str__(self):
        """[summary]

        Returns:
            [char]: [string]
        """
        string = ""
        if self.__size != 0:
            for _ in range(self.position[1]):
                string += '\n'
            for i in range(self.__size):
                for k in range(self.position[0]):
                    string += ' '
                for _ in range(self.__size):
                    string += '#'
                if i != self.size - 1:
                    string += '\n'
        return string
