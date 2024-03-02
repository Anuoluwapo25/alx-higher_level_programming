#!/usr/bin/python3
"""
given the URL and email, send POST request to URL
"""
import requests
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    email = {"email": argv[1]}
    response = requests.post(url, data=email)
    print(response.text)
