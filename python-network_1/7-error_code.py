#!/usr/bin/python3
"""
Sends a request to a given URL and displays the body of the response.
Prints "Error code: " followed by the HTTP status code if status_code >= 400.
"""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    response = requests.get(url)

    if response.status_code >= 400:
        print("Error code: {}".format(response.status_code))
    else:
        print(response.text)
