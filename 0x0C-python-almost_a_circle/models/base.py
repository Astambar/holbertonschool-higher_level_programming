#!/usr/bin/python3
"""[summary]

Returns:
    [type]: [description]
"""

import json
from os.path import exists


class Base:
    """[summary]

    Returns:
        [type]: [description]
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """[summary]

        Args:
            id ([type], optional): [description]. Defaults to None.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """[summary]

        Args:
            list_dictionaries ([type]): [description]

        Returns:
            [type]: [description]
        """
        return "[]" if list_dictionaries is None else json.dumps(
                                                list_dictionaries)


if __name__ == "__main__":

    b1 = Base()
    print(b1.id)

    b2 = Base()
    print(b2.id)

    b3 = Base()
    print(b3.id)

    b4 = Base(12)
    print(b4.id)

    b5 = Base()
    print(b5.id)
