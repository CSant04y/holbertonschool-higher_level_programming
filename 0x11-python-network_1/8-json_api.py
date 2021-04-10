#!/usr/bin/python3
"""[ takes in a letter and sends a POST request to
    http://0.0.0.0:5000/search_user with the letter as a parameter.]
"""

if __name__ == "__main__":
    from sys import argv
    import requests
    dic = {}
    if len(argv) >= 2:
        dic['q'] = argv[1]
    else:
        dic['q'] = ""
    response = requests.post('http://0.0.0.0:5000/search_user', data=dic)

    try:
        json_str = response.json()

        if json_str == {}:
            print('No result')
        else:
            print("[{}] {}".format(json_str['id'], json_str['name']))
    except Exception as err:
        print("Not a valid JSON")
