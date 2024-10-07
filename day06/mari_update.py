import pymysql

con = pymysql.connect(host='127.0.0.1', user='root', password='python', port=3305, db='python', charset='utf8')

cur = con.cursor()

e_id = "6"
e_name = "44"
e_gen = "4"
e_addr = "22"

sql = f"""UPDATE emp SET  
        e_name = '{e_name}',
        e_gen = '{e_gen}',
        e_addr = '{e_addr}'
        WHERE e_id = '{e_id}'"""

print(sql)

cur.execute(sql)
print("cnt : ", cur.rowcount)

con.commit()
con.close()

