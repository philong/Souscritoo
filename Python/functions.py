#!/usr/bin/env python3


def one_out_of_two(string):
    result = ""
    n = 0
    for i, c in enumerate(string.lower()):
        if not c.isalpha():
            n = 1 - n
        result += c.upper() if i % 2 == n else c
    return result


def is_isogram(string):
    string = string.lower()
    for i, c in enumerate(string):
        if i != string.rindex(c):
            return False
    return True
