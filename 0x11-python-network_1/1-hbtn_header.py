#!/usr/bin/python3
"""[ that takes in a URL, sends a request to the URL and displays the value
    of the X-Request-Id variable found in the header of the response.]
"""

if __name__ == "__main__":
    import urllib.request
    import urllib.parse
    import sys

    with urllib.request.urlopen(sys.argv[1]) as response:
        header = response.info()
        print("{}".format(header.get("X-Request-Id")))
