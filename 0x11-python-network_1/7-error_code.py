#!/usr/bin/python3
"""
request to given URL and display body of r, decoded
also handles error is HTTP status code is >= 400
"""
if __name__ == "__main__":
    import requests
    from sys import argv

    r = requests.get(argv[1])
    status = r.status_code
    if status >= 400:
        print("Error code: {}".format(status))
    else:
        print(r.text)
