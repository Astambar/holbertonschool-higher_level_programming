#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    string = ""
    increment = 0
    try:
        for i in range(x):
            string += f"{my_list[i]}"
            increment += 1
    except IndexError:
        pass
    print(string)
    return increment
