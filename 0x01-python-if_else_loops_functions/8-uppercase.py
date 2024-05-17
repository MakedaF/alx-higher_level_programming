#!/usr/bin/python3
"""
prints uppercase followed by a new line
"""

def uppercase(str):
    for x in range(len(str)):
       # if ord(str[x]) in range(65, 91):
           # print("{}".format(str[x]), end="")
        if ord(str[x]) in range(97, 123):
            print("{}".format(chr(ord(str[x]) - 32)), end="")
    print()
