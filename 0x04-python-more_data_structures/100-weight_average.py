#!/usr/bin/python3
from functools import reduce
def weight_average(my_list=[]):
    if not my_list:
        return 0
    sum_products = reduce(lambda acc, tpl: acc + (tpl[0] * tpl[1]), my_list, 0)
    sum_weights = reduce(lambda acc, tql: acc + tql[1], my_list, 0)
    return sum_products / sum_weights
