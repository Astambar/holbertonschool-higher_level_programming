#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list:
        return sum(tuple(s * w for s, w in my_list))/sum(i[1] for i in my_list)
    return 0
