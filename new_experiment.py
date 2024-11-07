from flask import Flask, render_template,request
app=Flask(__name__)
@app.route('/')
def home():
    return "Welcome! To Home Page"
@app.route('/del_usr',methods=['delete'])
def del_usr():
    return render_template('/table_data.html')
app.run(debug=True)