from flask import (
    Flask,
    request,
    jsonify
)
from pymongo import MongoClient
import requests

app = Flask(__name__)
client = MongoClient('localhost', 27017)
db = client['mydb']
UserNum = db['UserNum']

@app.route('/')
def index():
    return 'okssss'

@app.route('/add')
def addition():
    data = request.get_json()
    if 'x' not in data:
        return "Missing x"
    if 'y' not in data:
        return "Missing y"
    return jsonify({
        'Sum': data['x'] + data['y']
    })

@app.route('/subtract')
def subtract():
    data = request.get_json()
    return jsonify({
        "DATA": data['x'] - data['y']
    })

@app.route('/visit')
def visit():
    prev = UserNum.find({})[0]["num_of_users"]
    num = prev + 1
    UserNum.update({},{'$set': {"num_of_users": num}})
    return 'previous num: {0}, updated num: {1}'.format(str(prev),str(num))


if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=True)