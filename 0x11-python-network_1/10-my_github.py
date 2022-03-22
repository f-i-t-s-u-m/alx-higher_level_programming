#!/usr/bin/python3
""" fetch github user data """

if __name__ == "__main__":
    import requests
    import sys

    r = requests.get("https://api.github.com/user",
                     auth=(sys.argv[1], sys.argv[2])).json()
    print(r.get('id'))
