#!/usr/bin/env python3
import cgi
import pymysql
import connect
import setdefault

con = connect.con
cur = connect.cur

default = setdefault.init()

content = ""
print("Content-type: text/html")
print()
print(default)