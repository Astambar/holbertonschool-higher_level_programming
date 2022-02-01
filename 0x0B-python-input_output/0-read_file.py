#!/usr/bin/python3


def read_file(filename=""):
    """[summary]

    Args:
        filename (str, optional): [description]. Defaults to "".
    """
    with open(filename, encoding='UTF-8') as file:
        print(file.read(), end="")
