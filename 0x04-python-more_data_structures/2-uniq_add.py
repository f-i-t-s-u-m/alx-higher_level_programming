#!/usr/bin/python3
def uniq_add(my_list=[]):
    sum1 = 0
    for n in set(my_list):
            sum1 += n
    return sum1
