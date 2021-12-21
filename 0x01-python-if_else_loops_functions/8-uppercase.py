#!/usr/bin/python3
def uppercase(str):
	newstr = ""
	for i in str[:]:
		c = ord(i)
		if c >= ord("a") and c <= ord("z") + 1:
			c = chr(c - 32)
		newstr += '{:s}'.format(c)
	print("{:s}".format(newstr), end="")
