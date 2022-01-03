#!/usr/bin/python3
def multiple_returns(sentence):
    lensentence = len(sentence)
    return lensentence, None if lensentence == 0 else lensentence, sentence[0]
