#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    lenargv = len(sys.argv) - 1
    char = "{:d} ".format(lenargv)
    if lenargv == 0:
        char += "arguments.\n"
    elif lenargv > 1:
        char += "arguments:\n"
        for i in range(1, lenargv + 1, 1):
            char += "{}: {}\n".format((i), sys.argv[i])
    else:
        char += "argument:\n"
        char += "1: {}\n".format(sys.argv[1])
    print(char, end="")
