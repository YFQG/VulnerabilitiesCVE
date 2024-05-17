from flask import Flask
from pymongo import MongoClient

# Creating a Flask application instance
app = Flask(__name__)

# Importing routes module from the current package
from . import routes
