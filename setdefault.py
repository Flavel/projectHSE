import cgi
import pymysql
import connect
import os
import http.cookies
def init():
    f = open('default.html', 'r')
    default = f.read()
    con = connect.con
    cur = con.cursor()
    cookie = http.cookies.SimpleCookie(os.environ.get("HTTP_COOKIE"))
    login = cookie.get("login")
    password = cookie.get("password")
    if login is None or password is None :
        default = default.replace("_user_", """<a href = '/cgi-bin/login.py'>Войти</a> или 
                                                <a href = '/cgi-bin/register.py'>Зарегистрироваться</a>""")
    else :
        cur.execute("SELECT * FROM `users` WHERE `login` = '{0}' AND `password` = '{1}'".format(login.value, password.value))
        rows = cur.fetchall()
        if len(rows) == 1 :
            default = default.replace("_user_", """Вы вошли как {0}<br>
                                            <a href = '/cgi-bin/exit.py'>выйти</a>""".format(login.value))
        else :
            print("Set-cookie:login={0}; expires=Wed May 17 03:33:20 2000; path=/cgi-bin/; httponly".format(login))
            print("Set-cookie:password={0}; expires=Wed May 17 03:33:20 2000; path=/cgi-bin/; httponly".format(password))
    return default
def check():
    con = connect.con
    cur = con.cursor()
    cookie = http.cookies.SimpleCookie(os.environ.get("HTTP_COOKIE"))
    login = cookie.get("login")
    password = cookie.get("password")
    if login is None or password is None :
        return False
    cur.execute("SELECT * FROM `users` WHERE `login` = '{0}' AND `password` = '{1}'".format(login.value, password.value))
    rows = cur.fetchall()
    if len(rows) == 1 :
        return True
    return False

def getuserid():
    con = connect.con
    cur = con.cursor()
    cookie = http.cookies.SimpleCookie(os.environ.get("HTTP_COOKIE"))
    login = cookie.get("login")
    password = cookie.get("password")

    cur.execute("SELECT * FROM `users` WHERE `login` = '{0}' AND `password` = '{1}'".format(login.value, password.value))
    rows = cur.fetchall()
    if len(rows) == 1 :
        return rows[0][0]