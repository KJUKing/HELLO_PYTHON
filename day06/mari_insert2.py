import pymysql

con = pymysql.connect(host='127.0.0.1', user='root', password='python', port=3305, db='python', charset='utf8')

cur = con.cursor()

sql = """INSERT INTO emp 
        (e_id, e_name, e_gen, e_addr) 
        VALUES 
        (%s, %s, %s, %s)"""

cur.execute(sql, ("5", "5", "5", "5"))
print("cnt : ", cur.rowcount)
con.commit()
con.close()

