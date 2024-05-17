#!/usr/bin/python3
"""
prints uppercase followed by a new line
"""


def uppercase(str):
    result = ""
    for x in str:
        if ord(x) in range(97, 123):
            upper_char = chr(ord(x) - 32)
        else:
            upper_char = x
        result += upper_char
    print("{}".format(result))
