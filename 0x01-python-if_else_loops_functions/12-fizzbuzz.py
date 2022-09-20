#!/usr/bin/python3

def fizzbuzz():
    fizzbuzz = ""

    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            fizzbuzz += " FizzBuzz"
        elif i % 3 == 0:
            fizzbuzz += " Fizz"
        elif i % 5 == 0:
            fizzbuzz += "Buzz"
        else:
            if i == 1:
                fizzbuzz += str(i)
            else:
                fizzbuzz = fizzbuzz + " " + str(i)
    print(fizzbuzz)
