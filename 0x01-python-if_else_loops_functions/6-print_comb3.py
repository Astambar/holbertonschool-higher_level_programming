#!/usr/bin/python3
char = ""
for i in range(0, 8):
    for j in range(i + 1, 10):
        char += '{:d}{:d}'.format(i, j) + ', '
char += '{:d}{:d}'.format((i + 1), j)
print(char)
