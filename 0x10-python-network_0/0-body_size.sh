#!/bin/bash
# takes in a URL, sends request to URL, displays the size of body of response
curl -sI "$1" | grep Content-Length | cut -d ' ' -f2
