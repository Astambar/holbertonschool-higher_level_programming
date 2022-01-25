#!/usr/bin/python3
"""[summary]
"""


def print_square(size):
    """[summary]

    Args:
        size ([type]): [description]

    Raises:
        TypeError: [description]
        TypeError: [description]
        ValueError: [description]

    Returns:
        [type]: [description]
    """
    if type(size) != int:
        raise TypeError("size must be an integer")
    if type(size) == float and size < 0:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if size == 0:
        return None

    for _ in range(size):
        print('#' * size)
