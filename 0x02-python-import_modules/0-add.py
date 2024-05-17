#!/usr/bin/python3
"""
Imports function add(a, b) from module add_0.py
"""

if __name__ == "__main__":
    import add_0 as sum01
    a = 1
    b = 2
    print("{} + {} = {}".format(a, b, sum01.add(a, b)))
