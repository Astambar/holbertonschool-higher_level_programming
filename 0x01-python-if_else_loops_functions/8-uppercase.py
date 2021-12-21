#!/usr/bin/python3

def uppercase(str):
    for c in str[:]:
        val = ord(c)
        if val >= ord("a") and val <= ord("z") + 1:
            w = chr(val - 32)
        else:
            w = c
        print('{:s}'.format(w), end="")
    print()
