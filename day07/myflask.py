import pymysql.cursors
from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello, Flask!'


@app.route('/param', methods=['GET'])
def param():
    # menu = request.args.get('menu', default = '탕수육', type = str)
    menu = request.args['menu']
    print(menu)
    return 'PARAM : ' + menu


@app.route('/post', methods=['POST'])
def post():
    # menu = request.form['menu']
    menu = request.form.get('menu', default='탕수육')
    return 'POST : ' + menu


@app.route('/forw')
def forw():
    a = "홍길동"
    b = ["전우치", "외계인", "지구인"]
    c = [
        {'e_id': 1, 'e_name': 1, 'gen': 1, 'addr': 1},
        {'e_id': 2, 'e_name': 2, 'gen': 2, 'addr': 2}
    ]
    return render_template('forw.html', name=a, arr=b, c=c)


@app.route('/emp')
def emp():
    conn = pymysql.connect(host='127.0.0.1', user='root', password='python', port=3305, db='python', charset='utf8')

    cur = conn.cursor(pymysql.cursors.DictCursor)

    sql = "SELECT * FROM emp"
    cur.execute(sql)
    res = cur.fetchall()

    print(res)

    cur.close()
    conn.close()

    return render_template('emp.html', emp_list=res)

if __name__ == '__main__':
    app.run(debug=True)
