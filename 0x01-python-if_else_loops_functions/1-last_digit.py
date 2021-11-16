#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0 and number % 10 != 0:
    remainder = number %  - 10
else:  remainder = number % 10
if remainder < 6 and remainder != 0:
     _string = 'and is less than 6 and not 0'
elif remainder < 6 and remainder == 0:
      _string = 'and is 0'
else:
     _string = 'and is greater than 5'
print("Last digit of {} is {} {}".format(number, remainder, _string))
