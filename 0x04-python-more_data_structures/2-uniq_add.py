#!/usr/bin/python3
def uniq_add(my_list=[]):
    g = sorted(my_list)
    sum1 = 0
    for n in range(len(g)):
        if g[n] != g[n - 1]:
            sum1 += g[n]
    return sum1
