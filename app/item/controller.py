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

            return jsonify(
                'Item added successfully.',
                { 'item': item.to_dict()
            }), 201
        return jsonify({'message': 'There was an error adding data', 'error': form.errors}), 400

@itemMod.route('/<string:itemName>', methods=['GET', 'PUT', 'DELETE'])
def update(itemName):
    #get the Item.


    # view a single Item
    if request.method == 'GET':
        item = get(itemName)
        print(item)
        if not item:
            return jsonify('%r not found in database.' % itemName)
        item = a_dict(item)
        return jsonify({
            'item': item
        })

    # update a single Item
    if request.method == 'PUT':
        pass

    # delete a single item
    if request.method == 'DELETE':
        item = get(itemName)
        print(item)
        if not item:
            return jsonify('%r not found in database.' % itemName)
        try:
            #item = a_dict(item)
            db.session.delete(item)
            db.session.commit()
            return jsonify('%r deleted from the database.' % itemName)
        except:
            return jsonify(item)

## helper function
def get(itemName):
    """
    if itemName == "":
        return jsonify('error: itemName must not be a null string argument'), 404
    """
    item = Item.query.filter_by(name=itemName).first()
    if not item:
        return False
    #item = item[0].to_dict()
    return item

def a_dict(item):
    return item[0].to_dict()

    """
    return jsonify({
        'message': 'inside view!',
        'item': item
    }), 201
    """
