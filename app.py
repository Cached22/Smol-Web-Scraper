from flask import Flask, request, jsonify, send_from_directory
import os
from database import check_credentials

app = Flask(__name__, static_folder='client')

DEBUG = False
PORT = 80

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    
    if not username or not password:
        return jsonify({'error': 'Missing username or password'}), 400
    
    authenticated = check_credentials(username, password)
    
    if authenticated:
        return jsonify({'message': 'User authenticated successfully'}), 200
    else:
        return jsonify({'error': 'Invalid username or password'}), 401

@app.route('/<path:path>')
def static_proxy(path):
    return send_from_directory(app.static_folder, path)

@app.route('/')
def root():
    return send_from_directory(app.static_folder, 'index.html')

if __name__ == '__main__':
    app.run(debug=DEBUG, host='0.0.0.0', port=PORT)