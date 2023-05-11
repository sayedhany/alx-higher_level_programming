#!/usr/bin/python3
import sys
from calculator_1 import add, mul, div, sub
if __name__ == "__main__":
    operators = ["+", "-", "/", "*"]
    arglen = len(sys.argv)
    if arglen != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    elif sys.argv[2] not in operators:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    else:
        num1 = int(sys.argv[1])
        num2 = int(sys.argv[3])
        operator = sys.argv[2]
        if operator == "+":
                print("{:d} + {:d} = {:d}".format(num1, num2, add(num1, num2)))
        elif operator == "-":
                print("{:d} - {:d} = {:d}".format(num1, num2, sub(num1, num2)))
        elif operator == "*":
                print("{:d} * {:d} = {:d}".format(num1, num2, mul(num1, num2)))
        elif operator == "/":
                print("{:d} / {:d} = {:d}".format(num1, num2, div(num1, num2)))

