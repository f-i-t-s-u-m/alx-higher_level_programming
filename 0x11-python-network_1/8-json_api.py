#!/usr/bin/python3
""" search api """


import requests
from sys import argv


if __name__ == '__main__':
    q = argv[1] if len(argv) > 1 else ""
    req = requests.post('http://0.0.0.0:5000/search_user', params={'q': q})
    j = req.json()
    try:
        if not len(j) == 0:
            print('[{}] {}'.format(j.get('id'), j.get('name')))
        else:
            print('No result')
    except ValueError:
        print('Not a valid JSON')
