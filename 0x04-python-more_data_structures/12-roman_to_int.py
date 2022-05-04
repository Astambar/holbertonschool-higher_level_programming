#!/usr/bin/python3
def roman_to_int(roma_string):
    if roma_string is None or not isinstance(roma_string, str):
        return 0
    roman_number = {
                'I': 1,
                'V': 5,
                'X': 10,
                'L': 50,
                'C': 100,
                'D': 500,
                'M': 1000
                }
    maxchar = 'I'
    result = 0
    for i in roma_string[::-1]:
        if roman_number[i] >= roman_number[maxchar]:
            maxchar = i
            result += roman_number[i]
        else:
            result -= roman_number[i]
    return result
