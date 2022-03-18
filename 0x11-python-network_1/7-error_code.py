#!/usr/bin/python3
""" ERror code """


import requests
from sys import argv

if __name__ == '__main__':
    req = requests.get(argv[1])
    if req.status_code == 200:
        print(req.text)
    else:
        print('Error code: {}'.format(req.status_code))
