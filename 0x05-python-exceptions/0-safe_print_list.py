#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    increment = 0
    string = ""
    try:
        for i in range(x):
            string += "{}".format(my_list[i])
            increment += 1
    except IndexError:
        pass
    print(string)
    return increment
my_list = [1, 2, 3, 4, 5]

nb_print = safe_print_list(my_list, 2)
print("nb_print: {:d}".format(nb_print))
nb_print = safe_print_list(my_list, len(my_list))
print("nb_print: {:d}".format(nb_print))
nb_print = safe_print_list(my_list, len(my_list) + 2)
print("nb_print: {:d}".format(nb_print))