#!/bin/bash
# takes in URL as argument, sends GET request to the URL, displays the body of response
curl -sX GET -H "X-HolbertonSchool-User-Id: 98" "$1"
