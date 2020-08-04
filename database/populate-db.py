import os
from pymongo import MongoClient
from dotenv import load_dotenv
load_dotenv()

DROPPED = False

# Resource Document keys
TITLE_KEY                   = "title"
OFFERED_BY_KEY              = "offered_by"
PROVIDER_LINK_KEY           = "provider_link"
ORIGINAL_DESCRIPTION_KEY    = "original_description"
LINK_KEY                    = "link"
TECH_STACK_KEY              = "tech_stack"
FLAGS_KEY                   = "flags"
SAVED_KEY                   = "saved"

client = MongoClient(os.getenv("MONGO_URI"))
db = client["freedemyDb"]

db.test.insert_one({"test":"envvar"})

# connect to the collections
users = db["users"]
books = db["books"]
articles = db["articles"]
courses = db["courses"]
tracks = db["tracks"]

# drop all the collections before uploading new data
try:
    books.drop()
    articles.drop()
    courses.drop()
    tracks.drop()
    print("Dropped all collections")
    DROPPED = True
except:
    print("Could not drop the collections")


def populate_users():
    pass

def populate_books():

    books_list = [
        {
            TITLE_KEY: "How to Think Like a Computer Scientist: Interactive Edition",
            OFFERED_BY_KEY: "Runestone Academy",
            PROVIDER_LINK_KEY: "https://runestone.academy/runestone/default/user/login?_next=/runestone/default/index",
            ORIGINAL_DESCRIPTION_KEY: "This book is meant to provide you with an interactive experience as you learn to program in Python. You can read the text, watch videos, and write and execute Python code. In addition to simply executing code, there is a unique feature called 'codelens' that allows you to control the flow of execution in order to gain a better understanding of how the program works.",
            LINK_KEY: "https://runestone.academy/runestone/books/published/thinkcspy/index.html",
            TECH_STACK_KEY: ["Python"],
            FLAGS_KEY: ["Text-Based", "Interactive"],
            SAVED_KEY: False
        },
        {
            TITLE_KEY: "Algorithms and Data Structures using Python",
            OFFERED_BY_KEY: "Runestone Academy",
            PROVIDER_LINK_KEY: "https://runestone.academy/runestone/default/user/login?_next=/runestone/default/index",
            ORIGINAL_DESCRIPTION_KEY: "This book began as a paper book, first published by Franklin Beedle & Associates back in 2005. Written by Brad Miller and David Ranum. We are grateful for the vision of Jim Leisy who gave us permission to take our text and publish it online as an interactive textbook.",
            LINK_KEY: "https://runestone.academy/runestone/books/published/pythonds/index.html",
            TECH_STACK_KEY: ["Python"],
            FLAGS_KEY: ["Text-Based", "Interactive"],
            SAVED_KEY: False
        },
        {
            TITLE_KEY: "Algorithms and Data Structures using C++",
            OFFERED_BY_KEY: "Runestone Academy",
            PROVIDER_LINK_KEY: "https://runestone.academy/runestone/default/user/login?_next=/runestone/default/index",
            ORIGINAL_DESCRIPTION_KEY: "This book began as the paper book, Problem Solving with Algorithms and Data Structures Using Python, first published by Franklin Beedle & Associates written by Brad Miller and David Ranum back in 2005. It was translated to C++ by Jan Pearce and a team of excellent Berea College students in the summer of 2018. We are all grateful for the vision of Jim Leisy who gave permission to take the original Python version of this text and freely publish it online as an interactive textbook.",
            LINK_KEY: "https://runestone.academy/runestone/books/published/cppds/index.html",
            TECH_STACK_KEY: ["C++", "Python"],
            FLAGS_KEY: ["Text-Based", "Interactive"],
            SAVED_KEY: False
        },
        {
            TITLE_KEY: "Algorithms and Data Structures using C++",
            OFFERED_BY_KEY: "Runestone Academy",
            PROVIDER_LINK_KEY: "https://runestone.academy/runestone/default/user/login?_next=/runestone/default/index",
            ORIGINAL_DESCRIPTION_KEY: "This book began as the paper book, Problem Solving with Algorithms and Data Structures Using Python, first published by Franklin Beedle & Associates written by Brad Miller and David Ranum back in 2005. It was translated to C++ by Jan Pearce and a team of excellent Berea College students in the summer of 2018. We are all grateful for the vision of Jim Leisy who gave permission to take the original Python version of this text and freely publish it online as an interactive textbook.",
            LINK_KEY: "https://runestone.academy/runestone/books/published/cppds/index.html",
            TECH_STACK_KEY: ["C++", "Python"],
            FLAGS_KEY: ["Text-Based", "Interactive"],
            SAVED_KEY: False
        },
        {
            TITLE_KEY: "Algorithms and Data Structures using C++",
            OFFERED_BY_KEY: "Runestone Academy",
            PROVIDER_LINK_KEY: "https://runestone.academy/runestone/default/user/login?_next=/runestone/default/index",
            ORIGINAL_DESCRIPTION_KEY: "This book began as the paper book, Problem Solving with Algorithms and Data Structures Using Python, first published by Franklin Beedle & Associates written by Brad Miller and David Ranum back in 2005. It was translated to C++ by Jan Pearce and a team of excellent Berea College students in the summer of 2018. We are all grateful for the vision of Jim Leisy who gave permission to take the original Python version of this text and freely publish it online as an interactive textbook.",
            LINK_KEY: "https://runestone.academy/runestone/books/published/cppds/index.html",
            TECH_STACK_KEY: ["C++", "Python"],
            FLAGS_KEY: ["Text-Based", "Interactive"],
            SAVED_KEY: False
        }
    ]

    result = books.insert_many(books_list)

def populate_articles():
    articles_list = [
        {
            TITLE_KEY: "Express Tutorial: The Local Library website",
            OFFERED_BY_KEY: "Mozilla",
            PROVIDER_LINK_KEY: "https://developer.mozilla.org",
            ORIGINAL_DESCRIPTION_KEY: "The MDN 'Local Library' Express (Node) tutorial, in which we develop a website that might be used to manage the catalog for a local library.",
            LINK_KEY: "https://developer.mozilla.org/en-US/docs/Learn/Server-side/Express_Nodejs/Tutorial_local_library_website",
            TECH_STACK_KEY: ["JavaScript", "Node", "Express"],
            FLAGS_KEY: ["Text-Based", "Tutorial"],
            SAVED_KEY: False
        },
        {
            TITLE_KEY: "Express/Node introduction",
            OFFERED_BY_KEY: "Mozilla",
            PROVIDER_LINK_KEY: "https://developer.mozilla.org",
            ORIGINAL_DESCRIPTION_KEY: "In this Express article we answer the questions 'What is Node?' and 'What is Express?', and give you an overview of what makes the Express web framework special. We'll outline the main features, and show you some of the main building blocks of an Express application (although at this point you won't yet have a development environment in which to test it).",
            LINK_KEY: "https://developer.mozilla.org/en-US/docs/Learn/Server-side/Express_Nodejs/Introduction",
            TECH_STACK_KEY: ["Node", "Express"],
            FLAGS_KEY: ["Text-Based"],
            SAVED_KEY: False
        },
        {
            TITLE_KEY: "Setting up a Node development environment",
            OFFERED_BY_KEY: "Mozilla",
            PROVIDER_LINK_KEY: "https://developer.mozilla.org",
            ORIGINAL_DESCRIPTION_KEY: "We'll show you how to set up and test a Node/Express development environment on Windows, Linux (Ubuntu), and macOS. Whatever common operating system you are using, this article should give you what you need to be able to start developing Express apps.",
            LINK_KEY: "https://developer.mozilla.org/en-US/docs/Learn/Server-side/Express_Nodejs/development_environment",
            TECH_STACK_KEY: ["Node", "Express"],
            FLAGS_KEY: ["Text-Based"],
            SAVED_KEY: False
        }
    ]

    result = articles.insert_many(articles_list)

def populate_courses():
    courses_list = [
        {
            TITLE_KEY: "Express web framework (Node.js/JavaScript)",
            OFFERED_BY_KEY: "Mozilla",
            PROVIDER_LINK_KEY: "https://developer.mozilla.org",
            ORIGINAL_DESCRIPTION_KEY: "Express is a popular unopinionated web framework, written in JavaScript and hosted within the Node.js runtime environment. This module explains some of the key benefits of the framework, how to set up your development environment and how to perform common web development and deployment tasks.",
            LINK_KEY: "https://developer.mozilla.org/en-US/docs/Learn/Server-side/Express_Nodejs",
            TECH_STACK_KEY: ["JavaScript", "Node", "Express"],
            FLAGS_KEY: ["Text-Based"],
            SAVED_KEY: False
        },
        {
            TITLE_KEY: "Django Web Framework (Python)",
            OFFERED_BY_KEY: "Mozilla",
            PROVIDER_LINK_KEY: "https://developer.mozilla.org",
            ORIGINAL_DESCRIPTION_KEY: "Django is an extremely popular and fully featured server-side web framework, written in Python. This module shows you why Django is one of the most popular web server frameworks, how to set up a development environment, and how to start using it to create your own web applications.",
            LINK_KEY: "https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django",
            TECH_STACK_KEY: ["Python", "Django"],
            FLAGS_KEY: ["Text-Based"],
            SAVED_KEY: False
        },
        {
            TITLE_KEY: "Server-side website programming first steps",
            OFFERED_BY_KEY: "Mozilla",
            PROVIDER_LINK_KEY: "https://developer.mozilla.org",
            ORIGINAL_DESCRIPTION_KEY: "In this module we answer a few fundamental questions about server-side programming — 'What is it?', 'How does it differ from client-side programming?', and 'Why is it so useful?'. We then provide an overview of some of the most popular server-side web frameworks, along with guidance on how to select the most suitable framework for creating your first site. Finally, we provide a high-level introductory article about web server security.",
            LINK_KEY: "https://developer.mozilla.org/en-US/docs/Learn/Server-side/First_steps",
            TECH_STACK_KEY: ["Server-Side"],
            FLAGS_KEY: ["Text-Based"],
            SAVED_KEY: False
        }
    ]

    result = courses.insert_many(courses_list)

def populate_tracks():
    tracks_list = [
        {
            TITLE_KEY: "Server-side website programming",
            OFFERED_BY_KEY: "Mozilla",
            PROVIDER_LINK_KEY: "https://developer.mozilla.org",
            ORIGINAL_DESCRIPTION_KEY: """The Dynamic Websites – Server-side programming topic is a series of modules that show how to create dynamic websites; websites that deliver customised information in response to HTTP requests. The modules provide a general introduction to server-side programming, along with specific beginner-level guides on how to use the Django (Python) and Express (Node.js/JavaScript) web frameworks to create basic applications. 
                                            Most major websites use some kind of server-side technology to dynamically display data as required. For example, imagine how many products are available on Amazon, and imagine how many posts have been written on Facebook. Displaying all of these using different static pages would be extremely inefficient, so instead such sites display static templates (built using HTML, CSS, and JavaScript), and then dynamically update the data displayed inside those templates when needed, such as when you want to view a different product on Amazon. 
                                            In the modern world of web development, learning about server-side development is highly recommended.""",
            LINK_KEY: "https://developer.mozilla.org/en-US/docs/Learn/Server-side/First_steps",
            TECH_STACK_KEY: ["Server-Side", "Python", "Django", "JavaScript", "Node", "Express"],
            FLAGS_KEY: ["Text-Based"],
            SAVED_KEY: False
        }
    ]

    result = tracks.insert_many(tracks_list)

# populate the db with new data
if DROPPED:
    try:
        populate_books()
        print("Populated Books")
        populate_articles()
        print("Populated Articles")
        populate_courses()
        print("Populated Courses")
        populate_tracks()
        print("Populated Tracks")
    except:
        print("Could not populate the db")
