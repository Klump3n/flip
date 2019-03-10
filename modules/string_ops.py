#!/usr/bin/env python3
"""
Operations on strings.

"""
def flip_string(string):
    """
    Flip a string and replace certain chars with their symmetric counterparts.

    """
    rev_string = string[::-1]
    return rev_string

def pad_string(string, total_length=0):
    """
    Add padding to the right of the string.

    """
    str_len = len(string)
    if total_length < str_len:
        raise ValueError("Lenght of string is longer total string length")

    # add spaces to right side of string
    diff_len = total_length - str_len
    for _ in range(diff_len):
        string += " "

    return string

def replace_chars(string):
    """
    Replace certain characters in the string.

    Do this via a loop.

    """
    res = str()

    for char in string:

        if char == "b":
            char = "d"
        elif char == "d":
            char = "b"
        elif char == "/":
            char = "\\"
        elif char == "p":
            char = "q"
        elif char == "q":
            char = "p"
        elif char == "\\":
            char = "/"
        elif char == "`":
            char = "´"
        elif char == "´":
            char = "`"

        res += char

    return res
