#!/usr/bin/python3
from sys import stderr


def safe_function(fct, *args):
    result = None
    try:
        result = fct(*args)
    except Exception as exception:
        print("Exception: {}".format(exception), file=stderr)
    return result
