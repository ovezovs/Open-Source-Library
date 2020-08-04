import functools
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for, jsonify, json
)
from pymongo import MongoClient
from bson.objectid import ObjectId
import os
from dotenv import load_dotenv
load_dotenv()

admin = Blueprint('admin', __name__, url_prefix='/admin')

client = MongoClient(os.getenv("MONGO_URI"))
db = client["freedemyDb"]

# connect to the collections
users = db["users"]
books = db["books"]
articles = db["articles"]
courses = db["courses"]
tracks = db["tracks"]


# Resource Document keys
TITLE_KEY                   = "title"
OFFERED_BY_KEY              = "offered_by"
PROVIDER_LINK_KEY           = "provider_link"
ORIGINAL_DESCRIPTION_KEY    = "original_description"
LINK_KEY                    = "link"
TECH_STACK_KEY              = "tech_stack"
FLAGS_KEY                   = "flags"
SAVED_KEY                   = "saved"


@admin.route('/', methods=('GET', 'POST'))
def manage_resource():
    pass

@admin.route('/add', methods=('GET', 'POST'))
def add_resource():
    if request.method == 'POST':
        item_type = request.form['type']
        title = request.form['title']
        description = request.form['original_description']
        link = request.form['link']
        tech_stack = request.form.getlist('tech_stack')
        offered_by = request.form['offered_by']
        provider_link = request.form['provider_link']
        flags = request.form.getlist('flags')
        saved = False

        collection = None
        if item_type == "Book":
            collection = books
        elif item_type == "Article":
            collection = articles
        elif item_type == "Course":
            collection = courses
        elif item_type == "Track":
            collection = tracks

        try:
            collection.insert_one({
                TITLE_KEY: title,
                ORIGINAL_DESCRIPTION_KEY: description,
                LINK_KEY: link,
                TECH_STACK_KEY: tech_stack,
                OFFERED_BY_KEY: offered_by,
                PROVIDER_LINK_KEY: provider_link,
                FLAGS_KEY: flags,
                SAVED_KEY: saved
            })
            flash("Successfully added!")
        except:
            flash("Could not add the item", 'error')


    return render_template('admin/admin.html')



@admin.route('/update', methods=('GET', 'POST'))
def update_resource():
    pass


@admin.route('/remove', methods=('GET', 'POST'))
def remove_resource():
    pass