#!/usr/bin/python3
def islower(c):
    c_ascii = ord(c)
    if c_ascii >= ord("a") and c_ascii <= ord("z") + 1:
        return True
    else:
        return False
