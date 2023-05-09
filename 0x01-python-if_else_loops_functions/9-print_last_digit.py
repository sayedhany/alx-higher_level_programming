#!/usr/bin/python3
def print_last_digit(number):
    remind = 10
    if number < 0:
        remind = -10
    last_digit = number % remind
    print("{:d}".format(abs(last_digit)), end="")
    return abs(last_digit)
