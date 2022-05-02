#!/usr/bin/python3
def multiple_returns(sentence):
    lensentence = len(sentence)
    return (lensentence, sentence[0] if lensentence > 0 else None)
