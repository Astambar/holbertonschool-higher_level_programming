#!/usr/bin/python3
""" module documentation. """


class Square:
    """Représente un carré.
    Attribut d'instance privée : size.
    Instanciation avec taille (pas de vérification type/valeur).
    """

    def __init__(self, size):
        """Initializes the data."""
        self.__size = size
