import pymysql

con = pymysql.connect(host='127.0.0.1', user='root', password='python', port=3305, db='python', charset='utf8')

cur = con.cursor()
m_name = "3"
tel = "3"
email = "3"

sql = f"""INSERT INTO mem 
        (m_name, tel, email)
        VALUES 
        ('{m_name}', '{tel}', '{email}')
"""

print(sql)

cur.execute(sql)
print("cnt : ", cur.rowcount)

con.commit()
con.close()

