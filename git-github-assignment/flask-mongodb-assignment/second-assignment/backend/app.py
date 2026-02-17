from flask import Flask, request
from dotenv import load_dotenv
import requests
from pymongo import MongoClient
import os

load_dotenv()

uri = os.getenv('MONGO_URI')

client = MongoClient(uri)
db = client.test
collection = db['flask-assignment']

app = Flask(__name__)

@app.route('/success', methods=['POST'])
def success():
    form_data = request.get_json()
    collection.insert_one(form_data)
    return 'Data received and stored in MongoDB'

if __name__ == '__main__':
    app.run(host='127.0.0.2', port=5001, debug=True)