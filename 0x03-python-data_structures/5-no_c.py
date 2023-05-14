#!/usr/bin/python3
def no_c(my_string):
    new_string = ""
    for idx, char in enumerate(my_string):
        if char == 'c' or char == 'C':
            new_string += ""    
        else:
            new_string += char
    return my_string
