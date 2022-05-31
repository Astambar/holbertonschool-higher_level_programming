#!/usr/bin/python3
"""Defines a text file insertion function."""


def append_after(filename="", search_string="", new_string=""):
    """
    The append_after function appends a new string
    to the end of each line that contains a specific substring.

    :param filename=&quot;&quot;: Specify the name of the file
    that will be opened
    :param search_string=&quot;&quot;: Search for a string in the file
    :param new_string=&quot;&quot;: Add a new string after the search_string
    :return: A string
    :doc-author: Trelent
    """

    text = ""
    with open(filename) as read:
        for line in read:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, "w") as write:
        write.write(text)
