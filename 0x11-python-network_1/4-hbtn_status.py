#!/usr/bin/python3

"""
Python script that fetches https://alx-intranet.hbtn.io/status
"""

import requests

if __name__ == "__main__":
    url = "https://intranet.hbtn.io/status"
    httpResp = requests.get(url)
    print("Body response:")
    print("\t- type: {}".format(type(httpResp.text)))
    print("\t- content: {}".format(httpResp.text))


