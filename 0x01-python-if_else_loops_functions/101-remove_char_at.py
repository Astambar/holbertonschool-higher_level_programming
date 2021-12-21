#!/usr/bin/python3
def remove_char_at(str, n):
    newstring = ""
    for i in range(len(str)):
        if i != n:
            newstring += str[i]
    return newstring
