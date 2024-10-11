import pymysql.cursors
from flask import Flask, request, render_template
from day09.dao_emp import DaoEmp

app = Flask(__name__)


@app.route('/')
def main():
    return "HELLO MVVM"
if __name__ == '__main__':
    app.run(debug=True)
    app.run()

