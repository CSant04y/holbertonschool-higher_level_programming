#!/usr/bin/python3
def uniq_add(my_list=[]):
    my_set = set(my_list)
    sum = 0
    for itr in my_set:
        sum += itr
    return sum
