#!/usr/bin/python3
from add_0 import add as add1

if __name__ == "__main__":
    a = 1
    b = 2
    print("{:d} + {:d} = {:d}".format(a, b, add1(a, b)))
