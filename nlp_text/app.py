from flask import (
    Flask,
    request,
    jsonify
)
from pymongo import MongoClient
import bcrypt

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

def userExist(username):
    if User.find({'username': username}).count() == 1:
        return True
    return False


if __name__ == "__main__":
    app.run()

