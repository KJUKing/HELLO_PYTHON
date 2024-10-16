import pymysql


class DaoEmp:
    def __init__(self):
        self.con = pymysql.connect(host='127.0.0.1', user='root', password='python', port=3305, db='python', charset='utf8')
        self.cur = self.con.cursor(pymysql.cursors.DictCursor)

    def selectList(self):
        sql = "SELECT * FROM emp"

        self.cur.execute(sql)
        list = self.cur.fetchall()

        return list

    def select(self, e_id):
        sql = "SELECT * FROM emp WHERE e_id = %s"
        self.cur.execute(sql, (e_id,))
        vo = self.cur.fetchone()  # fetchall() 대신 fetchone() 사용
        return vo


    def insert(self, e_id, e_name, e_gen, e_addr):
        sql = f"""
            INSERT INTO emp
                (e_id, e_name, e_gen, e_addr)
            VALUES 
                ('{e_id}','{e_name}','{e_gen}','{e_addr}')
        """

        self.cur.execute(sql)
        self.con.commit()
        return self.cur.rowcount

    def update(self, e_id, e_name, e_gen, e_addr):
        sql = """
            UPDATE emp
            SET
                e_name = %s, 
                e_gen = %s,
                e_addr = %s
            WHERE 
                e_id = %s
        """
        self.cur.execute(sql, (e_name, e_gen, e_addr, e_id))  # 매개변수 바인딩
        self.con.commit()
        return self.cur.rowcount  # 수정된 행의 개수 반환


    def delete(self, e_id):
        sql = f"""
            DELETE FROM emp
            WHERE e_id = '{e_id}'
        """
        self.cur.execute(sql)
        self.con.commit()
        return self.cur.rowcount

    def __del__(self):
        self.cur.close()
        self.con.close()

if __name__ == '__main__':
    de = DaoEmp()
    cnt = de.insert("6","6","6","6")
    print("cnt :", cnt)
    # list = de.selectList()
    # print("list : ", list)