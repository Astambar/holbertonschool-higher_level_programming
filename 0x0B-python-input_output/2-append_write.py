#!/usr/bin/python3
""" This function have a append_file"""


def append_write(filename="", text=""):
    """ write this """
    with open(filename, mode="a", encoding="utf-8") as append_write:
        return append_write.write(text)
