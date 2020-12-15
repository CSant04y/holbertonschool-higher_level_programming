#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if not my_list:
        return None

    a = my_list[:]
    if idx > len(my_list):
        return a
    a[idx] = element
    return a
