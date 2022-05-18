#!/usr/bin/python3
""" module documentation. """


class Square:
    """Représente un carré.
    Attribut d'instance privée : size :
        - Taille de la propriété (self)
        - Pour modifier la taille def size(self, value)
    Instanciation avec taille par default.
    Méthode d'instance publique : def area(self).
    Méthode d'instance publique : def my_print(self).
    """

    def __init__(self, size=0):
        """Initialise la classe Square"""
        self.__size = size

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

    def area(self):
        """Retourne la surface du carrée"""
        return self.__size ** 2

    def my_print(self):
        """Imprime sur la sortie standard
        le carré avec le caractère #.
        """

        if self.__size == 0:
            print()
        else:
            string = ""
            for i in range(self.__size):
                for _ in range(self.__size):
                    string += "#"
                if i < self.__size:
                    string += '\n'
            print(string, end="")
