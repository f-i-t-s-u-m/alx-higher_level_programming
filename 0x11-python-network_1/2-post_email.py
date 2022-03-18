#!/usr/bin/python3
""" post email """

from urllib import request, parse
from sys import argv

if __name__ == '__main__':
    data = parse.urlencode({'email': argv[2]})
    data = data.encode('ascii')
    req = request.Request(argv[1], data)
    with request.urlopen(req) as resp:
        getres = resp.read()
    print(getres.decode('UTF8'))
