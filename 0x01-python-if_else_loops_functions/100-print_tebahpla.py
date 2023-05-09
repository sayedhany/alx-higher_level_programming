#!/usr/bin/python3
for num in range(122, 96, -1):
    if num % 2 == 0:
        char = chr(num)
    else:
        char = chr(num-32)
    print("{}".format(char), end="")
