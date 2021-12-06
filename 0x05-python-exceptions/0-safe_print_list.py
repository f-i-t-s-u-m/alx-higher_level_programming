#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        for n in range(x):
            print("{}".format(my_list[n]), end="")
    except IndexError:
        print("", end="")
    print()
    return x
