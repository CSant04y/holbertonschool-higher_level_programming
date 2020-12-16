#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if not my_list:
        return None
    tmp = list(my_list)
    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            tmp[i] = True
        else:
            tmp[i] = False
    return tmp
