#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    malist = list(my_list)
    if(idx < 0 or idx > len(my_list) - 1):
        return my_list
    malist[idx] = element
    return malist
