#!/usr/bin/python3
"""
Python script takes in a URL and an email
"""

import urllib.request
import urllib.parse
from sys import argv

if __name__ == '__main__':
    url = argv[1]
    values = {'email': argv[2]}
    data = urllib.parse.urlencode(values)
    data = data.encode('ascii')
    httpRequest = urllib.request.Request(url, data)

    with urllib.request.urlopen(httpRequest) as response:
        htmlBody = response.read()
        print(htmlBody.decode('utf-8'))
