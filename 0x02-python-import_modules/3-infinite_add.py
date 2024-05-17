#!/usr/bin/python3
import sys

if __name__ == "__main__":
    arg = sys.argv
    x = len(arg) - 1
    result = 0
    for i in range(1, x + 1):
        result += int(arg[i])
    print(result)
