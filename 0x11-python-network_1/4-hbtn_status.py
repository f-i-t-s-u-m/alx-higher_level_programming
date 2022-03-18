#!/usr/bin/python3
""" check status """
from urllib import request

if __name__ == "__main__":
    with request.urlopen('https://alx-intranet.hbtn.io/status') as resp:
        data = resp.read().decode('UTF8')

    print("Body response:")
    print('\t- type: {}'.format(type(data)))
    print('\t- content: {}'.format(data))
