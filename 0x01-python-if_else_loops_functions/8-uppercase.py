#!/bin/python3
def uppercase(str):
    for n in range(0, len(str)):
        if ord(str[n]) >= 97 and ord(str[n]) <= 122:
            print("{:c}".format(ord(str[n]) - 32), end='')
        else: print("{}".format(str[n]), end='')
