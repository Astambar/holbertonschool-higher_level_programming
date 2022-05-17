#!/usr/bin/python3
""" module documentation. """


class Square:
    """Représente un carré.
    Attribut d'instance privée : size :
        - Définition de la propriété size(self)
        - Pour modifier la taille def size(self, value)
    Attribut d'instance privée : position :
        -  Définition de la propriété position(self)
        - propriété setter def position(self, value)
    Instanciation avec taille par default.
    Méthode d'instance publique : def area(self).
    Méthode d'instance publique : def my_print(self).
    """

    def __init__(self, size=0, position=(0, 0)):
        """Initialise la classe Square"""
        self.size = size
        self.position = position

    @property
    def size(self):
        """Récupére la taille du carrée"""
        return self.__size

    @size.setter
    def size(self, value):
        """Définit la nouvelle de taille du carrée"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Retrieves the position."""
        return self.__position

    @position.setter
    def position(self, value):
        """Sets the position to a value."""
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Retourne la surface du carrée"""
        return self.__size ** 2

    def my_print(self):
        """Imprime sut l'entrer standard
        le carré avec le caractère #,
        à la position donnée par l'attribut position.
        """
        string = ""
        if self.__size == 0:
            string += "\n"
        else:
            for _ in range(self.__position[1]):
                string += "\n"
            for _ in range(self.__size):
                for _ in range(self.__position[0]):
                    string += " "
                for _ in range(self.__size):
                    string += "#"
                string += "\n"
        print(string, end="")
