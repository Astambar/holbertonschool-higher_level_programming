#!/usr/bin/python3
def uppercase(str):
	newstr = ""
	for i in str[:]:
		c = ord(i)
		if c >= ord("a") and c <= ord("z") + 1:
			w = chr(c - 32)
		else:
			w = c
		newstr += '{:s}'.format(w)
	print(newstr, end="\n")
