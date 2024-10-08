from pymongo import MongoClient
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/mongo')
def mongo():
    client = MongoClient('localhost', 27017)
    db = client['python']
    emp_collection = db['emp']

    emp_list = list(emp_collection.find())
    print(emp_list)
    return render_template('mongo.html', mongo_list=emp_list)
if __name__ == '__main__':

    app.run(debug=True)
