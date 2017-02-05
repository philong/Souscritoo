#!/usr/bin/env python3

def one_out_of_two(string):
    result = ""
    i = 0
    for char in string.lower():
        if char.isalpha():
            c = char.upper() if i % 2 == 0 else char
            i += 1
        else:
            c = char
        result += c
    return result


def is_isogram(string):
    string = string.lower()
    for i, c in enumerate(string):
        if i != string.rindex(c):
            return False
    return True
