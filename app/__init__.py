import os
import sys

from flask import Flask, jsonify

# extensions
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

#config
from config import config

app = Flask(__name__)
app.config.from_object(config['DEVELOPMENT'])

# initialize the extensions
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

# error handlers
@app.errorhandler(404)
def not_found(error):
    return jsonify({'message' : 'Page not found'}), 404

@app.errorhandler(403)
def error_forbidden(error):
    return jsonify({'message' : 'You must login first'}), 403

# Import routes
from app.auth.controller import auth as authModule
from app.restaurant.controller import restaurantMod

app.register_blueprint(authModule)
app.register_blueprint(restaurantMod)
