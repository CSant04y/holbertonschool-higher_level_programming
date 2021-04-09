#!/usr/bin/python3
"""[This script fetches this URL https://intranet.hbtn.io/status
    using the urllib module]
"""

if __name__ == "__main__":
    import urllib.request
    import urllib.parse

    with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
        content = response.read()
        print("Body response:")
        print('\t- type: {}'.format(type(content)))
        print('\t- content: {}'.format(str(content)))
        new_var = content.decode('UTF-8')
        print('\t- utf8 content: {}'.format(new_var))
