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

if __name__ == "__main__":
    app.run()

