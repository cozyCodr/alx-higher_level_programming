#!/usr/bin/python3
""" prints combinatiojn of numbers """

for x in range(10):
    for y in range(10):
        if x > y or x == y:
            continue
        if (x == 8 and y == 9):
            print("{}{}".format(x, y))
        else:
            print("{}{}".format(x, y), end=", ")
