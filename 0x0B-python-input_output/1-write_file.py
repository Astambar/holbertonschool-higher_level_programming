#!/usr/bin/python3
""" This function have a write_file """


def write_file(filename="", text=""):
    """
    The write_file function writes a string to a file.

    :param filename=&quot;&quot;: Specify the name of the file
    that will be written to
    :param text=&quot;&quot;: Pass a string to the function
    :return: None
    :doc-author: Trelent
    """

    with open(filename, mode="w", encoding="utf-8") as write_file:
        return write_file.write(text)
