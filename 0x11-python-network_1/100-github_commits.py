#!/usr/bin/python3
"""takes 2 arguments in order to solve this challenge"""

import requests
import sys

if __name__ == '__main__':
    if len(sys.argv) < 3:
        sys.exit()
    res = requests.get('https://api.github.com/repos/{}/{}/commits'
                       .format(sys.argv[2], sys.argv[1]))
    dato = res.json()

    try:
        for i in range(10):
            print('{}: {}'.format(
                dato[i].get("sha"),
                dato[i].get("commit").get("author").get("name")))
    except:
        pass
