#!/usr/bin/python3
"""[takes in a URL and an email, sends a POST request to the passed URL with the email as a parameter,
    and displays the body of the response (decoded in utf-8)]
"""

if __name__ == "__main__":
    import urllib.request
    import urllib.parse
    from sys import argv

    data = {}
    data['email'] = argv[2]
    data2 = urllib.parse.urlencode(data)
    data = data2.encode('UTF-8')
    req = urllib.request.Request(argv[0], data)
    with urllib.request.urlopen(req) as response:
        content = response.read()
        print(content.decode('UTF-8'))