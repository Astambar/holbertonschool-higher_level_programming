#!/usr/bin/python3
def uniq_add(my_list=[]):
	if my_list:
		return sum(i for i in set(my_list))
my_list = [1, 2, 3, 1, 4, 2, 5]
result = uniq_add(my_list)
print("Result: {}".format(result))
