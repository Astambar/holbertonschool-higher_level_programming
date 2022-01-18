#!/usr/bin/python3
""" module documentation. """


class Square:
    """Represents a square.
    Private instance attribute: size:
        - property def size(self)
        - property setter def size(self, value)
    Private instance attribute: position:
        - property def position(self)
        - property setter def position(self, value)
    Instantiation with optional size and optional position.
    Public instance method: def area(self).
    Public instance method: def my_print(self).
    """

    def __init__(self, size=0, position=(0, 0)):
        """Initializes the data."""
        self.size = size
        self.position = position

    @property
    def size(self):
        """Retrieves the size."""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size to a value."""
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
        """Returns the current square area."""
        return self.__size ** 2

    def my_print(self):
        """Prints to stdout the square with the character #,
        at the position given by the position attribute.
        """
        if self.__size == 0:
            print()
            return
        for y in range(0, self.__position[1]):
            print()
        for i in range(0, self.__size):
            for x in range(0, self.__position[0]):
                print(" ", end="")
            for j in range(0, self.__size):
                print("#", end="")
            print()
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
        """Imprime sur la sortie standard
        le carré avec le caractère #.
        """
        string = ""
        if self.__size == 0:
            string += "\n"
        for y in range(0, self.__position[1]):
            string += "\n"
        for i in range(0, self.__size):
            for x in range(0, self.__position[0]):
                string += " "
            for j in range(0, self.__size):
                string += "#"
            if i < self.__size:
                string += '\n'
        print(string)
