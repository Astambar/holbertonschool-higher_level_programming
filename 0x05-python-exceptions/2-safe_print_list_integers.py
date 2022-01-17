#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    increment = 0
    string = ""
    for i in range(x):
        try:
            string +="{:d}".format(my_list[i])
            increment += 1
        except (TypeError, ValueError):
            pass
    print(string)
    return (increment)
