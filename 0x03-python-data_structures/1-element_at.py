#!/usr/bin/python3
def element_at(my_list, idx):
    for index, element in enumerate(my_list):
        if idx < 0 or idx > len(my_list):
            return None
        else:
            if idx == index:
                return my_list[index]
