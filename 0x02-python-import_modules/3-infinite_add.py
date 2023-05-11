#!/usr/bin/python3
import sys
if __name__ == "__main__":
    arglen = len(sys.argv)
    sum = 0
    for count in range(1, arglen):
        sum += int(sys.argv[count])
    print(sum)
