#!/usr/bin/python3
import sys

if __name__ == "__main__":
    arg = sys.argv
    x = len(arg) - 1

    if x == 0:
        print("0 arguments.")
    elif x == 1:
        print("1 argument:")
    else:
        print(f"{x} arguments:")
    for i in range(1, x + 1):
        print(f"{i}: {arg[i]}")
