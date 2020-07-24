import functools
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for, jsonify
)
from werkzeug.security import check_password_hash, generate_password_hash
from flask_jwt_extended import create_access_token
from pymongo import MongoClient
from datetime import datetime
import os
from dotenv import load_dotenv
load_dotenv()

bp = Blueprint('auth', __name__, url_prefix='/auth')

client = MongoClient(os.getenv("MONGO_URI"))
db = client["freedemyDb"]

# connect to the collections
users = db["users"]

@bp.route('/register', methods=('GET', 'POST'))
def register():
    """docstring"""

    result = "register"
    if request.method == 'POST':
        first_name = request.get_json()['first_name']
        last_name = request.get_json()['last_name']
        email = request.get_json()['email']
        password = generate_password_hash(request.get_json()['password'])
        created = datetime.utcnow()

        if users.find_one({'email': email}) is not None:
            result = jsonify({"error": "User is already registered"})
        else:
            user = users.insert_one({
                "first_name": first_name,
                "last_name": last_name,
                "email": email,
                "password": password,
                "created": created
            })
            new_user = users.find_one({"_id": user.inserted_id})

            result = jsonify({"confirmation": new_user["email"] + " registered!"})

    return render_template('auth/register.html', result=result)


@bp.route('/login', methods=('GET', 'POST'))
def login():
    """docstring"""
    result = "login"
    if request.method == 'POST':
        email = request.get_json()['email']
        password = request.get_json()['email']

        user = users.find_one({'email': email})

        if user is None:
            result = jsonify({"error": "Invalid email"})
        elif not check_password_hash(user['password'], password):
            result = jsonify({"error": "Invalid password"})
        else:
            access_token = create_access_token(identity = {
                "first_name": user['first_name'],
                "last_name": user['last_name'],
                "email": user['email']
                }
            )
            result = jsonify({"token": access_token})
        
    return render_template('auth/login.html', result=result)
        