#!/usr/bin/python3
"""
Python script that takes in a URL and an email, sends a POST request to the 
passed URL with the email as a parameter, and displays the body of the
response (decoded in utf-8).
"""

from sys import argv
from urllib.request import Request, urlopen
from urllib.parse import urlencode

if __name__ == "__main__":
    url = argv[1]
    eml = argv[2]

    data = urlencode({'email': eml}).encode('utf-8')

    with urlopen(url, data) as res:
        bd = res.read().decode('utf-8')
        print("Response Body:", bd)
