#!/usr/bin/python3
'''Script Python qui envoie une requête à l'URL'''
import sys
import requests


if __name__ == "__main__":
    letter = sys.argv[1] if len(sys.argv) > 1 else ""
    data = {'q': letter}

    res = requests.post("http://0.0.0.0:5000/search_user", data=data)

    try:
        responseJson = res.json()
        name = responseJson.get("name")
        id = responseJson.get("id")
        if id is None or name is None:
            print("No result")
        else:
            print("[{}] {}".format(id, name))
    except Exception:
        print("Not a valid JSON")
