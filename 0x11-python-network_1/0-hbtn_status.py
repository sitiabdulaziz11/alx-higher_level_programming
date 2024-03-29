#!/usr/bin/python3
"""
A Python script that fetches https://alx-intranet.hbtn.io/status.
"""

import urllib.request


if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"

    with urllib.request.urlopen(url) as respo:
        html_cont = respo.read()
        deco_cont = html_cont.decode('utf-8')

    print("Body response:")
    print("\t- type: {}".format(type(html_cont)))
    print("\t- content: {}".format(html_cont))
    print("\t- utf8 content: {}".format(deco_cont))
