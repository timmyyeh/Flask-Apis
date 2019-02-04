from flask import (
    Flask,
    request,
    jsonify
)
from pymongo import MongoClient
import bcrypt
import spacy

app = Flask(__name__)

# setting up database
client = MongoClient('localhost', 27017)
db = client['nlp']
User = db['user']

@app.route('/')
def index():
    return 'ok'

@app.route('/register')
def register():
    data = request.get_json()
    
    if userExist(data['username']):
        return jsonify({
            'status': 301,
            'message': 'username already exist'
        })
    
    # hash the user password
    hashpass = bcrypt.hashpw(data['password'], bcrypt.gensalt())

    # store it into database
    User.insert({
        'username': data['username'],
        'password': hashpass,
        'tokens': 5
    })

    return jsonify({
        'status': 200,
        'success': True
    })

@app.route('/detect')
def detect():
    data = request.get_json()

    # verify user
    if not verifyUser(data['username'], data['password']):
        return jsonify({
            'status': 302,
            'message': 'Invalid username or password'
        })

    # compare text
    nlp = spacy.load('en_core_web_sm')
    text1 = nlp(data['text1'])
    text2 = nlp(data['text2'])

    user = User.find({'username': data['username']})[0]
    User.update({
        'username': data['username']
    }, {
        '$set': {'tokens': user['tokens'] - 1}
    })

    return jsonify({
        'status': 200,
        'sucess': True,
        'similarity': text1.similarity(text2)
    })

def verifyUser(username, passowrd):
    if not userExist(username):
        print(username)
        print('user not exist')
        return False
    
    hPass = User.find({'username': username})[0]['password']

    if not bcrypt.hashpw(passowrd, hPass) == hPass:
        print('password not match')
        return False

    return True

def userExist(username):
    if User.find({'username': username}).count() == 1:
        return True
    return False


if __name__ == "__main__":
    app.run()

