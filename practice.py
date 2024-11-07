from flask import Flask , request ,jsonify
app=Flask(__name__)
data = [
    {"id": 1, "name": "Item 1", "description": "This is item 1"},
    {"id": 2, "name": "Item 2", "description": "This is item 2"},
    {"id": 3, "name": "Item 3", "description": "This is item 3"}
]

@app.route('/')
def home():
    return "welcome to the Flask API Demo!"

@app.route('/items',methods=['get'])
def get_itmes():
    return jsonify(data)



@app.route('/items/<int:item_id>',methods=['get'])
def get_item(item_id):
    item=None
    for x in data:
        if x['id']==item_id:
            item=x
            break
    if item:
        return jsonify(item)
    else:
        return jsonify({"message":"item not found"}),404
    
@app.route('/items/<string:item_name>',methods=['get'])
def str_test(item_name):
    return f"hello {item_name}"


@app.route('/item',methods=['post'])
def add_item():
    new_item=request.json
    print("new items: ", new_item)
    data.append(new_item) 
    return jsonify(data),201       

@app.route('/items/<int:item_id>',methods=['put'])
def update_item(item_id):
    item=None
    for x in data:
        if x['id'] == item_id:
            item=x
            break
    if item:
        item.update(request.json)
        return jsonify(item)
    else:
        return jsonify({"message":"item not found"}),404    
    
@app.route('/item/<int:item_id>',methods=['delete']) 
def delete_item(item_id):
    item=None
    for x in data:
        if x['id'] ==item_id:
            item=x
            break
    else:
        return jsonify({"message":"item not found"}),404       

    data.remove(item)
    return jsonify({"data" :data})
app.run(debug=True)