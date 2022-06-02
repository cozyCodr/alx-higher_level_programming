#!/usr/bin/python3
from sys import argv as args


def main():
    sum = 0

    for i in args:
        if i == args[0]:
            continue
        else:
            sum += int(i)

    print("{}".format(sum))


if __name__ == "__main__":
    main()
