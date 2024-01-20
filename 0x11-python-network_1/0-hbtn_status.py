#!/usr/bin/python3
"""
A Python script that fetches https://alx-intranet.hbtn.io/status.
"""

from urllib.request import Request, urlopen

if __name__ == "__main__":
    url = Request('https://alx-intranet.hbtn.io/status')

    with urlopen(url) as respo:
        html_cont = respo.read()
        deco_cont = html_cont.decode('utf-8')

    print("Body response:")
    print("\t- type: {_type}".format(_type=type(html_cont)))
    print("\t- content: {_content}".format(_content=html_cont))
    print("\t- utf8 content: {_utf8_c}".format(_utf8_c=deco_cont))
