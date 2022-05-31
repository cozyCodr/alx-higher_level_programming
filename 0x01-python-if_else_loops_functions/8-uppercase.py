#!/usr/bin/python3

def uppercase(str):
    newstring = ""
    for i in str:
        if ord(i) in range(97, 123):
            newstring += chr(ord(i) - 32)
        else:
            newstring += i
    return newstring
