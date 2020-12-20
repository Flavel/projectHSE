#!/usr/bin/env python3
import cgi
import os
import http.cookies
import requests
login = "a"
password = "a"
print("Set-cookie:login={0}; expires=Wed May 17 03:33:20 2000; path=/cgi-bin/; httponly".format(login))
print("Set-cookie:password={0}; expires=Wed May 17 03:33:20 2000; path=/cgi-bin/; httponly".format(password))

redirectURL = "index.py"
print("Content-type: text/html")
print()
print('<html><head><meta http-equiv="refresh" content="0;url='+str(redirectURL)+'" /></head></html>')