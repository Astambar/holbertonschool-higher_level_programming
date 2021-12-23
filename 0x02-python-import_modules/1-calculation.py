#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, mul, div, sub
    a = 10
    b = 5
    char = "{:d} + {:d} = {:d}\n".format(a, b, add(a, b))
    char += "{:d} - {:d} = {:d}\n".format(a, b, sub(a, b))
    char += "{:d} * {:d} = {:d}\n".format(a, b, mul(a, b))
    char += "{:d} / {:d} = {:d}".format(a, b, div(a, b))
    print(char)
