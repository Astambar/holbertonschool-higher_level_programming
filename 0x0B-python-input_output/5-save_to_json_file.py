#!/usr/bin/python3
""" This function have a save_to_json_file """

import json


def save_to_json_file(my_obj, filename):
    """
    The save_to_json_file function writes an object to a text file,
    using a JSON representation.

    :param my_obj: Store the object that will be saved in the json file
    :param filename: Specify the file name to which the data is saved
    :return: None
    :doc-author: Trelent
    """

    with open(filename, mode="w", encoding="utf-8") as save_to_json_file:
        save_to_json_file.write(json.dumps(my_obj))
