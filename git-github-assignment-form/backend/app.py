from flask import Flask, jsonify, request
from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()
URI = os.getenv("MONGO_URI")

client  = MongoClient(URI)
db = client.test
collection = db['todo_items']

app = Flask(__name__)
@app.route('/submit', methods=['POST'])
def submit():
    data = request.get_json()
    title = data.get('title')
    description = data.get('description')

    todo_item = {
        'title': title,
        'description': description
    }
    collection.insert_one(todo_item)

    print(f"Received To-Do Item: Title: {title}, Description: {description}")
    
    return jsonify({'message': 'To-Do item submitted successfully'}), 201

@app.route('/todo', methods=['GET'])
def get_todo():
    todo_items = list(collection.find({}, {'_id': 0}))
    return jsonify(todo_items), 200

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5001, debug=True)