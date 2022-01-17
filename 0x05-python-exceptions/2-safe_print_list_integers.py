#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    string = ""
    for i in range(x):
        try:
            string += "{:d}".format(my_list[i])
            count += 1
        except (ValueError, TypeError):
            continue
    print(string)
    return count
