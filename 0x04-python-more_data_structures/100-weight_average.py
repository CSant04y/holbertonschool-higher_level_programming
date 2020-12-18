#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    mul_sum = 0
    denom = 0
    numerators = [num[0] * num[1] for num in my_list]

    b = [num[1] for num in my_list]

    for i in range(len(numerators)):
        mul_sum += numerators[i]

    for j in range(len(b)):
        denom += b[j]

    return mul_sum / denom
