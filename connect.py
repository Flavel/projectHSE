import pymysql
con = pymysql.connect('localhost', 'root', 'admin123', 'wikiHSE')
cur = con.cursor()