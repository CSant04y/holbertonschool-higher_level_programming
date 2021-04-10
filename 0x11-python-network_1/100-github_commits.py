#!/usr/bin/python3
"""[list 10 commits (from the most recent to oldest)
    of the repository “rails” by the user “rails”]
"""


if __name__ == "__main__":
    import requests
    from sys import argv

    repo = argv[1]
    user = argv[2]

    params = {'page': '1', 'per_page': '10'}
    url = ('https://api.github.com/repos/{}/{}/commits'.
           format(user, repo))

    response = requests.get(url, params=params)

    json_string = response.json()

    for commit in json_string:
        commit_id = commit.get('sha')
        authors = commit.get('commit').get('author').get('name')
        print('{}: {}'.format(commit_id, authors))
