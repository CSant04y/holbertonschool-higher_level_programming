#!/usr/bin/python3
"""[Finds the peak in an unsorted list]
"""


def find_peak(list_of_integers):
    """[Finds the peak in alist of numbers]
    """
    low = 0
    high = len(list_of_integers) - 1

    if list_of_integers is None or len(list_of_integers) < 2:
        return list_of_integers

    while low < high:
        mid = low + (high - low + 1) // 2
        if (mid-1 >= 0 and list_of_integers[mid-1] <= list_of_integers[mid]):
            low = mid
        else:
            high = mid - 1
    return list_of_integers[low + 1]
