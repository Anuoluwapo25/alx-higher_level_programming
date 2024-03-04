#!/usr/bin/python3
"""Get commit using git API"""

import requests
import sys
if __name__ == "__main__":
    r = requests.get('https://api.github.com/repos/{}/{}/commits'.format(
        sys.argv[2], sys.argv[1]))
    result = r.json()
    try:
        for i in range(10):
            print("{}: {}".format(
                  result[i].get("sha"),
                  result[i].get("commit").get("author").get("name")))
    except IndexError:
        pass
