#!/usr/bin/python3
"""
a Python script that takes in a URL and an email address,
sends a POST request to the passed URL with the email as a parameter,
and finally displays the body of the response.
"""
import requests
import sys

url = sys.argv[1]
e = sys.argv[2]

r = requests.post("{}".format(url), data={"email": e})

print(r.text)
