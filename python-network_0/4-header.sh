#!/bin/bash
# Sends a GET request to a URL with a custom header and displays the body of the response
curl -sH "X-HolbertonSchool-User-Id: 98" "$1"
