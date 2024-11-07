from flask import Flask,render_template,redirect,request
from bson import ObjectId
from pymongo import MongoClient

mongo_client=MongoClient("mongodb://localhost:27017")
database=mongo_client['mydatabase']
info_collection=database['info']

app=Flask(__name__)
@app.route('/')
def home_page():
    return "WELCOME!!!"

@app.route('/basic')
def basic_structure():
    return render_template('one.html')

@app.route('/subdata',methods=['POST'])
def submit_data():
    fname=request.form.get('first_name')
    lname=request.form.get('last_name')
    print(fname)
    print(lname)
    dumdum={'first_name':f'{fname}','last_name':f'{lname}'}
    info_collection.insert_one(dumdum)
    return "hallelujah!!"


@app.route('/uptodate',methods=['post'])
def uptodate():
    fname=request.form.get('first_name')
    lname=request.form.get('last_name')
    cid=request.form.get('cid')
    print(fname)
    print(lname)
    print(cid)
    info_collection.update_one(
        {"_id":ObjectId(cid)},{'$set':{'first_name':fname,'last_name':lname}}
    
    )
    return "yeyyeyee updated"

@app.route('/delu/<string:mid>',methods=['GET'])
def delete_user(mid):
    info_collection.delete_one({"_id":ObjectId(mid)})
    return "hey deleted"




app.run(debug=True)