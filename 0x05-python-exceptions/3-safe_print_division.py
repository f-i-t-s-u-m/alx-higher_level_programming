#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        print("{} / {} = {}".format(a, b, a/b))
        r = a/b
    except ZeroDivisionError:
        r = 'None'
    finally:
        return r
