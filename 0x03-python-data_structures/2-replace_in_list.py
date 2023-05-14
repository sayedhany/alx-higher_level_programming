#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    new_list = my_list[:]
    if idx < 0 or idx > len(my_list):
        return my_list
    else:
        for index in range(len(my_list)):
            if idx == index:
                new_list[idx] == element
                return new_list
