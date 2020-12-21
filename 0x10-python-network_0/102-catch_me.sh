#!/bin/bash
# makes request 0.0.0.0:5000/catch_me causes server to respond with message, in body of response
curl -sLX PUT 0.0.0.0:5000/catch_me -H "Origin: HolbertonSchool" -d "user_id=98"
