from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

from pymongo import MongoClient
import certifi
client = MongoClient('mongodb://test:sparta@cluster0-shard-00-00.pbhz9.mongodb.net:27017,cluster0-shard-00-01.pbhz9.mongodb.net:27017,cluster0-shard-00-02.pbhz9.mongodb.net:27017/?ssl=true&replicaSet=atlas-okqc9s-shard-0&authSource=admin&retryWrites=true&w=majority', tlsCAFile= certifi.where())
db = client.dbsparta

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/mars", methods=["POST"])
def web_mars_post():
    name_receive = request.form['name_give']
    address_receive = request.form['address_give']
    size_receive = request.form['size_give']
    price_receive = request.form['price_give']
    doc = {
        'name':name_receive,
        'address':address_receive,
        'size':size_receive,
        'price': price_receive
    }
    db.mars.insert_one(doc)

    return jsonify({'msg': '주문 완료!'})

@app.route("/mars", methods=["GET"])
def web_mars_get():
    order_list = list(db.mars.find({}, {'_id': False}))
    return jsonify({'orders': order_list})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)