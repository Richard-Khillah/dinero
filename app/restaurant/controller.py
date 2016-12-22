from flask import Blueprint, request, g, redirect, url_for, jsonify



from app import db
from app.restaurant.models.Restaurant import Restaurant
from app.auth.models.User import User
from app.restaurant.validators.RestaurantValidator import RestaurantValidator

restaurantMod = Blueprint('restaurant', __name__, url_prefix='/restaurant')

## index


## create
@restaurantMod.route('/', methods=['POST'])
def create_restaurant():
    form = RestaurantValidator(data=request.json)

    if form.validate():

        user = User.query.filter(User.id==request.json['owner_id']).all()

        if len(user) != 1:
            return jsonify({
                'error' : 'Owner does not exist.',
                'message' : 'There was an error'
            }), 400

        restaurant = Restaurant(user, request.json['name'], request.json['restaurant_number'], request.json['address'])

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
    })


## view


## update


## delete
