#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniqe = set(my_list)
    sum = 0
    for num in uniqe:
        sum += num
    return sum
