#!/usr/bin/python3
"""[summary]
"""


def add_attribute(obj, name, value):
    """[summary]

    Args:
        obj ([type]): [description]
        name ([type]): [description]
        value ([type]): [description]

    Raises:
        TypeError: [description]
    """
    if "__dict__" in dir(obj):
        setattr(obj, name, value)
    else:
        raise TypeError("can't add new attribute")
