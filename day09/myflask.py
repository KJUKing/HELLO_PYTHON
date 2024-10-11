import pymysql.cursors
from flask import Flask, request, render_template
from day09.dao_emp import DaoEmp

app = Flask(__name__)


@app.route('/')
@app.route('/emp_list.do')
def emp_list():
    de = DaoEmp()
    list = de.selectList()
    return render_template('emp_list.html', list=list)


@app.route('/emp_detail.do')
def emp_detail():
    e_id = request.args.get('e_id', default='1')
    print(e_id)
    de = DaoEmp()
    vo = de.select(e_id)
    return render_template('emp_detail.html', vo=vo)


@app.route('/emp_mod.do')
def emp_mod():
    e_id = request.args.get('e_id', default='1')
    de = DaoEmp()
    vo = de.select(e_id)
    return render_template('emp_mod.html', vo=vo)

@app.route('/emp_add.do')
def emp_add():
    return render_template('emp_add.html')

@app.route('/emp_mod.act', methods=["POST"])
def emp_mod_act():
    e_id = request.form['e_id']
    e_name = request.form['e_name']
    e_gen = request.form['e_gen']
    e_addr = request.form['e_addr']
    de = DaoEmp()
    cnt = de.update(e_id, e_name, e_gen, e_addr)
    return render_template('emp_mod_act.html', cnt=cnt)

@app.route('/emp_add.act', methods=["POST"])
def emp_mod_act():
    e_id = request.form['e_id']
    e_name = request.form['e_name']
    e_gen = request.form['e_gen']
    e_addr = request.form['e_addr']
    de = DaoEmp()
    cnt = de.insert(e_id, e_name, e_gen, e_addr)
    return render_template('emp_add_act.html', cnt=cnt)

@app.route('/emp_del.act', methods=["POST"])
def emp_del_act():
    e_id = request.form['e_id']
    de = DaoEmp()
    cnt = de.update(e_id)
    return render_template('emp_del_act.html', cnt=cnt)

if __name__ == '__main__':
    app.run(debug=True)
