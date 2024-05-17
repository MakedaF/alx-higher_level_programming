#!/usr/bin/python3
"""
prints the last digits of a number
"""


def print_last_digit(number):
    x = abs(number) % 10
    print("{}".format(x), end="")
    return x
