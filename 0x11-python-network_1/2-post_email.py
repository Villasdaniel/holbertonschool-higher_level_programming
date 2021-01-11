#!/usr/bin/python3
"""
takes in a URL and an email, sends a POST request to the 
passed URL with the email as a parameter and displays the
body of the response (decoded in utf-8)
"""

if __name__ == "__main__":
    import sys
    from urllib import request, parse

    Mail = parse.urlencode({'email': sys.argv[2]})
    Mail = Mail.encode('utf-8')
    with request.urlopen(sys.argv[1], Mail) as response:
        Mail = response.read().decode('utf-8')
        print(Mail)
