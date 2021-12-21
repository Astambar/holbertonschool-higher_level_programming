#!/usr/bin/python3
def uppercase(str):
    for c in str[:]:
        char = ord(c)
        if char >= ord("a") and char <= ord("z") + 1:
            w = chr(char - 32)
        else:
            w = c
        print('{:s}'.format(w), end="")
    print()
