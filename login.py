#!/usr/bin/env python3
import cgi
import pymysql
import connect
import setdefault
con = connect.con
cur = connect.cur

default = setdefault.init()

content = ""
form = cgi.FieldStorage()
login = form.getfirst("login", None)
password = form.getfirst("password", None)
content += """
        <form action="/cgi-bin/login.py" method=POST>
            <p>Имя пользователя</p>
            <input type="text" name = "login" value = {0}>
            <p>Пароль</p>
            <input type="password" name = "password">
            <br>
            <input type="submit">
        </form>
    """.format(login if login != None else "")

if login != None or password != None :
    cur.execute("SELECT * FROM users WHERE `login` = '{0}'".format(login))
    rows = cur.fetchall()
    if len(rows) == 1  and rows[0][2] == password:
        print("Set-cookie:login={0}; expires=Wed May 18 03:33:20 2033; path=/cgi-bin/; httponly".format(login))
        print("Set-cookie:password={0}; expires=Wed May 18 03:33:20 2033; path=/cgi-bin/; httponly".format(password))

        content += "SUCCESS<br> <img src=\"http://25.89.162.50:8000/cats.JPG\">"
        redirectURL = "/cgi-bin/index.py"
        print("Content-type: text/html")
        print()
        print('<html><head><meta http-equiv="refresh" content="0;url='+str(redirectURL)+'" /></head></html>')
        default = ""
    else :
        content += "Ошибка логин или пароль неверный "

default = default.replace("_content_", content)
default = default.replace("_namepage_", "Войти")

print("Content-type: text/html")
print()
print(default)
        
