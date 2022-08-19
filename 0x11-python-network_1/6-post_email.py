#!/usr/bin/python3
'''Script Python qui envoie une requête à l'URL'''
import sys
import requests


if __name__ == "__main__":
    data = {'email': sys.argv[2]}
    res = requests.post(sys.argv[1], data=data).text

    print(res)
