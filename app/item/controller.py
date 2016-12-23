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
    print('index')
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
        if len(check_item) != 1:
            return jsonify({
                'message': 'That user already exists.'
            }), 400

        #add item to database
        item = Item(request.json['name'], request.json['cost'], request.json['descritpion'])
        db.session.add(item)
        db.session.commit()

        return jsonify({
            'message': 'Item added successfully.',
            'data': {
                'item': item.to_dict()
            }
        }), 201
    return jsonify({'message': 'There was an error adding data', 'error': form.errors}), 400

"""
## update
@itemMod.route('/update', methods='POST')
#@itemMod.route('/<int: itemId>', methods=['GET', 'PUT', 'DELETE'])
def update():
    print("update")
    pass

## get
@itemMod.route('/get', methods='GET')
def get():
    print('get')
    pass

## view
@itemMod.route('/view', methods='GET')
def view():
    print('view')
    pass

##delete item
@itemMod.route("/delete")
def delete():
    print("delete")
    pass
"""
