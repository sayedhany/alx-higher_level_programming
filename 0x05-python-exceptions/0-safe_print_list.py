#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0
    try:
        for ele in my_list:
            if count < x:
                print("{}".format(ele), end="")
                count += 1
    except IndexError:
        print("x biger than the length of list")
    finally:
        print()
        return count
