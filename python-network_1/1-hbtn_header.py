#!/usr/bin/python3
"""
Fetches a URL passed as an argument and displays the value
of the X-Request-Id header variable in the response.
"""
import sys
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:
        print(dict(response.headers).get("X-Request-Id"))
