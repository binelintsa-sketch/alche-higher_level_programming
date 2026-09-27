#!/usr/bin/python3
"""
Takes in a URL, sends an HTTP request, and displays the value
of the X-Request-Id header found in the response.
"""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    response = requests.get(url)
    print(response.headers.get("X-Request-Id"))
