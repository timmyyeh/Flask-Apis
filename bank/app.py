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

if __name__ == "__main__":
    app.run()