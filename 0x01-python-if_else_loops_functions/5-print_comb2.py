#!/usr/bin/python3
char = ""
for i in range(0, 99):
    char += '{:d}{:d}'.format(i // 10, i % 10) + ', '
char += '{:d}{:d}'.format((i + 1) // 10, (i + 1) % 10)

print(char)
