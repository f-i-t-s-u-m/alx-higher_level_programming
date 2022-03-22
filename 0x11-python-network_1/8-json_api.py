#!/usr/bin/python3
""" search api """


import requests
from sys import argv


def main(query= ""):
    params = {'q': query}
    req = requests.post('http://httpbin.org/anythin/search_user', params)
    if req.text is not None:
        print('[{}] {}'.format(req.text.id, req.text.name))
    else:
        print('No result')


if __name__ == '__main__':
    if len(argv) > 1:
        main(argv[1])
    else:
        main()

