#!/usr/bin/python3
""" This function have a student class """


class Student:
    """ Information about the all students """
    def __init__(self, first_name, last_name, age):
        """ Initializate """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """The directory"""
        return self.__dict__
