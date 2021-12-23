#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    lenargv = len(sys.argv) -1
    print("{:d} ".format(lenargv), end="")
    if lenargv == 0:
        print("arguments.")
    elif lenargv == 1:
        print("argument:")
        print("1: {:s}".format(sys.argv[1]))
    else:
        print("{:d} argument:".format(lenargv))
        for i in range(1, lenargv +1, 1):
            print("{:d}: {:s}".format(i, sys.argv[i]))
