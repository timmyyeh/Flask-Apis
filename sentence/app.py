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


if __name__ == "__main__":
    app.run()