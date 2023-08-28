#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
h = abs(number) % 10
if number < 0:
    h = -h
if h > 5:
    print("Last digit of {} is {} and is greater than 5" .format(number, h))
elif h == 0:
    print("Last digit of {} is {} and is 0" .format(number, h))
else:
    print(f"Last digit of {number} is {h} and is less than 6 and not 0")
