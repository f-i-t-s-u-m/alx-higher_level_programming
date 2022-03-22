#!/usr/bin/python3
""" search api """



if __name__ == '__main__':
    import requests
    from sys import argv

    q = argv[1] if len(argv) > 1 else ""
    req = requests.post('http://0.0.0.0:5000/search_user', params={'q': q})
    j = req.json()
    try:
        if len(j) == 0:
            print('No result')
        else:
            print('[{}] {}'.format(j.get('id'), j.get('name')))
    except ValueError:
        print('Not a valid JSON')
