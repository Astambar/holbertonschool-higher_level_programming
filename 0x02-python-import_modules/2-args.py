#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    lenargv = len(sys.argv) -1
    if lenargv == 0:
        print("0 arguments.")
    elif lenargv == 1:
        print("1 argument:")
        print("1: {:s}".format(sys.argv[1]))
    else:
        print("{:d} argument:".format(lenargv))
        for i in range(1, lenargv +1, 1):
            print("{:d}: {:s}".format(i, sys.argv[i]))
