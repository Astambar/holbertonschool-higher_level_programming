#!/usr/bin/python3
'''Script Python qui envoie une requête à l'URL'''
import sys
import requests


if __name__ == "__main__":
    res = requests.get(sys.argv[1])
    print(res.headers.get('X-Request-Id'))
