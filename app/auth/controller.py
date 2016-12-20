from flask import Blueprint, request, g, redirect, url_for, jsonify
from werkzeug import check_password_hash, generate_password_hash

from app import db
from app.auth.models.User import User
from app.auth.decorators import requires_login


auth = Blueprint('auth', __name__, url_prefix='/auth')

# This is middleware that happens before the route controller is executed
# a user makes a request -> before_request(request) -> to specif route -> response
@auth.before_request
def before_request():
    g.user = {
        'name' : 'test',
        'username' : 'testing'
    }

@auth.route('/me/')
def home():
    print(g.get('user', None))
    return jsonify({'user' : 'test'})

@auth.route('/')
def index():
    user = User.query.get(1)
    print(user.toDict())
    print(request.headers)
    return jsonify({'message': 'done', 'user': user.toDict()})

@auth.route('/register/', methods=['GET', 'POST'])
def register():
    print(request)
    user = User(name='Test',email='test@test.com', password=generate_password_hash('password'))
    db.session.add(user)
    db.session.commit()
    print(user)

    return jsonify({'form' : request.form, 'json' : request.json})
