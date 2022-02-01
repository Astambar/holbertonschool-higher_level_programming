#!/usr/bin/python3
"""" This function have a reads file """


def read_file(filename=""):
    """ read the text file """
    with open(filename, mode="r", encoding="utf-8") as read_file:
        print(read_file.read(), end="")
