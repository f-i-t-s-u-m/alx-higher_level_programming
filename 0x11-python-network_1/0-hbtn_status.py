#!/usr/bin/python3
from urllib import request

""" get status code """


with request.urlopen('https://alx-intranet.hbtn.io/status') as resp:
    data = resp.read()

print("Body response:")
print("    - type: {}".format(type(data)))
print("    - content: {}".format(data))
print("    - utf8: {}".format(data.decode('UTF8')))
