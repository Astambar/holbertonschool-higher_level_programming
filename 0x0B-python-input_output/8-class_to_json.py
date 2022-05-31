#!/usr/bin/python3
""" This function have a class_to_json """


def class_to_json(obj):
    """
    The class_to_json function takes a class object and returns the dictionary
    representation of it. This is useful for converting objects to JSON format.
    
    :param obj: Pass in the class object that needs to be converted into a json string
    :return: A dictionary of the class attributes
    :doc-author: Trelent
    """
    return obj.__dict__
