#!/usr/bin/env python3
import cgi
import pymysql
import connect
import setdefault
import cgitb; cgitb.enable()
print("Content-type: text/html")
print()
if setdefault.check() == False :
    redirectURL = "/cgi-bin/login.py"
    print('<html><head><meta http-equiv="refresh" content="0;url='+str(redirectURL)+'" /></head></html>')
else :
    form = cgi.FieldStorage()
    knowledge       = form.getfirst("knowledge",        "Null")
    skill           = form.getfirst("skill",            "Null")
    communication   = form.getfirst("communication",    "Null")
    free            = form.getfirst("free",             "Null")
    assessment      = form.getfirst("assessment",       "Null")
    teacherid       = form.getfirst("id",               "Null")
    con = connect.con
    cur = connect.cur
    userid = setdefault.getuserid()
    query = "SELECT * FROM `assessments` WHERE `userid` = {0} AND `teacherid` = {1}".format(userid, teacherid)
    cur.execute(query)
    rows = cur.fetchall()
    if len(rows) >= 1:
        query = """UPDATE `assessments` SET `knowledge`={0},`skill`={1},`communication`={2},`free`={3},
                    `assessment`={4} WHERE `userid`={5} AND `teacherid`={6}""".format(knowledge, skill, communication,
                                                                                      free, assessment, userid, teacherid)
        cur.execute(query)
        con.commit()
    else :
        query = """INSERT INTO `assessments`(`userid`, `teacherid`, `knowledge`, `skill`, `communication`, 
                `free`, `assessment`) VALUES ({0}, {1}, {2}, {3}, {4}, {5}, {6})""".format(userid, teacherid, knowledge, skill, 
                                                                                            communication, free, assessment)
        print(query)
        cur.execute(query)
        con.commit()
    redirectURL = "/cgi-bin/page.py?id={0}".format(teacherid)
    print('<html><head><meta http-equiv="refresh" content="0;url='+str(redirectURL)+'" /></head></html>')
