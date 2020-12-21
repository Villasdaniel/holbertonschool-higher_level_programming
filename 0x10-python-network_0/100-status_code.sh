#!/bin/bash
# sends a request to URL passed as argument, displays only the status code of response
curl -so /dev/null -w "%{http_code}" "$1"