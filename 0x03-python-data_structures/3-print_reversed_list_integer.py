#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list:
        for count in range(len(my_list)):
            print("{:d}".format(my_list[len(my_list) - count - 1]))
