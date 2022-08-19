#!/usr/bin/python3
'''Script Python qui envoie une requête à l'URL'''
import sys
import urllib.request


if __name__ == "__main__":
    try:
        with urllib.request.urlopen(sys.argv[1]) as response:
            print(response.read().decode('utf-8'))
    except urllib.error.HTTPError as err:
        print('Error code:', err.code)
