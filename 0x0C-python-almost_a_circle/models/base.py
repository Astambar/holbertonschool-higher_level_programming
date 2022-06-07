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
        """
        The __init__ function is called the constructor and is always called when creating an instance of a class.
        It is used to initialize data attributes of an object. In this case, it initializes the id attribute.
        
        :param self: Refer to the current instance of the class
        :param id=None: Set the id of the object to a specific value
        :return: The object itself
        :doc-author: Trelent
        """
        
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @classmethod
    def save_to_file(cls, list_objs):
        """
        The save_to_file function writes a JSON string representation of the object
        to a file.
        
        
        :param cls: Call the to_json_string method from the class that is calling it
        :param list_objs: Check if the list of objects is empty or not
        :return: None
        :doc-author: Trelent
        """
        
        string = ""

        if list_objs is None:
            list_objs = []

        dict = [obj.to_dictionary() for obj in list_objs]

        string = cls.to_json_string(dict)

        with open(f"{cls.__name__}.json", "w") as fd:
            fd.write(string)
        fd.close()

    @classmethod
    def create(cls, **dictionary):
        """
        The create function creates a new instance of the class,
        and takes as arguments all attributes that are required to create an instance.
        If one of the attributes is not passed in, it will default to None.
        
        :param cls: Call the class rectangle or square
        :param **dictionary: Update the attributes of the instance
        :return: The new object
        :doc-author: Trelent
        """
        
        new = cls(1, 1) if cls.__name__ == "Rectangle" else cls(1)

        new.update(**dictionary)

        return new

    @classmethod
    def load_from_file(cls):
        """
        The load_from_file function is a function that takes in a class and loads the data from the file
        and returns an instance of it. If there is no file, then it will return an empty list.
        
        :param cls: Call the class that is being used
        :return: A list of instances
        :doc-author: Trelent
        """
        
        list_json = []
        list_instance = []

        if exists(f"{cls.__name__}.json"):
            with open(f"{cls.__name__}.json") as fd:
                list_json = cls.from_json_string(fd.read())
            fd.close()

            list_instance.extend(cls.create(**i) for i in list_json)

        return list_instance

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        The save_to_file_csv function writes a list of objects to a csv file.
            Args:
                cls (class): The class name of the object being written to the file.
                list_objs (list): A list of objects that will be written to the file.
        
            Returns:
                None,
        
        :param cls: Determine the name of the class
        :param list_objs: Save the list of objects to a file
        :return: None
        :doc-author: Trelent
        """
        
        rectangle_list = ["id", "width", "height", "x", "y", "\0"]
        square_list = ["id", "size", "x", "y", "\0"]
        write_list = ""

        if list_objs is None:
            list_objs = []

        with open(f"{cls.__name__}.csv", "w") as fd:
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
        """
        The load_from_file_csv function creates a list of instances from a csv file.
        The function takes the name of the class as an argument and creates an instance
        of that class for each line in the csv file. The function returns a list with all 
        the new instances.
        
        :param cls: Call the class name
        :return: The list of instances
        :doc-author: Trelent
        """
        
        list_instance = []

        if exists(f"{cls.__name__}.csv"):
            with open(f"{cls.__name__}.csv", "r") as fd:
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
        """
        The to_json_string function converts a list of dictionaries into a json string.
            Args:
                list_dictionaries (list): A list of dictionaries.
        
            Returns:
                str: The JSON string representation of the object.
        
        :param list_dictionaries: Check if the list is empty or not
        :return: A string representation of the list_dictionaries parameter
        :doc-author: Trelent
        """
        
        return "[]" if list_dictionaries is None else json.dumps(
                                                list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """
        The from_json_string function converts a JSON string to a Python object.
        
        Parameters:
            json_string (str): A JSON string.  The value can be any Python-supported data type.
        
            Returns:
                list, dict, str, int, float: A Python object constructed from the provided JSON string.
        
        :param json_string: Pass a string that contains a json object
        :return: A list of dictionaries
        :doc-author: Trelent
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
