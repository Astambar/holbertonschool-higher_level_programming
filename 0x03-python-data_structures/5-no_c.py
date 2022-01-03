#!/usr/bin/python3
def no_c(my_string):
	newstring =""
	if my_string:
		for i in my_string:
			if my_string[i] != "C" and my_string[i] != "c":
				newstring += my_string[i]
		return newstring
