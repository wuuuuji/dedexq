import pymysql

db = pymysql.connect(host="8.129.128.31", user='root', password='Qwe1355wu*.*', database='student')

cursor = db.cursor()

sql = "select * from user"
try:
    cursor.execute(sql)
    results = cursor.fetchall()
    for row in results:
        id = row[0]
        name = row[1]
        sex = row[2]
        print("id=%s,name=%s,sex=%s" %(id,name,sex))
except:
    print("123")

db.close()