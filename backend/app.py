from flask import Flask, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient("mongodb://mongodb:27017/")
db = client["webapp"]
collection = db["users"]

@app.route('/submit', methods=['POST'])
def submit():
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    if name and email:
        collection.insert_one({'name': name, 'email': email})
        return jsonify({'success': True}), 200
    else:
        return jsonify({'success': False, 'error': 'Name and email are required'}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
