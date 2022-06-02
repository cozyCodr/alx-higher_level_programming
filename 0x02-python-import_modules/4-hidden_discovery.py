#!/usr/bin/python3
import hidden_4 as hdm


def main():
    lis = dir(hdm)

    for i in lis:
        if i[0] == '_':
            continue
        else:
            print(i)


if __name__ == '__main__':
    main()
