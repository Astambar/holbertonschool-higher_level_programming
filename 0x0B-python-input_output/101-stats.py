#!/usr/bin/python3
"""[summary]
"""


def print_stats(size, status_codes):
    """[summary]

    Args:
        size ([type]): [description]
        status_codes ([type]): [description]
    """
    print("File size: {}".format(size))
    for key in sorted(status_codes):
        print("{}: {}".format(key, status_codes[key]))

