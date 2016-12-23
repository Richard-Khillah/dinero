from flask import Blueprint, request, g, redirect, url_for, jsonify
from datetime import datetime, timedelta
import pprint

from app import db
from app.item.models.Item import Item
from app.auth.models.User import User
from app.item.validators.ItemValidator import ItemValidator
#from app.auth.decorators import requires_login, requres_status_manager



itemMod = Blueprint('item', __name__, url_prefix='/item')

##index
@itemMod.route('/', methods=['GET'])
def index():
    return jsonify({
        'message': 'in index'
    }), 201
    pass


@itemMod.route('/add_item', methods=['POST'])
#@requires_login
#@requres_status_manager
def add_item():
    print("got into add_item()")
    form = ItemValidator(data=request.json)

    if form.validate():
        # Check whether item exists
        check_item = Item.query.filter(Item.name==request.json['name']).all()
        if len(check_item) != 0:
            return jsonify({
                'message': 'That item already exists.'
            }), 400

        #add item to database
        item = Item(request.json['name'], request.json['cost'], request.json['description'])
        db.session.add(item)
        db.session.commit()

        return jsonify({
            'message': 'Item added successfully.',
            'data': {
                'item': item.to_dict()
            }
        }), 201
    return jsonify({'message': 'There was an error adding data', 'error': form.errors}), 400


## view
@itemMod.route('/<string:itemName>')#, methods=['GET'])
def view(itemName):
    if itemName == "":
        return jsonify({
            'message': 'error',
            'error' : {
                'itemName': 'Must not be a null string argument'
            }
        }), 404

    item = Item.query.filter(Item.name == itemName).all()

    if not item:
        return jsonify({
            'message': 'Item was not found. Ensure you have the right spelling.',
            'error': {
                'itemName': 'No item: %r in database.' % itemName
            }
        }), 404
    item = item[0].to_dict()

    return jsonify({
        'message': 'Helooooo from inside view!',
        'data': {
            'item': item
        }
    }), 201


## update
@itemMod.route('/update', methods=['POST'])
#itemMod.route('/<int: itemId>', methods=['GET', 'PUT', 'DELETE'])
def update():
    return jsonify({
        'message': 'Yes! inside za update side \'o things'
    })

## get
@itemMod.route('/get', methods=['GET'])
def get():
    return jsonify({
        'message': 'Yup Yup! 1M/yr here we come!'
    })

##delete item
@itemMod.route("/delete")
def delete():
    return jsonify({
        'message': 'oh my my! we\'re deleting something??'
    })
