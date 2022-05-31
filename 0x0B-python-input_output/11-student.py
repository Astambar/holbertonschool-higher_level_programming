#!/usr/bin/python3
""" This function have the class "Student" """


class Student:
    """ Students information """
    def __init__(self, first_name, last_name, age):
        """
        The __init__ function is called automatically every time
        the class is being used to create a new object.
        The __init__ function can accept arguments,
        but self is always the first one.
        This function is used to initialize the objects it creates.

        :param self: Refer to the instance of the class
        :param first_name: Set the first name of the person
        :param last_name: Set the last name of the person
        :param age: Set the age of the person
        :return: Nothing
        :doc-author: Trelent
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        The to_json function is a method that takes in an optional
        list of attributes.
        If no attributes are passed,
        it returns the entire dictionary representation of the object.
        Otherwise,
        it creates a new dictionary with only those attributes and values.
        :param self: Access the attributes and methods of the class
        :param attrs=None: Pass a list of strings as arguments
        :return: A dictionary of the class instance's attributes
        :doc-author: Trelent
        """
        if attrs is None:
            return self.__dict__
        else:
            return {i: self.__dict__[i] for i in attrs if i in self.__dict__}

    def reload_from_json(self, json):
        """
        The reload_from_json function allows the user
        to reload a previously saved
        instance of an object from its JSON representation.
        This function is useful for
        reloading instances after they have been modified,
        or if you want to see what
        the instance looks like in JSON format.
        The function takes one argument: json,
        which is a dictionary

        :param self: Reference the class itself
        :param json: Load the data from a json file
        :return: A dictionary with the key-value pairs of the json file
        :doc-author: Trelent
        """
        for a in json:
            self.__dict__[a] = json[a]
