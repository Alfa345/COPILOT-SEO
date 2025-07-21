# app/__init__.py

from dotenv import load_dotenv
load_dotenv() # Load variables from .env file FIRST

from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

from app import paths # This line must come AFTER app is created