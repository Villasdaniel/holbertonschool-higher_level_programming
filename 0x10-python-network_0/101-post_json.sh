#!/bin/bash
# sends JSON POST request to URL passed as first argument, displays body of response
curl -sX POST -H "Content-Type: application/json" -d @"$2" "$1"
