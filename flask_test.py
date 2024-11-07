from flask import Flask,request,jsonify,render_template
import mysql.connector


mydb=mysql.connector.connect(
    host="localhost",
    username="root_yogesh",
    password="cG9aczQ$1",
    database="mydatabase"
)
mycursor = mydb.cursor()

app=Flask(__name__)

@app.route('/')
def home():
    return "welcome! to this page."

@app.route('/test')
def test():
    return render_template ('/test.html')


@app.route('/details', methods=['post'])
def details():
    f_name=request.form.get('first_name')
    l_name=request.form.get('last_name')
    print("first name",f_name)
    print("last name",l_name)

    mycursor.execute(f"insert into info values('{f_name}','{l_name}') ")
    mydb.commit()
    return jsonify("success")


@app.route('/getall',methods=['get'])
def get_all():
    
    mycursor.execute("select * from info" )
    rr=mycursor.fetchall()
    return render_template('all_employee.html', employee = rr)
app.run(debug=True)
