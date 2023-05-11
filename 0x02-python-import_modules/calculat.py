#!/usr/bin/python3
from calculator_1 import add, sub, div, mul


def calculate(argv):
    num1 = int(argv[1])
    num2 = int(argv[3])
    operator = argv[2]
    if operator == "+":
        print("{:d} + {:d} = {:d}".format(num1, num2, add(num1, num2)))
    elif operator == "-":
        print("{:d} - {:d} = {:d}".format(num1, num2, sub(num1, num2)))
    elif operator == "*":
        print("{:d} * {:d} = {:d}".format(num1, num2, mul(num1, num2)))
    elif operator == "/":
        print("{:d} / {:d} = {:d}".format(num1, num2, div(num1, num2)))
