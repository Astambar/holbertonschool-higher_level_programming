#!/usr/bin/python3
""" This function defines the student class """


class Student:
    """ The student class """

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
        return {key: self.__dict__[key]
                for key in attrs if key in self.__dict__}
