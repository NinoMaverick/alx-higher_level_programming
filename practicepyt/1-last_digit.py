#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if number < 0:
    last_num = -1 * (abs(number) % 10)
else:
    last_num = number % 10

if (last_num > 5):
    print(f"Last digit of {number} is {last_num} and is greater than 5")
elif (number % 10 == 0):
    print(f"Last digit of {number} is {last_num} and is 0")
elif (number % 10 < 6 and number % 10 != 0):
    print(f"Last digit of {number} is {last_num} and is less than 6 and not 0")
          