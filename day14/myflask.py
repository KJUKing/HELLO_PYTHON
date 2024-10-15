from flask import jsonify
from flask import Flask, request, render_template, redirect

from day09.dao_emp import DaoEmp

app = Flask(__name__)


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
    e_id = request.json['e_id']
    de = DaoEmp()
    emp = de.select(e_id)
    return jsonify(emp=emp)

if __name__ == '__main__':
    app.run(port=80)

