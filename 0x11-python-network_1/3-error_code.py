#!/usr/bin/python3
"""[takes in a URL, sends a request to the URL and displays
    the body of the response (decoded in utf-8]
"""

if __name__ == "__main__":
    import urllib.request
    import urllib.error
    import urllib.parse
    from sys import argv

    try:
        with urllib.request.urlopen(argv[1]) as response:
            content = response.read()
            print(content.decode('UTF-8'))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
