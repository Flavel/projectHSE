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
form = cgi.FieldStorage()
login = form.getfirst("login", None)
password = form.getfirst("password", None)
confirm = form.getfirst("confirm", None)
if login != None :
    cur.execute("SELECT * FROM users WHERE `login` = '{0}'".format(login))
    rows = cur.fetchall()
    if len(rows) == 1 :
        content += "<p>Пользователь с таким логином уже существует</p>"
        login = None
if not password == None and not password == confirm :
    content += "<p>Пароли не совпадают</p>"
    password = None
if login == None or password == None :
    content += """
        <form action="/cgi-bin/register.py" method=POST>
            <p>Логин</p>
            <input type="text" name = "login" value = "{0}"><br>
            <p>Пароль</p>
            <input type="password" name = "password"><br>
            <p>Повторить пароль</p>
            <input type="password" name = "confirm"><br>
            <input type="submit">
        </form>
    </body>
</html>""".format(login if not login == None else "")
else :
    query = "INSERT INTO `users`(`login`, `password`) VALUES ('{0}', '{1}')".format(login, password)
    cur.execute(query)
    con.commit()
    content += "Регистрация прошла успешно, перейдите <a href = \"/cgi-bin/login.py\">сюда</a> чтобы войти."
default = default.replace("_content_", content)
default = default.replace("_namepage_", "Регистрация")
print(default)
    
        