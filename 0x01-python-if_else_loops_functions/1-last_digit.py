#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    pnumber = number * -1
    x = pnumber % 10
else:
    x = number % 10
if x > 5:
    print("Last digit of {:d} is {:d} and is greater than 5".format(number, x))
elif x == 0:
    print("Last digit of {:d} is {:d} and is 0".format(number, x))
else:
    print("Last digit of {:d} is {:d} and is less than 6 and not 0".format(number, x))
