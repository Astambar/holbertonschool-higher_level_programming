#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    modulo = number % -10
else:
    modulo = number % 10
chardefault = 'Last digit of {:d} is {:d} '.format(number, modulo)
if modulo > 5:
    print('{:s} and is greater than 5'.format(chardefault))
elif modulo == 0:
    print('{:s} and is 0'.format(chardefault))
else:
    print('{:s} and is less than 6 and not 0'.format(chardefault))
