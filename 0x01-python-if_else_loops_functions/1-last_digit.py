#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_str = str(number)
last_num = int(last_str[-1])
if last_num > 5:
    print(f"Last digit of {number} is {last_str} and is greater than 5")
elif last_num == 0:
    print(f"Last digit of {number} is {last_str} and is zero")
elif last_num < 6 and last_num != 0:
    print(f"Last digit of {number} is {last_str} and is less than 6 and not 0")
