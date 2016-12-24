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
@itemMod.route('/', methods=['GET', 'POST'])
def index():
    #index page
    if request.method == 'GET':
        return jsonify({
            'message': 'in index'
        }), 201

    # add item to database
    if request.method == 'POST':
        print("got into add_item()")
        # validate the inputted information.
        form = ItemValidator(data=request.json)
        if form.validate():
            # Check whether item exists
            name = request.json['name']
            check_item = get(name)
            if check_item:
                return jsonify(
                    '%r already exists in your system.' % name,
                    {'item': a_dict(check_item)}
                    ), 400
            #add item to database
            item = Item(request.json['name'], request.json['cost'], request.json['description'])
            db.session.add(item)
            db.session.commit()
            return jsonify(
                'Item added successfully.',
                { 'added item': item.to_dict()
            }), 201
        return jsonify({'message': 'There was an error adding data', 'error': form.errors}), 400

@itemMod.route('/<string:itemName>', methods=['GET', 'PUT', 'DELETE'])
def update(itemName):
    # Query all items in the database and return.
    if itemName == 'all':
        items = Item.query.all()
        return jsonify([a_dict(item) for item in items]), 200

    # retrieve and verify the existence of the Item from the database
    item = get(itemName)
    print(item)
    if not item:
        return jsonify('%r not found in database.' % itemName), 400

    # view a single Item
    if request.method == 'GET':
        item = a_dict(item)
        return jsonify({
            'item': item
        }), 200

    # update a single Item
    if request.method == 'PUT':
        try:
            item.name = request.json.get('name', item.name)
            item.cost = request.json.get('cost', item.cost)
            item.description = request.json.get('description', item.description)
            db.session.commit()
            item = a_dict(item)
            return jsonify({'updated item':item}), 200
        except:
            return jsonify('error occured when updating ', item), 400

    # delete a single item
    if request.method == 'DELETE':
        try:
            db.session.delete(item)
            db.session.commit()
            return jsonify('%r deleted from the database.' % itemName), 200
        except:
            return jsonify('error deleting %r from the database' % itemName,
                            item), 400

## helper functions
# Query itemName and return the item to the caller.
# if an item with `itemName` is not found in the database, return False
def get(itemName):
    item = Item.query.filter_by(name=itemName).first()
    if not item:
        return False
    return item

# Serialize the information passed in as item.
def a_dict(item):
    return item.to_dict()
