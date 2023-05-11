#!/usr/bin/python3
import sys
from calculat import calculate
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
        calculate(sys.argv)
