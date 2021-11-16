#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
def get_last():
    if number < 0 and number % 10 != 0:
        return number %  - 10
    return number % 10
def comval():
    if get_last() < 6 and get_last() != 0:
        return 'and is less than 6 and not 0'
    elif get_last() < 6 and get_last() == 0:
        return 'and is 0'
    elif get_last() > 5:
        return 'and is greater than 5'
print("Last digit of {} is {} {}".format(number, get_last(), comval()))
