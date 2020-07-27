import functools
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for, jsonify
)
from pymongo import MongoClient
from bson.json_util import dumps
import os
from dotenv import load_dotenv
load_dotenv()

bp = Blueprint('catalog', __name__, url_prefix='/catalog')

client = MongoClient(os.getenv("MONGO_URI"))
db = client["freedemyDb"]

# connect to the collections
books = db["books"]
articles = db["articles"]
courses = db["courses"]
tracks = db["tracks"]


@bp.route('/books', methods=('GET', 'POST'))
def populate_books():
    cursor = books.find()
    books_list = list(cursor)
    json = dumps(books_list)

    return render_template('catalog/books.html', books=books_list)

@bp.route('/articles', methods=('GET', 'POST'))
def populate_articles():
    cursor = articles.find()
    articles_list = list(cursor)

    return dumps(articles_list)

@bp.route('/courses', methods=('GET', 'POST'))
def populate_courses():
    cursor = courses.find()
    courses_list = list(cursor)

    return dumps(courses_list)

@bp.route('/tracks', methods=('GET', 'POST'))
def populate_tracks():
    cursor = tracks.find()
    tracks_list = list(cursor)

    return dumps(tracks_list)