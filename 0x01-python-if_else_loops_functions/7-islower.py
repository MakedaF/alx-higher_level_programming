#!/usr/bin/python3
"""
Function that checks for lowercase character
"""
def islower(c):
    if ord(c) in range(97, 123):
        return True
    else:
        return False
