#!/usr/bin/python3

def fizzbuzz():
    for i in range(100):
        if i % 3 == 0:
            if i % 5 == 0:
                print("FizzBuzz")
            else:
                print("Fizz")
        if i % 5 == 0:
            print("Buzz")
