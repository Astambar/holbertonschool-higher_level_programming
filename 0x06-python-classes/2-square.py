#!/usr/bin/python3
""" module documentation. """


class Square:
    """Représente un carré.
    Attribut d'instance privée : size.
    Instanciation avec taille par default.
    """

    def __init__(self, size=0):
        """
        The __init__ function is called automatically every time the class is
        used to create a new object.
        The first argument of the __init__ function is
        always a reference to the instance of
        the class itself (by convention this is named self).
        This allows us to access or modify attributes of our objects, as
        the attributes are actually stored in self.__dict__.

        :param self: Represent the instance of the object itself
        :param size=0: Initialise the size of the square
        :return: The instance of the object created
        :doc-author: Trelent
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
