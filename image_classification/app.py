from flask import (
    Flask,
    jsonify,
    request
)

from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient('localhost', 27017)
db = client['imageclassification']
Image = db['Images']

@app.route('/')
def index():
    return 'ok'

@app.route('/register')
def register():
    data = request.get_json()

    res = Image.insert_one({
        'username': data['username'],
        'password': data['password'],
        'toke_amount': data['token_amount']
    })

    return jsonify({
        'success': True,
        'data': res
    })


if __name__ == "__main__":
    app.run()