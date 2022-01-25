#!/usr/bin/python3
"""[summary]
"""

def max_integer(list=[]):
    """[summary]

    Args:
        list (list, optional): [description]. Defaults to [].

    Returns:
        [type]: [description]
    """
    if len(list) == 0:
        return None
    result = list[0]

    for i in list:
        if i > result:
            result = i
    return result
