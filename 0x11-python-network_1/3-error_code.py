#!/usr/bin/python3
"""error code"""


from urllib import request, error
from sys import argv


if __name__ == '__main__':
    try:
        with request.urlopen(argv[1]) as req:
            print(req.read().decode('UTF8'))
    except error.URLError as e:
        print('Error code: {}'.format(e.code))
