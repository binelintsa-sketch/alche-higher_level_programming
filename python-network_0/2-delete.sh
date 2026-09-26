#!/bin/bash
# Sends a DELETE request to a URL passed as argument and displays the body of the response
curl -sX DELETE "$1"
