from flask import Blueprint, request, g, redirect, url_for, jsonify



from app import db
from app.restaurant.models.Restaurant import Restaurant
#from models import Restaurant
from app.auth.models.User import User
from app.restaurant.validators.RestaurantValidator import RestaurantValidator

#from validators.RestaurantValidator import RestaurantValidator

from app.auth import constants as USER
from app.auth.decorators import requires_login


restaurantMod = Blueprint('restaurant', __name__, url_prefix='/restaurants')

## TODO: create auth validation on all routes

## create
#@restaurantMod.route('/create_restaurant', methods=['POST'])
@restaurantMod.route('/', methods=['GET','POST'])
@requires_login
def index_restaurant():
    if request.method == 'GET':
        page = None
        # check if user supplied a page number in query
        if request.args.get('page', ''):
            page = request.args.get('page', '')

            # check if page is a number
            try:
                page = int(page)
            except ValueError:
                page = 1

            if page < 0:
                page = 1
        else:
            page = 1

        restaurant_query = None

        if g.user.role == USER.ADMIN:
            restaurant_query = Restaurant.query.paginate(page,25,False)
        elif g.user.role == USER.OWNER:
            restaurant_query = Restaurant.query.join(Restaurant.owner, aliased=True).filter(User.id==g.user.id).paginate(page, 25,False)
        else:
            return jsonify({
                'status' : 'error',
                'message': 'You are not allowed.',
                'errors' : {
                    'user' : 'Not authorized'
                }
            }), 403

        restaurants = []

        for res in restaurant_query.items:
            restaurant = res.to_dict()
            restaurant['owner'] = res.owner.to_dict()

            restaurants.append(restaurant)

        return jsonify({
            'status' : 'success',
            'meta' : {
                'page' : restaurant_query.page,
                'pages' : restaurant_query.pages,
                'total' : restaurant_query.total
            },
            'data' : {
                'restaurants' : restaurants
            }
        })

    else: # POST request
        try:
            request.json["restaurant_number"] = int(request.json["restaurant_number"])
        except:
            return jsonify({
                'status' : 'error',
                'errors' : [
                    'Restaurant number must be a positive integer.'
                ],
                'message' : 'There was a problem making the request.'
            }), 400

        request.json['owner_id'] = g.user.id

        form = RestaurantValidator(data=request.json)

        if form.validate():
            user = g.user

            # get all restaurants with same name
            restaurants = Restaurant.query.filter(Restaurant.name == request.json['name']).all()

            errors = {}


            for restaurant in restaurants:
                if restaurant.address == request.json['address']:
                    errors['address'] = ['Address is already taken for this restaurant name']
                if restaurant.restaurant_number == request.json['restaurant_number']:
                    errors['restaurant_number'] = ['Restaurant number is already taken for this restaurant name']

            if errors:
                return jsonify({
                    'status' : 'error',
                    'message' : 'There was a problem adding the restaurant',
                    'errors' : errors
                }), 400


            restaurant = Restaurant(user, request.json['name'], request.json['restaurant_number'], request.json['address'])
            user.role = USER.OWNER

            try:
                db.session.add(restaurant)
                db.session.commit()
            except:
                db.session.rollback()

                return jsonify({
                    'status' : 'error',
                    'message' : 'There was a problem adding the restaurant',
                    'errors' : {
                        'server' : 'There was a server error'
                    }
                }), 500


            return jsonify({
                'status' : 'success',
                'message' : 'Restaurant successfully added',
                'data' : {
                    'restaurant' : restaurant.to_dict()
                }
            }), 201

        # if there were form errors
        return jsonify({
            'message' : 'There is missing data',
            'errors' : form.errors
        }), 400


@restaurantMod.route('/<int:restaurantId>', methods=['GET', 'PUT', 'DELETE'])
@requires_login
def restaurant_view(restaurantId):
    # Happens for every request on this route
    if restaurantId < 1:
        return jsonify({
        'message' : 'There was an error',
        'errors' : {
        'restaurantId' : 'Must be greater than 0'
        }
        }), 404

    restaurants = Restaurant.query.filter(Restaurant.id == restaurantId).all()


    is_owner = restaurants[0].owner.id == g.user.id
    is_admin = g.user.get_role() == 'admin'

    if not restaurants:
        return jsonify({
        'message' : 'Restaurant cannot be found',
        'errors' : {
        'restaurant' : 'No restaurant with id of %d' % restaurantId
        }
        }), 404

    if request.method == 'GET': # single view
        restaurant = restaurants[0].to_dict()
        restaurant['owner'] = restaurants[0].owner.to_dict()

        return jsonify({
            'status' : 'success',
            'message' : 'restaurant found',
            'data' : {
                'restaurant' : restaurant
            }
        })
    if request.method == 'DELETE': # single delete
        if not is_owner and not is_admin:
            return jsonify({
                'status' : 'error',
                'message' : 'You are not allowed',
                'errors' : {
                    'user' : 'Not allowed'
                }
            }), 403


        try:
            db.session.delete(restaurants[0])
            db.session.commit()
        except:
            db.session.rollback()
            return jsonify({
                'status' : 'error',
                'message' : 'There was a problem deleteing the restaurant',
                'errors' : {
                    'restaurant' : ['There was a problem deleteing the restaurant with id of %d' % restaurantId]
                }
            }), 500

        return jsonify({
            'status' : 'success',
            'message' : 'The restaurant with id of %d was deleted.' % restaurantId
        }), 200

    else: # single update
        if not is_owner and not is_admin:
            return jsonify({
                'status' : 'error',
                'message' : 'You are not allowed',
                'errors' : {
                    'user' : 'Not allowed'
                }
            }), 403

        try:
            request.json["restaurant_number"] = int(request.json["restaurant_number"])
        except:
            return jsonify({
                'status' : 'error',
                'errors' : [
                    'Restaurant number must be a positive integer.'
                ],
                'message' : 'There was a problem making the request.'
            }), 400

        request.json['owner_id'] = g.user['id']

        form = RestaurantValidator(data=request.json)

        if form.validate():
            restaurant = restaurants[0]

            # get all restaurants with same name
            restaurants = Restaurant.query.filter(Restaurant.name == request.json['name']).all()


            errors = {}

            for rest in restaurants:
                if rest.address == request.json['address']:
                    errors['address'] = ['Address is already taken for this restaurant name']
                if rest.restaurant_number == request.json['restaurant_number']:
                    errors['restaurant_number'] = ['Restaurant number is already taken for this restaurant name']

            if errors:
                return jsonify({
                    'status' : 'error',
                    'message' : 'There was a problem adding the restaurant',
                    'errors' : errors
                }), 400


            restaurant.name = request.json['name']
            restaurant.restaurant_number = request.json['restaurant_number']
            restaurant.address = request.json['address']

            # save the restaurant updates
            try:
                db.session.commit()
            except:
                db.session.rollback()

                return jsonify({
                    'status' : 'error',
                    'message' : 'There was a problem adding the restaurant',
                    'errors' : {
                        'server' : 'There was a server error'
                    }
                }), 500


            return jsonify({
                'status' : 'sucess',
                'message' : 'Restaurant successfully updated',
                'data' : {
                    'restaurant' : restaurant.to_dict()
                }
            })


        return jsonify({
            'status' : 'error',
            'message' : 'There were problems with the request',
            'errors' : form.errors
        }), 400
