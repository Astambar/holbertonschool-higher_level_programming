#!/usr/bin/python3
""" This function have a load_from_json_file """

import json


def load_from_json_file(filename):
    """
    The load_from_json_file function reads a json file and returns the object

    :param filename: Specify the file to load from
    :return: The content of the file in a string format
    :doc-author: Trelent
    """

    with open(filename, mode="r", encoding="utf-8") as load_from_json_file:
        return json.load(load_from_json_file)
