#!/usr/bin/python3
"""[summary]
"""


def add_integer(a, b=98):
    """[summary]

    Args:
        a ([type]): [description]
        b (int, optional): [description]. Defaults to 98.

    Raises:
        TypeError: [description]
        TypeError: [description]

    Returns:
        [type]: [description]
    """
    if type(a) == float or type(b) == float:
        a = int(a)
        b = int(b)

    if type(a) != int:
        raise TypeError("a must be an integer")
    elif type(b) != int:
        raise TypeError("b must be an integer")
    else:
        return a + b
