import pymysql

conn = pymysql.connect(host='127.0.0.1', user='root', password='python', port=3305, db='python', charset='utf8')

cur = conn.cursor(pymysql.cursors.DictCursor)

sql = "SELECT * FROM emp"

cur.execute(sql)
res = cur.fetchall()

print(res[0]['e_name'])

cur.close()
conn.close()

