#!/usr/bin/python3

"""
Python script that fetches https://alx-intranet.hbtn.io/status
"""

import request

if __name__ == "__main__":
    url = "https://intranet.hbtn.io/status"
    httpResponse = requests.get(url)
    print("Body response:")
    print("\t- type: {}".format(type(httpResponse.text)))
    print("\t- content: {}".format(httpResponse.text))


