#!/usr/bin/python3
for n in range (0, 100):
    print("0{}, ".format(n)  if n < 10 else "{}, ".format(n) if n < 99 else "{}".format(n), end='')
print()
