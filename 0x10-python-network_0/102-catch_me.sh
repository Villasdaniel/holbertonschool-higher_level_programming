#!/bin/bash
# makes request 0.0.0.0:5000/catch_me causes server to respond with message, in body of response
curl -s -H --data @catch_me 0.0.0.0:5000/catch_me
