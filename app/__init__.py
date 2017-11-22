# app/__init__.py

from flask import Flask

# Initialize the app
app = Flask(__name__, instance_relative_config=True)

# Load the views
from app import views
from app import process

# Load the config file
app.config.from_object('config')