import os
import sys

from flask import Flask, jsonify, request, g

# extensions
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
import jwt
from flask_cors import CORS

# config
from config import config


app = Flask(__name__)
app.config.from_object(config['DEVELOPMENT'])

# initialize the extensions
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
CORS(app, supports_credentials=True)

# import models
from app.auth.models.User import User

# checks if request has auth token and if so adds user data to g.user
@app.before_request
def before_request():
    if 'Authorization' in request.headers:
        token = request.headers['Authorization'].split(' ')[1]
        try:
            payload = jwt.decode(token,app.config['SECRET_KEY'])

            user = User.query.get(payload['id'])

            g.user = user
        except (jwt.DecodeError, jwt.ExpiredSignatureError):
            return jsonify({'message' : 'Token is invalid'}), 401
    else:
        g.user = None



# error handlers
@app.errorhandler(500)
def error_sever(error):
    return jsonify({
        'status' : 'error',
        'message' : 'There was a server error',
        'errors' : {
            'server' : ['there was a server error']
        }
    })

@app.errorhandler(404)
def not_found(error):
    return jsonify({
        'status' : 'error',
        'message' : 'Page not found',
        'errors' : {
            'page' : ['page not found']
        }
    }), 404

@app.errorhandler(403)
def error_forbidden(error):
    return jsonify({
        'status' : 'error',
        'message' : 'You are not allowed',
        'errors' : {
            'user' : ['You are not allowed to use this.']
        }
    }), 403

@app.errorhandler(401)
def error_unauthorized(error):
    return jsonify({
        'status' : 'error',
        'message' : 'You must login first',
        'errors' : {
            'user' : ['You must login to use this route']
        }
    }), 401


# Import routes
from app.auth.controller import auth as authModule
from app.restaurant.controller import restaurantMod
from app.item.controller import itemMod
from app.bill.controller import billMod

app.register_blueprint(authModule)
app.register_blueprint(restaurantMod)
app.register_blueprint(billMod)
app.register_blueprint(itemMod)
