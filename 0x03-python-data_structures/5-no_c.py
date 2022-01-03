#!/usr/bin/python3
def no_c(my_string):
	newstring =""
	if my_string:
		for i in my_string:
			if my_string[i] not in 'Cc':
				newstring += my_string[i]
		return newstring
