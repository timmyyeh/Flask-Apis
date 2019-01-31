from flask import (
    Flask,
    request,
    jsonify
)
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return 'okssss'

@app.route('/add')
def addition():
    data = request.get_json()
    if 'x' not in data:
        return "Missing x"
    if 'y' not in data:
        return "Missing y"
    return jsonify({
        'Sum': data['x'] + data['y']
    })


if __name__ == "__main__":
    app.run()