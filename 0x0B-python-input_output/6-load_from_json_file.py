#!/usr/bin/python3
""" This function have a load_from_json_file """

import json


def load_from_json_file(filename):
    """ json load """
    with open(filename, mode="r", encoding="utf-8") as load_from_json_file:
        return json.load(load_from_json_file)
