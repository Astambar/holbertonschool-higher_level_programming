#!/usr/bin/python3
""" This function defines the student class """


class Student:
    """ The student class """

    def __init__(self, first_name, last_name, age):
        """ Initializate class """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        # sourcery skip: dict-comprehension, inline-immediately-returned-variable
        """ returns the dictionary """
        if attrs is None:
            return self.__dict__
    
        new_aux = {}

        for key in attrs:
            if key in self.__dict__:
                new_aux[key] = self.__dict__[key]

        return new_aux