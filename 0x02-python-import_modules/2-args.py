#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    lenargv = len(sys.argv) - 1
    print("{} ".format(lenargv), end="")
    if lenargv == 0:
        print("arguments.")
    elif lenargv > 1:
        print("arguments:")
        for i in range(1, lenargv + 1, 1):
            print("{}: {}".format((i), sys.argv[i]))
    else:
        print("argument:")
        print("1: {}".format(sys.argv[1]))
