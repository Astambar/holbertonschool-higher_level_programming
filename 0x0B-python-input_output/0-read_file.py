#!/usr/bin/python3
"""" This function have a reads file """


def read_file(filename=""):
    """
    The read_file function reads a text file and prints it to the console.

    :param filename=&quot;&quot;: Specify the name of the file to be read
    :return: A string object
    :doc-author: Trelent
    """
    with open(filename, mode="r", encoding="utf-8") as read_file:
        print(read_file.read(), end="")
