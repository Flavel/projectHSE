#!/usr/bin/env python3
import cgi
import pymysql
import connect
import setdefault
import os
import cgitb; cgitb.enable()

print("Content-type: text/html")
print()
if setdefault.check() == False :
    redirectURL = "/cgi-bin/login.py"
    print('<html><head><meta http-equiv="refresh" content="0;url='+str(redirectURL)+'" /></head></html>')
else :
    con = connect.con
    cur = connect.cur

    form = cgi.FieldStorage()
    name = form.getfirst("name", None)
    description = form.getfirst("description", None)

    query = "INSERT INTO `teachers`(`name`, `description`) VALUES ('{0}','{1}')".format(name, description)
    cur.execute(query)
    con.commit()
    query = "SELECT * FROM `teachers` ORDER BY `id` DESC LIMIT 1"
    cur.execute(query)
    teacherid = cur.fetchall()[0][0]
    print("{0}".format(teacherid))

    image = form["img"]
    if image.file :
        open('tmp/' + str(teacherid) + ".png", 'wb').write(image.file.read())
    

    redirectURL = "/cgi-bin/page.py?id={0}".format(teacherid)
    print('<html><head><meta http-equiv="refresh" content="0;url='+str(redirectURL)+'" /></head></html>')