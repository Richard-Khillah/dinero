from flask import Blueprint, request, g, redirect, url_for, jsonify
import jwt
from datetime import datetime, timedelta

from app import app, db
from app.auth.models.Customer import Customer
from app.auth.decorators import requires_login
from app.auth.validators.CustomerValidator import CustomerValidator

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

    customers = Customer.query.all()

    customers_dicts = []

    # convert all customers to dictionaries
    for customer in customers:
        customers_dicts.append(customer.to_dict())

    return jsonify({'message': 'done', 'data': {'customers': customers_dicts}})


@auth.route('/login', methods=['POST'])
def login():

    if not 'email' in request.json or not 'password' in request.json :
        return jsonify({
            'message' : 'Missing email or password'
        }), 400

    customer = Customer.query.filter(Customer.email==request.json['email']).all()

    if len(customer) is 0:
        return jsonify({
            'message' : 'Email or password incorrect.'
        }), 401

    if customer[0].check_password(request.json['password']):
        payload = {
            'id' : customer[0].id,
            'username' : customer[0].username,
            'email' : customer[0].email,
            'exp' : datetime.utcnow() + timedelta(days=99999)
        }

        # create a jwt token for user
        token = jwt.encode(payload, app.config['SECRET_KEY'])

        return jsonify({
            'message' : 'successfully logged in.',
            'data' : {
                'customer' : customer[0].to_dict(),
                'token' : token
            }
        })


    return jsonify({
        'message' : 'Email or password incorrect.'
    }), 401

#router is /auth/register
@auth.route('/register', methods=['POST'])
def register():
    print(request)
    # pass data to validator
    form = CustomerValidator(data=request.json)

    # ensure lowercase
    if 'email' in request.json:
        request.json['email'] = request.json['email'].lower()
    if 'username' in request.json:
        request.json['username'] = request.json['username'].lower()

    if not 'email' in request.json or not 'username' in request.json:
        return jsonify({'message' : 'Missing username or email'}), 400

    # check if user exists
    customers = Customer.query.filter(Customer.email==request.json['email']).all()
    customers += Customer.query.filter(Customer.username==request.json['username']).all()


    if len(customers) != 0:
        return jsonify({
            'message': 'That user already exists'
        }), 400


    if form.validate():
        # add customer to database
        customer = Customer(request.json['name'],request.json['username'],request.json['email'],request.json['password'])
        db.session.add(customer)
        db.session.commit()

        payload = {
            'id' : customer.id,
            'username' : customer.username,
            'email' : customer.email,
            'exp' : datetime.utcnow() + timedelta(days=99999)
        }

        # create a jwt token for user
        token = jwt.encode(payload, app.config['SECRET_KEY'])
        print(token)

        return jsonify({'message' : 'Account created successfully.', 'customer' : customer.to_dict(), 'token' : token.decode('utf-8)')}), 201


    return jsonify({'message' : 'There is missing data', 'errors' : form.errors}), 400
