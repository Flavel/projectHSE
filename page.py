#!/usr/bin/env python3
import cgi
import pymysql
import connect
import setdefault
import cgitb; cgitb.enable()
con = connect.con
cur = connect.cur

form = cgi.FieldStorage()
teacherid = form.getfirst("id", None)

default = setdefault.init()
cur.execute("SELECT * FROM teachers WHERE `id` = {0}".format(teacherid))
rows = cur.fetchall()
if len(rows) != 0 :
    cur.execute("SELECT * FROM `assessments` WHERE `teacherid` = {0}".format(teacherid))
    assessments = cur.fetchall()
    knowledge       = 0
    skill           = 0
    communication   = 0
    free            = 0
    assessment      = 0
    knowledgecount       = 0
    skillcount           = 0
    communicationcount   = 0
    freecount            = 0
    assessmentcount      = 0
    for row in assessments :
        if row[3] != None :
            knowledge += row[3]
            knowledgecount += 1
        if row[4] != None :
            skill += row[4]
            skillcount += 1
        if row[5] != None :
            communication += row[5]
            communicationcount += 1
        if row[6] != None :
            free += row[6]
            freecount += 1
        if row[7] != None :
            assessment += row[6]
            assessmentcount += 1
    if knowledgecount != 0 :
        knowledge = knowledge / knowledgecount
    if skillcount != 0 :
        skill = skill / skillcount
    if communicationcount != 0 :
        communication = communication / communicationcount
    if freecount != 0 :
        free = free / freecount
    if assessmentcount != 0 :
        assessment = assessment / assessmentcount
    

    teacherinfo = rows[0]
    content = """
    <div style = "display: inline-block;vertical-align: top;width: 55%;">
    <H2>
    {0}
    </H2>
    <p>
    {1}
    </p>
    <h3>Комментарии</h3>
    _comments_
    </div><div style = "display: inline-block;vertical-align: top;">
    <img src="/tmp/{2}.png" style="width: 70%;">
    <form action="setassessment.py?id={2}" method=POST>
    <table>
    <tr><td>
    Знания \t               
    </td><td>
                            1 <input type="radio" name="knowledge" value=1> 
                            2 <input type="radio" name="knowledge" value=2> 
                            3 <input type="radio" name="knowledge" value=3> 
                            4 <input type="radio" name="knowledge" value=4> 
                            5 <input type="radio" name="knowledge" value=5> {3} ({8} голосов)
    </td>
    </tr><tr><td>
    Умение преподавать\t    
    </td><td>
                            1 <input type="radio" name="skill" value=1> 
                            2 <input type="radio" name="skill" value=2> 
                            3 <input type="radio" name="skill" value=3> 
                            4 <input type="radio" name="skill" value=4> 
                            5 <input type="radio" name="skill" value=5> {4} ({9} голосов)
    </td>
    </tr><tr><td>
    В общении \t 
    </td><td>           
                            1 <input type="radio" name="communication" value=1> 
                            2 <input type="radio" name="communication" value=2> 
                            3 <input type="radio" name="communication" value=3> 
                            4 <input type="radio" name="communication" value=4> 
                            5 <input type="radio" name="communication" value=5> {5} ({10} голосов)
    </td>
    </tr><tr><td>
    Халявность\t    
    </td><td>        
                            1 <input type="radio" name="free" value=1> 
                            2 <input type="radio" name="free" value=2> 
                            3 <input type="radio" name="free" value=3> 
                            4 <input type="radio" name="free" value=4> 
                            5 <input type="radio" name="free" value=5> {6} ({11} голосов)
    </td>
    </tr><tr><td>
    Общая оценка\t    
    </td><td>      
                            1 <input type="radio" name="assessment" value=1> 
                            2 <input type="radio" name="assessment" value=2> 
                            3 <input type="radio" name="assessment" value=3> 
                            4 <input type="radio" name="assessment" value=4> 
                            5 <input type="radio" name="assessment" value=5> {7} ({12} голосов)
    </td>
    </tr>
    </table>
    <input type = "submit" value = "Проголосовать">
    </form>
    </div>
    """.format(teacherinfo[1], teacherinfo[2], teacherid, knowledge, skill, communication, free, assessment, knowledgecount, skillcount, communicationcount, freecount, assessmentcount)
    if setdefault.check() == True :
        userid = setdefault.getuserid()
        for row in assessments :
            if row[1] == userid :
                if row[3] != None :
                    name = "knowledge" 
                    value = row[3]
                    content = content.replace("""<input type="radio" name="{0}" value={1}>""".format(name, value), """<input type="radio" name="{0}" value={1} checked>""".format(name, value))
                if row[4] != None :
                    name = "skill" 
                    value = row[4]
                    content = content.replace("""<input type="radio" name="{0}" value={1}>""".format(name, value), """<input type="radio" name="{0}" value={1} checked>""".format(name, value))
                if row[5] != None :
                    name = "communication" 
                    value = row[5]
                    content = content.replace("""<input type="radio" name="{0}" value={1}>""".format(name, value), """<input type="radio" name="{0}" value={1} checked>""".format(name, value))
                if row[6] != None :
                    name = "free" 
                    value = row[6]
                    content = content.replace("""<input type="radio" name="{0}" value={1}>""".format(name, value), """<input type="radio" name="{0}" value={1} checked>""".format(name, value))
                if row[7] != None :
                    name = "assessment" 
                    value = row[7]
                    content = content.replace("""<input type="radio" name="{0}" value={1}>""".format(name, value), """<input type="radio" name="{0}" value={1} checked>""".format(name, value))
    else :
        content = content.replace("""<input type = "submit" value = "Проголосовать">""", """<input type = "submit" value = "Проголосовать" disabled> Голосовать могут только авторизованные пользователи""")

    default = default.replace("_namepage_", teacherinfo[1])
else :
    default = default.replace("_namepage_", "Несуществующая страница")
    content = "<H1>Такой страницы не существует</H1><p>Как Вы вообще сюда попали?</p>"

#Комметнарии
comments = ""
if setdefault.check() == False :
    comments += "<p> Оставлять комментарии могут только авторизированные пользователи </p>"
else :
    comments += """
                <form action="addcomment.py?id={0}" method = POST>
                    <textarea style="width: 80%;" name = "comment"> </textarea><br>
                    <input type = "submit" value = "Отправить">
                </form>
    
                """.format(teacherid)

query = "SELECT * FROM `comments` WHERE `teacherid` = {0} ORDER BY `id` DESC".format(teacherid)
cur.execute(query)
commentsarray = cur.fetchall()
for comment in commentsarray:
    comments += """
        <div style="border-bottom:3px solid black;">
            <p>{0} : <b>{1}</b> </p>
            <p> {2} </p>
        </div>
    """.format(comment[3], comment[2], comment[4])

content = content.replace("_comments_", comments)
default = default.replace("_content_", content)

print("Content-type: text/html")
print()
print(default)