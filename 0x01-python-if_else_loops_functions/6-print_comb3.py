#!/usr/bin/python3
for n in range(0, 100):
    if n == 99:
        print(n)
    elif(str(n)[::-1] >= str(n)):
        print("{:0>2}".format(n), end=', ')
