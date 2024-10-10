from pymongo import MongoClient
from flask import Flask, render_template

app = Flask(__name__)


client = MongoClient('localhost', 27017)
db = client['python']
emp_collection = db['emp']

cnt = emp_collection.insert_one({"e_id":4, "e_name":4, "gen" : 4, "addr":4})

print("cnt : ", cnt)
@app.route('/mongo')
def mongo():
    client = MongoClient('localhost', 27017)
    db = client['python']
    emp_collection = db['emp']

    # list = emp_collection.find()
    # for x in list():
    #     print(x)

    emp_list = list(emp_collection.find())
    print(emp_list)
    return render_template('mongo.html', mongo_list=emp_list)

if __name__ == '__main__':

    app.run(debug=True)
