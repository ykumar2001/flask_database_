from flask import Flask,request,render_template, redirect
from bson import ObjectId 
from pymongo import MongoClient

mongo_client=MongoClient("mongodb://localhost:27017")
database=mongo_client['mydatabase']
info_collection=database['info']

app=Flask(__name__)
@app.route('/')
def home():
    return "welcome! to this page."
@app.route('/fnl_name')
def fnl_name():
    return render_template('f&l_name.html')

@app.route('/data',methods=['get','POST'])
def data():
    fn=request.form.get('first_name')
    ln=request.form.get('last_name')
    print("firstname",fn)
    print("lastname",ln)
    if request.method=='POST':
        new_dict={"first_name":f"{fn}","last_name":f"{ln}"}
        info_collection.insert_one(new_dict)
        return "successfully submitted!"
    else:
        return render_template('f&l_name.html')  
    
@app.route('/DBtoAPI',methods=['get'])
def DBtoAPI():
    info=list(info_collection.find())
    
    return render_template('/getDATA_mymongo.html',data=info)


@app.route('/tab/<string:eid>', methods=["GET"])
def table_data(eid):
    info_collection.delete_one({"_id":ObjectId(eid)})
    return redirect('/DBtoAPI')
app.run(debug=True)