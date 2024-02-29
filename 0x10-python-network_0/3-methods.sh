#!/bin/bash
# send request to URL and display all HTTP methods server will accept
curl -sI -X OPTIONS "$1" | grep -i Allow | cut -f2- -d':' | sed 's/^[[:space:]]*//' | sed 's/[[:space:]]*$//'
