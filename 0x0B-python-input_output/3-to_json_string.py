#!/usr/bin/python3
""" This function have a to_json_string """

import json


def to_json_string(my_obj):
    """
    The to_json_string function accepts a dictionary as input
    and returns a JSON string representation of it.


    :param my_obj: Pass in the object that will be converted to a json string
    :return: A string representation of my_obj in json format
    :doc-author: Trelent
    """

    return json.dumps(my_obj)
