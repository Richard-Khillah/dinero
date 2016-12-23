from flask import Blueprint, request, g, redirect, url_for, jsonify
from datetime import datetime, timedelta
import pprint

from app import db
from app.auth.models.User import User
from app.auth.decorators import requires_login, requres_status_manager
from app.item.validators.ItemValidator import ItemValidator
from app.item.models.Item import Item

itembp = Blueprint('item', __name__, url_prefix='/item')

##index
@itembp.route('/', methods=['GET'])
def index():
    print('index')
    pass


@itembp.route('/add_item', methods=['POST'])
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

## update
@itembp.route('/update', method='POST')
def update():
    print('update')
    pass

## get
@itembp.route('/get', method='GET')
def get():
    print('get')
    pass

## view
@itembp.route('/view', method='GET')
def view():
    print('view')
    pass

##delete item
@itembp.route('/delete')
def delete():
    print('delete')
    pass
