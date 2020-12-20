#!/usr/bin/env python3
import cgi
import pymysql
import connect
import setdefault
import os
import cgitb; cgitb.enable()
import http.cookies

print("Content-type: text/html")
print()
if setdefault.check() == False :
    redirectURL = "/cgi-bin/login.py"
    print('<html><head><meta http-equiv="refresh" content="0;url='+str(redirectURL)+'" /></head></html>')
else :
    con = connect.con
    cur = connect.cur
    form = cgi.FieldStorage()
    teacherid = form.getfirst("id", None)
    comment = form.getfirst("comment", None)
    cookie = http.cookies.SimpleCookie(os.environ.get("HTTP_COOKIE"))
    login = cookie.get("login").value
    query = "INSERT INTO `comments`(`teacherid`, `login`, `comment`) VALUES ({0},'{1}','{2}')".format(teacherid, login, comment)
    cur.execute(query)
    con.commit()
    redirectURL = "/cgi-bin/page.py?id={0}".format(teacherid)
    print('<html><head><meta http-equiv="refresh" content="0;url='+str(redirectURL)+'" /></head></html>')