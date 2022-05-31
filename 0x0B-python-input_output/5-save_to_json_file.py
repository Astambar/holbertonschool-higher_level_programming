#!/usr/bin/python3
""" This function have a save_to_json_file """

import json


def save_to_json_file(my_obj, filename):
    """ Using and save the save_to_json_file """
    with open(filename, mode="w", encoding="utf-8") as save_to_json_file:
        save_to_json_file.write(json.dumps(my_obj))
