#!/usr/bin/python3
import sys

args = sys.argv


def main():
    if len(args) <= 1:
        print("0 arguments.")
    elif len(args) == 2:
        print("1 argument:")
        print("1: {}".format(args[1]))
    else:
        print("{} arguments:".format(len(args) - 1))
        for index, arg in enumerate(args):
            if arg == args[0]:
                continue
            else:
                print("{}: {}".format(index, arg))


if __name__ == "__main__":
    main()
