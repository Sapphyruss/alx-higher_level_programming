#!/usr/bin/python3
"""
Send a POST request with email parameter
"""


if __name__ == '__main__':
    import requests
    from sys import argv

    r = requests.post(argv[1], data={'email': argv[2]})
    print(r.text)
