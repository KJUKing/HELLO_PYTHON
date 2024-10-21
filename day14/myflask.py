from flask import jsonify
from flask import Flask, request, render_template, redirect
from day09.dao_emp import DaoEmp
from flask_cors import CORS


app = Flask(__name__)
CORS(app)


@app.route('/')
def main():
    return redirect("/static/emp.html")

@app.route('/emp_list.ajax', methods=['POST'])
def ajax_emp_list():
    de =DaoEmp()
    list = de.selectList()
    return jsonify(list=list)

@app.route('/emp_one.ajax', methods=['POST'])
def ajax_emp_one():
    param = request.json['e_id']
    de = DaoEmp()
    vo = de.select(param)
    return jsonify(vo=vo)

@app.route('/emp_add.ajax', methods=['POST'])
def ajax_emp_add():
    param = request.get_json()

    e_id = param['e_id']
    e_name = param['e_name']
    e_gen = param['e_gen']
    e_addr = param['e_addr']
    de = DaoEmp()
    cnt = de.insert(e_id, e_name, e_gen, e_addr)
    return jsonify(cnt=cnt)

@app.route('/emp_mod.ajax', methods=['POST'])
def ajax_emp_mod():
    param = request.get_json()

    e_id = param['e_id']
    e_name = param['e_name']
    e_gen = param['e_gen']
    e_addr = param['e_addr']
    de = DaoEmp()
    cnt = de.update(e_id, e_name, e_gen, e_addr)
    return jsonify(cnt=cnt)

@app.route('/emp_del.ajax', methods=['POST'])
def ajax_emp_del():
    param = request.get_json()

    e_id = param['e_id']
    de = DaoEmp()
    cnt = de.delete(e_id)
    return jsonify(cnt=cnt)

if __name__ == '__main__':
    app.run(port=80)

