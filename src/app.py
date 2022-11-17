from http.client import NOT_FOUND

from flask import Flask, Response, jsonify, request
from flask_pymongo import PyMongo
from werkzeug.security import check_password_hash, generate_password_hash

app = Flask(__name__)
app.config['MONGO_URI']='mongodb://0.0.0.0:27017'
mongo = PyMongo(app)


@app.route('/users', methods=['POST'])
def create_user():
    # Receiving Data
    username = request.json['username']
    password = request.json['password']
    email = request.json['email']

    if username and email and password:
        # Encrypting password
        hashed_password = generate_password_hash(password)
        id = mongo.db.users.insert_one(
            {'username': username, 'email': email, 'password': hashed_password})
        
        response = {
            'id': str(id),
            'username': username,
            'password': hashed_password,
            'email': email
        }
        return response
    else: 
        {'message': 'received'}
    return {'message': 'received'}
        
if __name__ == "__main__":
    app.run(debug=True)