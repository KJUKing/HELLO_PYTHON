import pymysql

con = pymysql.connect(host='127.0.0.1', user='root', password='python', port=3305, db='python', charset='utf8')

cur = con.cursor()

e_id = "6"

sql = f"""DELETE FROM emp
        WHERE e_id = '{e_id}'"""

print(sql)

cur.execute(sql)
print("cnt : ", cur.rowcount)

con.commit()
con.close()

