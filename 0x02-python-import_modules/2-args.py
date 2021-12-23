#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    lenargv = len(sys.argv) -1
    if lenargv == 0:
        char = "0 arguments."
    elif lenargv == 1:
        char = "1 argument:\n"
        char += "1: {:s}".format(sys.argv[1])
    else:
        char = "{:d} argument:\n".format(lenargv)
        for i in range(1, lenargv +1, 1):
            char += "{:d}: {:s}\n".format(i, sys.argv[i])
    print(char, end="")
