#!/usr/bin/python3
""" This function have a student class """


class Student:
    """ Information about the all students """
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

    def to_json(self):
        """
        The to_json function converts a Python object to a JSON string.


        :param self: Reference the object itself
        :return: A dictionary representation of the class
        :doc-author: Trelent
        """

        return self.__dict__
