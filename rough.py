from flask import Flask,request,jsonify, render_template
app=Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/item", methods=["POST"])
def save():
    # print(dir(request))
    # data=request.get_json()
    first_name = request.form.get('first_name')
    last_name = request.form.get('last_name')

    print("first name=",first_name)
    print("last name=",last_name)
    if first_name and last_name:
        return jsonify({"Result":"success"})
    else:
        return jsonify({"Result":"failed"})

app.run(debug=True)

import my