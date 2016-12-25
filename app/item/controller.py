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
        # Query all items in the database and return.
        items = get('all_items')
        return jsonify({
            'status': 'success',
            'data': [repr(item) for item in items]
        }), 200

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
                return jsonify({
                    'status': 'error',
                    'message': '%r already exists in your system.' % name,
                    'data': {
                        'item in database': a_dict(check_item)
                    }
                }), 400

            #add item to database
            try:
                item = Item(request.json['name'], request.json['cost'], request.json['description'])
                db.session.add(item)
                db.session.commit()
                return jsonify({
                    'status': 'success',
                    'message': 'item added successfully.',
                    'data': {
                        'added item': item.to_dict()
                    }
                }), 201
            except:
                return jsonify({
                    'status': 'error',
                    'message': 'there was an error adding the item',
                    'error': {
                        'key': ['errors here']
                    }
                }), 400
        return jsonify({
            'status': 'error',
            'message': 'there was an error with form validation',
            'error': form.errors
        }), 400

@itemMod.route('/<int:itemId>', methods=['GET', 'PUT', 'DELETE'])
def update(itemId):
    # retrieve and verify the existence of the Item from the database
    item = get(itemId)
    print(item)
    if not item:
        return jsonify({
            'status': 'error',
            'message': 'item %d not found in database.' % itemId
        }), 400

    # view a single Item
    if request.method == 'GET':
        item = a_dict(item)
        return jsonify({
            'status': 'success',
            'message': 'found item successfully',
            'data': {
                'item': item
            }
        }), 200

    # update a single Item
    if request.method == 'PUT':
        form = ItemValidator(data=request.json)
        if form.validate():
            # create a new Item() and verify that the update is indeed an update
            # an not a duplication of an item already in the database.
            # if the item item being updated in the database is indeed an attempt
            # to duplicate, reroute user to update form, displying current item
            # at the top of the page.
            updated_item_exists = get(request.json['name'])
            name = request.json['name']
            cost = request.json['cost']
            description = request.json['description']

            if not exists(id=itemId, name=name, cost=cost, description=description):
            #if not updated_item_exists:
                try:
                    item.name = request.json.get('name', item.name)
                    item.cost = request.json.get('cost', item.cost)
                    item.description = request.json.get('description', item.description)
                    db.session.commit()
                    item = a_dict(item)
                    return jsonify({
                        'status': 'success',
                        'message': 'updated item',
                        'data': item
                    }), 200
                except:
                    return jsonify({
                        'status': 'error',
                        'messge': 'error occured when updating item',
                        'error': {
                            'key': ['errors']
                        }
                    }), 400
            else:
                return jsonify({
                    'status': 'error',
                    'message': 'Similar Items seem to exist'
                })
        return jsonify({
            'status': 'error',
            'message': 'there was an error with form validation',
            'error': form.errors
        }), 400

    # delete a single item
    if request.method == 'DELETE':
        try:
            db.session.delete(item)
            db.session.commit()
            return jsonify({
                'status': 'success',
                'message': '%d deleted from the database.' % itemId,
            }), 200
        except:
            return jsonify({
                'status': 'error',
                'message': '%r not deleted.',
                'errors': {
                    'key': ['errors here']
                }
            }), 400

## helper functions
# Query itemId and return the item to the caller.
# if an item with `itemId` is not found in the database, return False
def get(arg):
    if arg == 'all_items':
        item = Item.query.all()
        #print(item)
    elif type(arg) is str:
        item = Item.query.filter_by(name=arg).first()
    elif type(arg) is int:
        item = Item.query.filter_by(id=arg).first()
    if not item:
        return False
    return item

# Serialize the information passed in as item.
def a_dict(item):
    return item.to_dict()

def exists(**kwargs):
    #item = Item.query.filter_by(**kwargs)
    kid = kwargs['id']
    kname = kwargs['name']
    kcost = kwargs['cost']
    kdescription = kwargs['description']

    # query all items with the same name.
    items = Item.query.filter_by(name=kname).all()
    for item in items:
        item = a_dict(item)
        if not item['id'] == kid:
        # look for items with the same name and description
            if item['description'] == kdescription:
                return True
    return False
