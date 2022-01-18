#!/usr/bin/python3
""" module documentation. """


class Square:
    """Représente un carré.
    Attribut d'instance privée : size.
    Instanciation avec taille par default.
    Méthode d'instance publique : def area(self).
    """

    def __init__(self, size=0):
        """Initialise la classe Square"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Retourne la surface du carrée"""
        return self.__size ** 2
