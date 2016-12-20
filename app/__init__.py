import os
import sys

from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

from config import config

app = Flask(__name__)
app.config.from_object(config['DEVELOPMENT'])

db = SQLAlchemy(app)

@app.errorhandler(404)
def not_found(error):
    return jsonify({'message' : 'Page not found'})

from app.auth.controller import auth as authModule
app.register_blueprint(authModule)
