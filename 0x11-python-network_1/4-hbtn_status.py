#!/usr/bin/python3
"""script that fetches hbtn status page"""
import requests


if __name__ == "__main__":
    html = requests.get('https://alx-intranet.hbtn.io/status').text
    print("Body response:")
    print(f'\t- type: {type(html)}')
    print(f'\t- content: {html}')
