#!/usr/bin/python3
""" search api """


import requests
from sys import argv


def main(query= ""):
    params = {'q': query}
    req = requests.post('http://httpbin.org/anythin/search_user', params)
    if req.json is not None:
        print('[{}] {}'.format(req.get('id'), req.get('name')))
    else:
        print('No result')


if __name__ == '__main__':
    if len(argv) > 1:
        main(argv[1])
    else:
        main()

