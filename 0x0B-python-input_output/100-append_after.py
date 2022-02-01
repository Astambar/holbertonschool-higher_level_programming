#!/usr/bin/python3
"""Defines a text file insertion function."""


def append_after(filename="", search_string="", new_string=""):
    """[summary]

    Args:
        filename (str, optional): [description]. Defaults to "".
        search_string (str, optional): [description]. Defaults to "".
        new_string (str, optional): [description]. Defaults to "".
    """
    text = ""
    with open(filename) as r:
        for line in r:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, "w") as w:
        w.write(text)
