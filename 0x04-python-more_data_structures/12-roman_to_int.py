#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string:
        return None
    num_roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total = 0
    prev_val = 0
    for word in roman_string:
        for key, value in num_roman.items():
            if key == word:
                total += value
                if prev_val < value:
                    total -= (prev_val * 2)
                    prev_val = value
    return total
