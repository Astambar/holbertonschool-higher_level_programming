#!/usr/bin/python3
""" This function have a save_to_json_file """
from sys import argv

save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file
filename = 'add_item.json'

try:
    a = load_from_json_file(filename)
except load_from_json_file(filename).DoesNotExist:
    a = []
finally:
    a.extend(argv[1:])
    save_to_json_file(a, filename)
