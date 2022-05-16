#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    string = ""
    try:
        for i in range(x):
            string += f"{my_list[i]}"
    except IndexError:
        pass
    print(string)
    return i - 1
