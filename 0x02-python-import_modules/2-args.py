#!/usr/bin/python3
import sys
if __name__ == "__main__":
    arrlen = len(sys.argv)
    if arrlen == 1:
        print("{:d} argument".format(arrlen))
    else:
        print("{:d} arguments".format(arrlen))
    for count in range(1, arrlen):
        print("{:d}: {:s}".format(count, sys.argv[count]))
