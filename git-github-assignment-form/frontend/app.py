from flask import Flask, render_template, request
import requests

BACKEND_URL = '127.0.0.1:5001'

app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')    

@app.route('/submit', methods=['POST'])
def submit():
    title = request.form['title']
    description = request.form['description']
    
    data = {
        'title': title,
        'description': description
    }
    
    response = requests.post(f'http://{BACKEND_URL}/submit', json=data)
    
    if response.status_code == 201:
        return render_template('success.html')
    else:
        return "Error submitting data", 500
    
@app.route('/todo')
def todo():
    response = requests.get(f'http://{BACKEND_URL}/todo')
    
    if response.status_code == 200:
        todo_list = response.json()
        return render_template('todo.html', todo_list=todo_list)
    else:
        return "Error fetching to-do list", 500
    
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)