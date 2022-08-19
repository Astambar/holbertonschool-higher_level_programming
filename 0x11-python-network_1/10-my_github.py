#!/usr/bin/python3
'''Script Python qui envoie une requête à l'URL'''
import sys
import requests


if __name__ == "__main__":
    res = requests.get(
        'https://api.github.com/user',
        auth=(sys.argv[1], sys.argv[2])
    )
    print(res.json().get("id"))
