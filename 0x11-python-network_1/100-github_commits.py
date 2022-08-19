#!/usr/bin/python3
'''Script Python qui envoie une requête à l'URL'''
import requests
import sys


if __name__ == "__main__":
    res = requests.get(f'https://api.github.com/repos/{sys.argv[2]}/{sys.argv[1]}/commits')
    if res.status_code >= 400:
        print('None')
    else:
        for comment in res.json()[:10]:
            print(f"{comment.get('sha')}: {comment.get('commit').get('author').get('name')}")
