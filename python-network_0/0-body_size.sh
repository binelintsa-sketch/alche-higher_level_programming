#!/bin/bash
# Displays the size of the HTTP response body in bytes for a given URL
curl -sL "$1" | wc -c
