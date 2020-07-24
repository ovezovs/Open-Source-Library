import os
from flask import Flask
from pymongo import MongoClient
from dotenv import load_dotenv
load_dotenv()


client = MongoClient(os.getenv("MONGO_URI"))
db = client["freedemyDb"]
print(os.getenv("MONGO_URI"))
# connect to the collections
users = db["users"]
books = db["books"]
articles = db["articles"]
courses = db["courses"]
tracks = db["tracks"]

app = Flask(__name__)

@app.route('/home')
def get_current_time():
    return {"time": "Hello World"}