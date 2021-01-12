#!/usr/bin/python3
"""
takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter
"""

import requests
import sys

if __name__ == '__main__':
    if len(sys.argv) > 1:
        val = {'q': sys.argv[1]}
    else:
        val = {'q': ''}

    try:
        r = requests.post('http://0.0.0.0:5000/search_user', data=val)
        data = r.json()

        if data:
            print('[{}] {}'.format(data.get('id'), data.get('name')))
        else:
            print('No result')
    except ValueError:
        print("Not a valid JSON")
