#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None or a_dictionary == {}:
        return None
    keys = list(a_dictionary.keys())
    maxnum = keys[0]
    for num in keys:
        maxnum = num if a_dictionary[num] > a_dictionary[maxnum] else maxnum
    return maxnum
