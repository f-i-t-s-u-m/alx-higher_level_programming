#!/usr/bin/python3
from urllib import request
from sys import argv
""" get x data """

if __name__ == '__main__':
    with request.urlopen(argv[1]) as resp:
        for i in resp.getheaders():
            if i[0] == 'X-Request-Id':
                print(i[1])
