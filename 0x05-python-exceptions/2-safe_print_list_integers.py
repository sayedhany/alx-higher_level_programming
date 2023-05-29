#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    try:
        for num in my_list:
            if (isinstance(num, int) and count < x):
                print("{:d}".format(num), end="")
                count += 1
    except (TypeError, ValueError):
        pass
    finally:
        print()
        return count
