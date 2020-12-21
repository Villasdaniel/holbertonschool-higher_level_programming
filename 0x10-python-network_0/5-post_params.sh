#!/bin/bash
# takes in URL, sends POST request to passed URL, and displays body of response
curl -s --data "email=hr@holbertonschool.com&subject=I will always be here for PLD" "$1"
