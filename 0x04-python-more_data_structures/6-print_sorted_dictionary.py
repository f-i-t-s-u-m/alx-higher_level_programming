#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    getsort = sorted(a_dictionary)
    for n in getsort:
        print("{}: {}".format(n, a_dictionary[n]))
