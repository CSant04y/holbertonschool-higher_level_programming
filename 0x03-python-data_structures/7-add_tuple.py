#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) == 0:
        tup = (0, 0)
    elif len(tuple_a) == 1:
        tup = (tuple_a[0], 0)
    elif len(tuple_a) >= 2:
        tup = (tuple_a[0], tuple_a[1])

    if len(tuple_b) == 0:
        tup2 = (0, 0)
    elif len(tuple_b) == 1:
        tup2 = (tuple_b[0], 0)
    elif len(tuple_b) >= 2:
        tup2 = (tuple_b[0], tuple_b[1])
    return (tup[0] + tup2[0], tup[1] + tup2[1])
