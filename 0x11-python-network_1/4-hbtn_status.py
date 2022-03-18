#!/usr/bin/python3
""" check status """

if __name__ == "__main__":
    from urllib import request

    with request.urlopen('https://alx-intranet.hbtn.io/status') as resp:
        data = resp.read().decode('UTF8')

    print("Body response:")
    print('\t- type: {}'.format(type(data)))
    print('\t- content: {}'.format(data))
