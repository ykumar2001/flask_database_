########### input user_id and password on flask ,saving it into database. #################

from flask import Flask,jsonify,request,render_template

import mysql.connector


mydb=mysql.connector.connect(
    host="localhost",
    username="root_yogesh",
    password="cG9aczQ$1",
    database="db_goognu")
mycursor=mydb.cursor()


app=Flask(__name__)
@app.route('/')
def home_page():
    return "welcome!pepole,how you doing?"

@app.route('/rough',methods=['get'])
def rough():
    return render_template('/rough.html')

@app.route('/info',methods=['get','post'])
def info():

    u_id=request.form.get('user_id')
    pass_d=request.form.get('password')
    
    u_id=request.json.get('user_id')
    pass_d=request.json.get('password')

    print("userID:",u_id)
    print("password:",pass_d)
   
    mycursor.execute(f"insert into config values('{u_id}','{pass_d}')")
    mydb.commit()
    return jsonify("successfully sumitted")



app.run(debug=True)