#!/usr/bin/python3
"""Magic class from a given ByteCode."""
import math


class MagicClass:
    """AI is creating summary for 

    Raises:
        TypeError: [description]

    Returns:
        [type]: [description]
    """

    def __init__(self, radius=0):
        """Initialization of the data."""
        self._MagicClass__radius = 0
        if type(radius) not in [int, float]:
            raise TypeError("radius must be a number")
        self._MagicClass__radius = radius

    def area(self):
        """Calculation of the area."""
        return self._MagicClass__radius ** 2 * math.pi

    def circumference(self):
        """Calculation of the circumference."""
        return 2 * math.pi * self._MagicClass__radius
