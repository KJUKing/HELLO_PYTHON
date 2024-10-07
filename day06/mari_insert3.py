import pymysql

con = pymysql.connect(host='127.0.0.1', user='root', password='python', port=3305, db='python', charset='utf8')

cur = con.cursor()

e_id = "6"
e_name = "6"
e_gen = "6"
e_addr = "6"

sql = f"""INSERT INTO emp 
        (e_id, e_name, e_gen, e_addr) 
        VALUES 
        ('{e_id}', '{e_name}', '{e_gen}', '{e_addr}')"""

print(sql)

cur.execute(sql)
print("cnt : ", cur.rowcount)

con.commit()
con.close()

