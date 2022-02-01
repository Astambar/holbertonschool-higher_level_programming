#!/usr/bin/python3


def read_lines(filename="", nb_lines=0):
    with open(filename, encoding="UTF-8") as file:
        if nb_lines <= 0:
            print(file.read(), end="")
            return
        i = sum(1 for _ in file)
        file.seek(0)
        if nb_lines >= i:
            print(file.read(), end="")
            return
        else:
            i = 0
            while i < nb_lines:
                print(file.readline(), end="")
                i += 1
