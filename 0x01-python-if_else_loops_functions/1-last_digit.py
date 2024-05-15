#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
x = abs(number)
if (x % 10) == 0:
    a = f"Last digit of {number} is {x % 10}"
    a0 = " and is 0"
    print(a + a0)
elif number < 0:
    a = f"Last digit of {number} is {-1 *(x % 10)}"
    a1 = " and is less than 6 and not 0"
    print(a + a1)
elif number > 0 and (x % 10) != 0 and (x % 10) < 6:
    a = f"Last digit of {number} is {number % 10}"
    a1 = " and is less than 6 and not 0"
    print(a + a1)
elif (x % 10) > 5:
    a = f"Last digit of {number} is {number % 10}"
    b = " and is greater than 5"""
    print(a + b)
