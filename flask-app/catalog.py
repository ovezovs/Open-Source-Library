import functools
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for, jsonify, json
)
from pymongo import MongoClient
from bson.objectid import ObjectId
import os
from dotenv import load_dotenv
load_dotenv()

bp = Blueprint('catalog', __name__, url_prefix='/catalog')

client = MongoClient(os.getenv("MONGO_URI"))
db = client["freedemyDb"]

# connect to the collections
users = db["users"]
books = db["books"]
articles = db["articles"]
courses = db["courses"]
tracks = db["tracks"]


@bp.route('/', methods=('GET', 'POST'))
def user_catalog():
    saved_items_list = []

    all_items = list(books.find()) + list(articles.find()) + list(courses.find()) + list(tracks.find())

    # handle the saved resources for the logged in user
    if g.user:
        user_id = ObjectId(session.get("user_id"))   # get current user
        user = users.find_one({"_id": user_id})
        saved_item_ids_list = user["saved"]
        saved_item_set = set(saved_item_ids_list)   # use set for runtime efficiency
        
        for item in all_items:
            if str(item["_id"]) in saved_item_set:
                saved_items_list.append(item)


    return render_template('catalog/resources.html', resources=saved_items_list, user_catalog=True, user_catalog_empty= len(saved_items_list)==0)


@bp.route('/books', methods=('GET', 'POST'))
def populate_books():
    cursor = books.find()
    books_list = list(cursor)
    
    # handle the saved resources for the logged in user
    if g.user:
        user_id = ObjectId(session.get("user_id"))   # get current user
        user = users.find_one({"_id": user_id})
        saved_item_ids_list = user["saved"]
        saved_item_set = set(saved_item_ids_list)   # use set for runtime efficiency
        
        for item in books_list:
            if str(item["_id"]) in saved_item_set:
                item["saved"] = True       # mark the saved books

    return render_template('catalog/resources.html', resources=books_list, books=True)

@bp.route('/articles', methods=('GET', 'POST'))
def populate_articles():
    cursor = articles.find()
    articles_list = list(cursor)

    # handle the saved resources for the logged in user
    if g.user:
        user_id = ObjectId(session.get("user_id"))   # get current user
        user = users.find_one({"_id": user_id})
        saved_item_ids_list = user["saved"]
        saved_item_set = set(saved_item_ids_list)   # use set for runtime efficiency
        
        for item in articles_list:
            if str(item["_id"]) in saved_item_set:
                item["saved"] = True       # mark the saved books

    return render_template('catalog/resources.html', resources=articles_list, articles=True)

@bp.route('/courses', methods=('GET', 'POST'))
def populate_courses():
    cursor = courses.find()
    courses_list = list(cursor)

    # handle the saved resources for the logged in user
    if g.user:
        user_id = ObjectId(session.get("user_id"))   # get current user
        user = users.find_one({"_id": user_id})
        saved_item_ids_list = user["saved"]
        saved_item_set = set(saved_item_ids_list)   # use set for runtime efficiency
        
        for item in courses_list:
            if str(item["_id"]) in saved_item_set:
                item["saved"] = True       # mark the saved books

    return render_template('catalog/resources.html', resources=courses_list, courses=True)

@bp.route('/tracks', methods=('GET', 'POST'))
def populate_tracks():
    cursor = tracks.find()
    tracks_list = list(cursor)

    # handle the saved resources for the logged in user
    if g.user:
        user_id = ObjectId(session.get("user_id"))   # get current user
        user = users.find_one({"_id": user_id})
        saved_item_ids_list = user["saved"]
        saved_item_set = set(saved_item_ids_list)   # use set for runtime efficiency
        
        for item in tracks_list:
            if str(item["_id"]) in saved_item_set:
                item["saved"] = True       # mark the saved books

    return render_template('catalog/resources.html', resources=tracks_list, tracks=True)


@bp.route('/save/<item_id>', methods=('GET', 'POST'))
def save_resource(item_id):
    user_id = ObjectId(session.get("user_id"))
    
    if g.user:
        user = users.find_one({"_id": user_id})
        saved_item_ids_list = user["saved"]
        saved_item_ids_list.append(item_id)
        users.update_one({"_id": user_id}, {"$set": {"saved": saved_item_ids_list}}, upsert=False)

        return jsonify(status=200)

    return jsonify(status=500)

