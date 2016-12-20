from flask import Blueprint, request, g, redirect, url_for, jsonify
from werkzeug import check_password_hash, generate_password_hash

from app import db
from app.auth.models.User import User



auth = Blueprint('auth', __name__, url_prefix='/auth')

@auth.route('/me/')
def home():
    return jsonify({'user' : 'test'})

@auth.route('/')
def index():
    user = User.query.get(1)
    print(user.toDict())

    return jsonify({'message': 'done', 'user': user.toDict()})

@auth.route('/register/', methods=['GET', 'POST'])
def register():
    print(request)
    user = User(name='Test',email='test@test.com', password=generate_password_hash('password'))
    db.session.add(user)
    db.session.commit()
    print(user)

    return jsonify({'form' : request.form, 'json' : request.json})
