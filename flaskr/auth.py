import functools
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for, jsonify
)
from werkzeug.security import check_password_hash, generate_password_hash
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
        first_name = request.form['first-name']
        last_name = request.form['last-name']
        email = request.form['email']
        password = generate_password_hash(request.form['password'])
        created = datetime.utcnow()

        error = None

        if not email:
            error = 'Email is required.'
        elif not password:
            error = 'Password is required.'

        if users.find_one({'email': email}) is not None:
            error = 'User is already is registered'
        
        if error is None:
            user = users.insert_one({
                "first_name": first_name,
                "last_name": last_name,
                "email": email,
                "password": password,
                "created": created
            })
            new_user = users.find_one({"_id": user.inserted_id})
            flash("Confirmation:" + new_user["email"] + " registered!")
            return redirect(url_for('auth.login'))

        flash(error)

    return render_template('auth/register.html')


@bp.route('/login', methods=('GET', 'POST'))
def login():
    """docstring"""
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        user = users.find_one({'email': email})
        
        error = None

        if user is None:
            error = "Invalid email"
        elif not check_password_hash(user['password'], password):
            error = "Invalid password"
        else:
            session.clear()
            session["user_id"] = str(user["_id"])
            
            return redirect(url_for('index'))
        
        flash(error)
        
    return render_template('auth/login.html')


@bp.before_app_request
def load_logged_in_user():
    user_id = session.get("user_id")
    if user_id is None:
        g.user = None
    else:
        g.user = True


@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))