#!/usr/bin/python3
"""
print numbers 1 to 100 separated by space.
sustitute Fizz for multiples of 3,
Buzz  for multiple of 5,
and FizzBuzz for multiple of both
"""


def fizzbuzz():
    for x in range(1, 101):
        if x % 3 == 0 and x % 5 == 0:
            print("FizzBuzz ", end="")
        elif x % 3 == 0:
            print("Fizz ", end="")
        elif x % 5 == 0:
            print("Buzz ", end="")
        else:
            print("{} ".format(x), end="")
