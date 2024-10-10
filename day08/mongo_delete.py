from pymongo import MongoClient
from flask import Flask, render_template


client = MongoClient('localhost', 27017)
db = client['python']
emp_collection = db['emp']

cnt = emp_collection.delete_many({"e_id":"3"})
#update_many도 있어요

# print("cnt: ", cnt.raw_result['n'])

print("cnt : ", cnt)

