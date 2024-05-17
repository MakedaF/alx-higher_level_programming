#!/usr/bin/python3
"""
Imports function add(a, b) from module add_0.py
"""

if __name__ == "__main__":
    from add_0 import add
    a = 1
    b = 2
    sum01 = add(a, b)
    print("{} + {} = {}".format(a, b, sum01))
