from flask import Blueprint, request, g, redirect, url_for, jsonify
import jwt
from datetime import datetime, timedelta

from app import app, db
from app.auth.models.User import User
from app.auth.decorators import requires_login
from app.auth.validators.UserValidator import UserValidator

auth = Blueprint('auth', __name__, url_prefix='/auth')


# This is middleware that happens before the route controller is executed
# a user makes a request -> before_request(request) -> to specif route -> response
@auth.before_request
def before_request():
    if 'Authorization' in request.headers:
        token = request.headers['Authorization'].split(' ')[1]

        try:
            g.user = jwt.decode(token,app.config['SECRET_KEY'])
        except (jwt.DecodeError, jwt.ExpiredSignatureError):
            return jsonify({'message' : 'Token is invalid'}), 401
    else:
        g.user = None


@auth.route('/')
@requires_login
def index():

    users = User.query.all()

    users_dicts = []

    # convert all users to dictionaries
    for user in users:
        users_dicts.append(user.to_dict())

    return jsonify({'message': 'done', 'data': {'users': users_dicts}})


@auth.route('/login', methods=['POST'])
def login():

    if not 'email' in request.json or not 'password' in request.json :
        return jsonify({
            'message' : 'Missing email or password'
        }), 400

    user = User.query.filter(User.email==request.json['email']).order_by(User.id).all()

    console.log(user)

    if len(user) is 0:
        return jsonify({
            'message' : 'Email or password incorrect.'
        }), 401

    if user[0].check_password(request.json['password']):
        payload = {
            'id' : user[0].id,
            'username' : user[0].username,
            'email' : user[0].email,
            'exp' : datetime.utcnow() + timedelta(days=99999)
        }

        # create a jwt token for user
        token = jwt.encode(payload, app.config['SECRET_KEY'])

        return jsonify({
            'message' : 'successfully logged in.',
            'data' : {
                'user' : user[0].to_dict(),
                'token' : token.decode('utf-8')
            }
        })


    return jsonify({
        'message' : 'Email or password incorrect.'
    }), 401

#router is /auth/register
@auth.route('/register', methods=['POST'])
def register():
    # pass data to validator
    form = UserValidator(data=request.json)


    if form.validate():
        # ensure lowercase
        request.json['email'] = request.json['email'].lower()
        request.json['username'] = request.json['username'].lower()


        # check if user exists
        users = User.query.order_by(User.id).filter(User.email==request.json['email']).all()
        users += User.query.order_by(User.id).filter(User.username==request.json['username']).all()


        if len(users) != 0:
            return jsonify({
                'message': 'That user already exists'
            }), 400


        # add user to database
        user = User(request.json['name'],request.json['username'],request.json['email'],request.json['password'])
        db.session.add(user)
        db.session.commit()

        payload = {
            'id' : user.id,
            'username' : user.username,
            'email' : user.email,
            'exp' : datetime.utcnow() + timedelta(days=99999)
        }

        # create a jwt token for user
        token = jwt.encode(payload, app.config['SECRET_KEY'])

        return jsonify({'message' : 'Account created successfully.', 'user' : user.to_dict(), 'token' : token.decode('utf-8')}), 201


    return jsonify({'message' : 'There is missing data', 'errors' : form.errors}), 400
