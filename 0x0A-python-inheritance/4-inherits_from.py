#!/usr/bin/python3
"""[summary]
"""


def inherits_from(obj, a_class):
    """[summary]

    Args:
        obj ([type]): [description]
        a_class ([type]): [description]

    Returns:
        [type]: [description]
    """
    return (isinstance(obj, a_class) and (type(obj) is not a_class))
