#!/usr/bin/python3
""" module documentation. """


class Square:
    """Représente un carré.
    Attribut d'instance privée : size :
        - Taille de la propriété (self)
        - Pour modifier la taille def size(self, value)
    Instanciation avec taille par default.
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
