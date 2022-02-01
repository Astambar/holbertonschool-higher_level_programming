#!/usr/bin/python3


def number_of_lines(filename=""):
    i = 0
    with open(filename) as file:
        for _ in file:
            i += 1
        return i
