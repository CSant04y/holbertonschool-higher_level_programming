#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    a_dict = a_dictionary.copy()
    for j in sorted(a_dict):
        print("{}: {}".format(j, a_dict[j]))
