#!/usr/bin/python3
"""
Sends a request to URL and display the value
"""

from sys import argv
import urllib.request

if __name__ == '__main__':
    url = argv[1]
    httpRequest = urllib.request.Request(url)
    with urllib.request.urlopen(httpRequest) as response:
        htmlBody = response.getheader('X-Request-Id')
        print(htmlBody)
