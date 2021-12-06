#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    n = 0
    try:
        for i in range(x):
            print("{:d}".format(my_list[i]), end="")
            n += 1
    except IndexError:
        print("", end="")
    print("")
    return n