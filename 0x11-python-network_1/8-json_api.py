#!/usr/bin/python3
""" search api """


import requests
from sys import argv


def main(query= ""):
    params = {'q': query}
    req = requests.post('http://0.0.0.0:5000/search_user', params)
    try:
        if req.json() is not None:
            print('[{}] {}'.format(req().get('id'), req().get('name')))
        else:
            print('No result')
    except ValueError:
        print('Not a valid JSON')


if __name__ == '__main__':
    if len(argv) > 1:
        main(argv[1])
    else:
        main()

