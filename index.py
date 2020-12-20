#!/usr/bin/env python3
import cgi
import pymysql
import connect
import setdefault
import cgitb; cgitb.enable()

con = connect.con
cur = connect.cur

default = setdefault.init()
content = ""

content += """
    <div style="display : inline-block; width :20%;">
        <p>Самые умные</p>
"""
#Расчет самых умных
query = "SELECT * FROM `assessments` WHERE `knowledge` ORDER BY `teacherid`"
cur.execute(query)
rows = cur.fetchall()
rating = {}
count = 0
teacherid = None
for row in rows :
    if teacherid == row[2] :
        rating[teacherid] += row[3] 
        count += 1
    else :
        if rating.get(teacherid) :
            rating[teacherid] /= count
        teacherid = row[2]
        rating[teacherid] = row[3]
        count = 1
rating[teacherid] /= count
list_keys = list(rating.keys())
list_keys.sort()
for i in list_keys[::-1]:
    query = "SELECT * FROM `teachers` WHERE `id` = {0}".format(i)
    cur.execute(query)
    content += "<div> <a href = 'page.py?id={0}'>{1}</a> {2}</div> ".format(i, cur.fetchall()[0][1], rating[i])
content += "</div>"

content += """
    <div style="display : inline-block; width :20%;">
        <p>Лучше всего преподают</p>
"""
#Расчет тех кто лучше всего преподает
content += "</div>"

content += """
    <div style="display : inline-block; width :20%;"> 
        <p>Лучше всего в общении</p>
"""
#Расчет тех кто лучше всего в общении
content += "</div>"

content += """
    <div style="display : inline-block; width :20%;">
        <p>Самые халявные</p>
"""
#Расчет самых халявных
content += "</div>"

content += """
    <div style="display : inline-block; width :20%;">
        <p>Самые строгие</p>
"""
#Расчет самых строгих(обратная сторона халявных)
content += "</div>"

content += """
    <div style="display : inline-block; width :20%;">
        <p align="center">Самые самые</p>
"""
#Расчет самых самых
content += "</div>"

print("Content-type: text/html")
print()

default = default.replace("_content_", content)
default = default.replace("_namepage_", "Главная")

print(default)