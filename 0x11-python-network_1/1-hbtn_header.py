#!/usr/bin/python3
'''Script Python qui prend une URL, envoie une requête à l'URL'''
import urllib.request
import sys


if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as response:
        print(response.info().get('X-Request-Id'))
