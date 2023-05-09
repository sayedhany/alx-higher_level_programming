#!/usr/bin/python3
def uppercase(str):
    for char in str:
        if ord(char) >= 97 and ord(char) <= 122:
            new = ord(char) - 32
            res = chr(new)
        else:
            res = char
        print("{}".format(res), end="")
    print()
