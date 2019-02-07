from flask import (
    Flask,
    jsonify,
    request
)

from pymongo import MongoClient
import subprocess
import json
import requests

app = Flask(__name__)
client = MongoClient('localhost', 27017)
db = client['imageclassification']
Image = db['Images']

@app.route('/')
def index():
    return 'ok'

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()

    res = Image.insert_one({
        'username': data['username'],
        'password': data['password'],
        'toke_amount': 5
    })

    return jsonify({
        'success': True,
    })

@app.route('/classify')
def classify():
    data = request.get_json()
    url = data['url']

    r = requests.get(url)
    ret = {}
    with open("temp.jpg", "wb") as f:
        f.write(r.content)
        proc = subprocess.Popen('python classify_image.py --image_file=temp.jpg', shell=True)
        proc.communicate()[0]
        proc.wait()
        with open('text.txt') as g:
            ret = json.load(g)
    
    return jsonify(ret)

if __name__ == "__main__":
    app.run()