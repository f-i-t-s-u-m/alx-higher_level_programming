#!/usr/bin/python3
""" ERror code """


import requests
from sys import argv

if __name__ == '__main__':

    req = requests.get('http://0.0.0.0:5000/search_user', {'q': argv[1]})
    if req.text == {}:
        print('No result')
    else:
        print('[{}] {}'.format(req.text.get('id'), req.text.get('name')))
