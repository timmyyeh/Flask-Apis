from flask import (
    Flask,
    jsonify,
    request
)
import bcrypt
from pymongo import MongoClient

app = Flask(__name__)

# database
client = MongoClient('localhost', 27017)
db = client['mydb']
Sentance = db['Sentence']

@app.route('/')
def index():
    return "ok"

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()

    username = data['username']
    password = data['password']

    hpass = bcrypt.hashpw(password, bcrypt.gensalt())
    print('password: {}, encrypted password: {}'.format(password, hpass))

    Sentance.insert({
        'username': username,
        'password': hpass,
        'sentence': '',
        'token': 5
    })

    return jsonify({
        'success': True,
        'status': 200
    })

@app.route('/store', methods=['POST'])
def store():
    data = request.get_json()

    # find user
    sentence = Sentance.find({'username':data['username']})[0]
    # check password
    if not bcrypt.hashpw(data['password'], sentence['password']) == sentence['password']:
        return jsonify({
            'error': 'password does not match',
            'status': 301
        })

    # update sentence
    res = Sentance.update_one({'username': data['username']}, {'$set': {'sentence': data['sentence']}})
    return jsonify({
        'success': res.raw_result
    })

if __name__ == "__main__":
    app.run()