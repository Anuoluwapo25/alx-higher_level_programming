#!/usr/bin/python3
"""
using Github API get id of user
"""
import requests
from sys import argv

if __name__ == "__main__":
    url = "https://api.github.com/user"
    headers = {
    "Authorization": f"Basic {username}:{personal_access_token}",
    }

    response = requests.get(url, headers=headers)
    user_id = response.json().get('id')
    print('user_id')
