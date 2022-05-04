#!/usr/bin/python3
"""fonction  d'addition de nombre de la liste (de façon unique)
    Return:
        addition de nombre unique
"""


def uniq_add(my_list=[]):
    unique_number = []

    for i in my_list:
        if i not in unique_number:
            unique_number.append(i)
    return sum(unique_number)
