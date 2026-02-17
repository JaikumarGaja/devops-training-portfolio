from flask import Flask, jsonify
import json

app = Flask(__name__)

def get_data_from_file():
    f = open('data.json', 'r')
    return json.load(f)

@app.route('/api')
def get_api_data():
    data = get_data_from_file()
    return jsonify(data)
    
if __name__ == '__main__':
    app.run(debug=True)