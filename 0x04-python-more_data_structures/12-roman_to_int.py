#!/usr/bin/python3
def roman_to_int(roma_string):
    if roma_string is None or isinstance(roma_string, str) is False:
        return 0
    letters = {'I': 1, 'V': 5,  'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    reverse_num = roma_string[::-1]
    maxchar = 'I'
    total = 0
    for i in reverse_num:
        if letters[i] >= letters[maxchar]:
            maxchar = i
            total += letters[i]
        else:
            total -= letters[i]
    return total
