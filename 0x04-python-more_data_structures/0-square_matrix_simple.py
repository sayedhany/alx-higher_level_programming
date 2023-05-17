#!/usr/bin/python3
def cal_square(list1=[]):
    new_list = []
    for num in list1:
        new_list.append(num * num)
    return new_list


def square_matrix_simple(matrix=[]):
    res = list(map(cal_square, matrix))
    return res
