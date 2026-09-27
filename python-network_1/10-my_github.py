#!/usr/bin/python3
"""
Uses the GitHub API and HTTP Basic Authentication to retrieve
and display the user ID of a given GitHub account.
"""
import requests
import sys


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    url = "https://api.github.com/user"

    response = requests.get(url, auth=(username, password))
    json_data = response.json()

    print(json_data.get('id'))
