from flask import Flask, render_template, request, redirect, url_for, flash
import requests

BACKEND_URL = 'http://127.0.0.2:5001'

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    full_name = request.form.get('full_name')
    age = request.form.get('age')
    gender = request.form.get('gender')
    if not full_name or not age or not gender:
        return redirect(url_for('index'))
    form_data = request.form.to_dict()
    # requests.post(f'{BACKEND_URL}/success', json=form_data)
    # return render_template('success.html')
    try:
        requests.post(f'{BACKEND_URL}/success', json=form_data)
        # flash("Success! Data saved to MongoDB.")
        return redirect(url_for('index'))
    except:
        # flash("Error: Could not connect to database.")
        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='127.0.0.2', port=5000, debug=True)