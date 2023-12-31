#!/usr/bin/python3
"""
a Python script that takes in a letter
and sends a POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter.
"""
import requests
import sys


try:
    q = sys.argv[1]
except IndexError:
    q = ""

if len(q) == 0:
    print("No result")
else:
    r = requests.post("http://0.0.0.0:5000/search_user", data={"q": q})
    try:
        body = eval(r.text)
        print("[{}] {}".format(body["id"], body["name"]))
    except (SyntaxError, NameError):
        print("Not a valid JSON")
