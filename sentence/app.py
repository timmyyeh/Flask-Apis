from flask import (
    Flask,
    jsonify,
    request
)

from pymongo import MongoClient

app = Flask(__name__)

# database
client = MongoClient('localhost', 27017)
db = client['mydb']
Sentance = db['Sentence']

@app.route('/')
def index():
    return "ok"


if __name__ == "__main__":
    app.run()