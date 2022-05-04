#!/usr/bin/python3
"""function that returns a set of common elements in two sets
    Return:
        the addition of all unique elemnts
"""


def uniq_add(my_list=[]):
    unique_number = []

    for i in my_list:
        if i not in unique_number:
            unique_number.append(i)
    return sum(unique_number)
