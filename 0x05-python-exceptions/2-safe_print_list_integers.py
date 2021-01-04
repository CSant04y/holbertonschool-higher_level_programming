#!/usr/bin/pyhton3
def safe_print_list_integers(my_list=[], x=0):
    num = 0
    try:
        for itr in range(0, x):
            if type(my_list[itr]) is not int:
                continue
            print("{:d}".format(my_list[itr]), end='')
            num += 1
        print()
        return num
    except:
        raise
        print("IndexError: list index out of range")
        return num
