#!/usr/bin/python3
from sys import argv as args
from calculator_1 import add, sub, mul, div


def main():
    length = len(args) - 1
    if length != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        return (1)

    a = int(args[1])
    b = int(args[3])
    op = str(args[2])

    if (op == '+') or (op == '-') or (op == '*') or (op == '/'):
        if op == '+':
            print("{} + {} = {}".format(a, b, add(a, b)))

        elif op == '-':
            print("{} - {} = {}".format(a, b, sub(a, b)))

        elif op == '*':
            print("{} * {} = {}".format(a, b, mul(a, b)))

        elif op == '/':
            print("{} / {} = {}".format(a, b, div(a, b)))

    else:
        print("Unknown operator. Available operators: +, -, * and /")
        return (1)


if __name__ == '__main__':
    main()
