from flask import (
    Flask,
    jsonify,
    request
)

import bcrypt
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient('localhost', 27017)
db = client['imageclassification']
Image = db['Images']

@app.route('/')
def index():
    return 'ok'



if __name__ == "__main__":
    app.run()