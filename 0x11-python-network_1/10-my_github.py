#!/usr/bin/python3
"""
takes your Github credentials (username and password) and uses
the Github API to display your id
"""
from requests.auth import HTTPBasicAuth
import requests
import sys

if __name__ == '__main__':
    user = HTTPBasicAuth(sys.argv[1], sys.argv[2])

    result = requests.get('https://api.github.com/user', auth=user)
    print(result.json().get('id'))
