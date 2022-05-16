#!/usr/bin/python3
import contextlib

def safe_print_list(my_list=[], x=0):
    string = ""
    with contextlib.suppress(IndexError):
        for i in range(x):
            string += f"{my_list[i]}"

    print(string)
    return increment
