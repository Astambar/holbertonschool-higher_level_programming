#!/usr/bin/python3
""" This function have a write_file """


def write_file(filename="", text=""):
    """ write this """
    with open(filename, mode="w", encoding="utf-8") as write_file:
        return write_file.write(text)
