from flask import Blueprint, request, g, redirect, url_for, jsonify



from app import db
from app.restaurant.models.Restaurant import Restaurant
from app.auth.models.User import User
from app.restaurant.validators.RestaurantValidator import RestaurantValidator
from app.auth import constants as USER

restaurantMod = Blueprint('restaurant', __name__, url_prefix='/restaurants')

## TODO: create auth validation on all routes

@restaurantMod.route('/', methods=['GET','POST'])
def index_restaurant():
    if request.method == 'GET':
        # TODO: check if user is admin

        # TODO: check if user is owner
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

        restaurant_query = Restaurant.query.paginate(page,25,False)

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
            print(request.json['restaurant_number'])
        except:
            return jsonify({
                'status' : 'error',
                'errors' : [
                    'Restaurant number must be a positive integer.'
                ],
                'message' : 'There was a problem making the request.'
            })

        try:
            request.json['owner_id'] = int(request.json['owner_id'])
        except:
            return jsonify({
                'status' : 'error',
                'errors' : [
                    'Owner id must be a positive integer.'
                ],
                'message' : 'There was a problem making the request.'
            })

        form = RestaurantValidator(data=request.json)

        if form.validate():

            # todo get user from the token
            user = User.query.filter(User.id==request.json['owner_id']).all()

            if len(user) != 1:
                return jsonify({
                    'error' : 'Owner does not exist.',
                    'message' : 'There was an error'
                }), 400

            user = user[0]

            restaurant = Restaurant(user, request.json['name'], request.json['restaurant_number'], request.json['address'])
            #user.role = USER.OWNER

            db.session.add(restaurant)
            db.session.commit()

            return jsonify({
                'message' : 'Restaurant successfully added',
                'data' : {
                    'restaurant' : restaurant.to_dict()
                }
            }), 201

        return jsonify({
            'message' : 'There is missing data',
            'errors' : form.errors
        }), 400

## view
## update
## delete
@restaurantMod.route('/<int:restaurantId>', methods=['GET', 'PUT', 'DELETE'])
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

    if len(restaurants) is not 1:
        return jsonify({
        'message' : 'Restaurant cannot be found',
        'errors' : {
        'restaurant' : 'No restaurant with id of %d' % restaurantId
        }
        }), 404

    if request.method == 'GET':
        restaurant = restaurants[0].to_dict()
        restaurant['owner'] = restaurants[0].owner.to_dict()

        return jsonify({
            'status' : 'success',
            'message' : 'restaurant found',
            'data' : {
                'restaurant' : restaurant
            }
        })
    if request.method == 'DELETE':
        # TODO: check if user is owner or admin
        try:
            db.session.delete(restaurants[0])
            db.session.commit()
        except:
            return jsonify({
                'status' : 'error',
                'message' : 'There was a problem deleteing the restaurant',
                'errors' : {
                    'restaurant' : ['There was a problem deleteing the restaurant with id of %d' % restaurantId]
                }
            })

        return jsonify({
            'status' : 'success',
            'message' : 'The restaurant with id of %d was deleted.' % restaurantId
        }), 200
