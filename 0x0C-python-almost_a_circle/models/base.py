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


    @classmethod
    def load_from_file_csv(cls):
        """[summary]

        Returns:
            [type]: [description]
        """
        list_instance = []

        if exists(cls.__name__ + ".csv"):
            with open(cls.__name__ + ".csv", "r") as fd:
                list_csv = csv.reader(fd)
                for i in list_csv:
                    if cls.__name__ == "Rectangle":
                        new = {
                            "id": int(i[0]),
                            "width": int(i[1]),
                            "height": int(i[2]),
                            "x": int(i[3]),
                            "y": int(i[4])
                        }

                    if cls.__name__ == "Square":
                        new = {
                            "id": int(i[0]),
                            "size": int(i[1]),
                            "x": int(i[2]),
                            "y": int(i[3])
                        }

                    new_instance = cls.create(**new)
                    list_instance.append(new_instance)

        return list_instance

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

    @staticmethod
    def from_json_string(json_string):
        """[summary]

        Args:
            json_string ([type]): [description]

        Returns:
            [type]: [description]
        """
        return [] if json_string in [None, ""] else json.loads(json_string)


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
