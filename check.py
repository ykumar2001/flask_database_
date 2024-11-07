from flask import Flask,render_template,redirect,request
from bson import ObjectId
from pymongo import MongoClient

mongo_client=MongoClient("mongodb://localhost:27017")
database=mongo_client['mydatabase']
info_collection=database['info']

app=Flask(__name__)
# dispaly home page.
@app.route('/')
def home():
    return "hellooooooooo!!!!WELOCME"

# display basic structure.
@app.route('/display')
def display():
    return render_template('/fnl_structure.html')

# upload data and show it into database, return hallelujah!! on web page.
@app.route('/data',methods=['POST'])
def upload():
    fname=request.form.get('first_name')
    lname=request.form.get('last_name')
    new={"first_name":f"{fname}","last_name":f"{lname}"}
    info_collection.insert_one(new)
    return "hallelujah!!!!"

# display information from database to API.
@app.route('/getdata',methods=['get'])
def get_data():
    info=list(info_collection.find())
    print(info)
    return render_template('/mymongoDB_to_API.html',data=info)

# delete infomaton on API.
@app.route('/tab/<string:id>',methods=['GET'])
def update(id):
    info_collection.delete_one({"_id":ObjectId(id)})
    return redirect('/getdata') 

# update data on API and save it on database using a particular objectid of a person.
@app.route('/update',methods=['POST'])
def update_info():
    fname=request.form.get('first_name')
    lname=request.form.get('last_name')
    cid=request.form.get("_id")
    print(fname)
    print(lname)
    info_collection.update_one(
        {"_id":ObjectId(cid)},
        {"$set":{"first_name":fname,"last_name":lname}}
    )
    return redirect ('/getdata')

# shows firstname ,last name and you can modify it to update its object id.
@app.route('/detinfo/<string:id>',methods=['get'])
def detail_info(id):
    
    cand=(info_collection.find_one({"_id":ObjectId(id)}))
    return render_template('/get_into_info.html',cand=cand)


app.run(debug=True)