#!/usr/bin/python3
"""function that returns a set of common elements in two sets
    Return:
        the addition of all unique elemnts
"""

def uniq_add(my_list=[]):
	if my_list:
		return sum(i for i in set(my_list))
