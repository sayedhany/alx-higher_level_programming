#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dic = dict(a_dictionary.items())
    for num in new_dic.keys():
        new_dic[num] *= 2
    return new_dic
