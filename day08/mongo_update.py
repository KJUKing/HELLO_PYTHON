from pymongo import MongoClient
from flask import Flask, render_template


client = MongoClient('localhost', 27017)
db = client['python']
emp_collection = db['emp']

cnt = emp_collection.update_one({"e_id":"3"}, { "$set" : { "e_name":4, "gen" : 4, "addr":4}})
#update_many도 있어요

# print("cnt: ", cnt.raw_result['n'])

print("cnt : ", cnt)

