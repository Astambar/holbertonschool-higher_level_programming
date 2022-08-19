#!/usr/bin/python3
'''récupère https://intranet.hbtn.io/status'''
import requests


html = requests.get('https://intranet.hbtn.io/status').text

print("Body response:")
print('\t- type:', type(html))
print('\t- content:', html)
