from flask import (
    Flask,
    request,
    jsonify
)

from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient('localhost', 27017)
db = client['BankAPI']
User = db['Users']

@app.route('/')
def index():
    return 'ok'

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data['username']
    password = data['password']
    amount = 0

    User.insert_one({
        'username': username,
        'password': password,
        'amount': amount
    })
    
    return jsonify({'success': True})

@app.route('/deposit', methods=['POST'])
def deposit():
    data = request.get_json()

    # find person
    person = User.find_one({'username': data['username']})

    # store money
    res = User.update_one({'username': data['username']}, {'$set': {'amount': data['amount'] + person['amount']}})
    print(res.raw_result)
    return jsonify({'success': True})

@app.route('/withdraw', methods=['POST'])
def withdraw():
    data = request.get_json()

    # find person
    person = User.find_one({'username': data['username']})

    # check password

    # check balance

    # update
    User.update_one({'username': data['username']}, {'$set': {'amount': person['amount'] - data['amount']}})
    return jsonify({'success':True})
if __name__ == "__main__":
    app.run()