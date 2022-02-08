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
    def save_to_file(cls, list_objs):
        """[summary]

        Args:
            list_objs ([type]): [description]
        """
        string = ""

        if list_objs is None:
            list_objs = []

        dict = [obj.to_dictionary() for obj in list_objs]

        string = cls.to_json_string(dict)

        with open(cls.__name__ + ".json", "w") as fd:
            fd.write(string)
        fd.close()

    @classmethod
    def create(cls, **dictionary):
        """[summary]

        Returns:
            [type]: [description]
        """
        new = cls(1, 1) if cls.__name__ == "Rectangle" else cls(1)

        new.update(**dictionary)

        return new

    @classmethod
    def load_from_file(cls):
        """[summary]

        Returns:
            [type]: [description]
        """
        list_json = []
        list_instance = []

        if exists(cls.__name__ + ".json"):
            with open(cls.__name__ + ".json") as fd:
                list_json = cls.from_json_string(fd.read())
            fd.close()

            for i in list_json:
                list_instance.append(cls.create(**i))

        return list_instance

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """[summary]

        Args:
            list_objs ([type]): [description]
        """
        rectangle_list = ["id", "width", "height", "x", "y", "\0"]
        square_list = ["id", "size", "x", "y", "\0"]
        write_list = ""

        if list_objs is None:
            list_objs = []

        with open(cls.__name__ + ".csv", "w") as fd:
            if list_objs is None or list_objs == []:
                fd.write("")
            else:
                if cls.__name__ == "Rectangle":
                    write_list = rectangle_list
                elif cls.__name__ == "Square":
                    write_list = square_list

                list_dict = csv.DictWriter(fd, fieldnames=write_list)
                for obj in list_objs:
                    list_dict.writerow(obj.to_dictionary())

        fd.close()

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
