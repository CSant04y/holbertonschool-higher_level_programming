#!/usr/bin/python3
"""[Python script that takes in GitHub credentials
    (username and password) and uses the GitHub API
    to display your id]
"""
if __name__ == "__main__":
    import requests
    from requests.auth import HTTPBasicAuth
    from sys import argv

    token = argv[2]
    user = argv[1]
    params = {'state': 'open'}
    url = 'https://api.github.com/user'

    response = requests.get(
                            url, auth=HTTPBasicAuth(
                                                user, token), params=params)
    json_string = response.json()
    print(json_string.get('id'))
