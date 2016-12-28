from flask import Blueprint, request, g, redirect, url_for, jsonify
#from datetime import datetime, timedelta

from app import db
from app.item.models.Item import Item
from app.auth.models.User import User
from app.item.validators.ItemValidator import ItemValidator
#from app.auth.decorators import requires_login, requres_status_manager

from app.auth import constants as USER
from app.auth.decorators import requires_login

from app.item.testFuncs import addTestItems

itemMod = Blueprint('item', __name__, url_prefix='/item')
dbs = db.session

#TODO Test items:
        #rollback, duplicate items, user authentication
#TODO Create Documentation

##index
@itemMod.route('/<string:command>', methods=['GET', 'POST'])
@requires_login
def index(command):
    # authorized status based on login informatoin
    authorizedUser = g.user.role >= USER.MANAGER


    #index page
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

        ##Algorithm for user login.
        """
        # Query all items in the database and return.
        if authorizedUser:
            items = get('all_items')
            return jsonify({
                'status': 'success',
                # Return allavailable information about all items
                'data': [repr(item) for item in items]
            }), 200
        else:
            items = get('all_items')
            return jsonify({
                'status': 'success',
                #return only `menu style` information
                'data': [str(item) for item in items]
            }), 200
        """
        # Query all items in the database and return.
        if command == 'test':
            items = get('all_items')
            return jsonify({
                'status': 'success',
                # Return allavailable information about all items
                'data': [repr(item) for item in items]
            }), 200
        elif command == 'cust':
            items = get('all_items')
            return jsonify({
                'status': 'success',
                #return only `menu style` information
                'data': [str(item) for item in items]
            }), 200

    # add item to database
    if request.method == 'POST':
        print("got into add_item()")
        if authorizedUser:
            if command == 'test':
                addTestItems()

                items = get('all_items')
                return jsonify({
                    'status': 'success',
                    'data': [str(item) for item in items]
                }), 200
            elif command == 'normal':

                # validate the inputted information.
                form = ItemValidator(data=request.json)
                if form.validate():
                    # Check whether item exists
                    name = request.json['name']
                    cost = request.json['cost']
                    description = request.json['description']
                    category = request.json['category']

                    found_items = items_with_same(name, description, cost)#, itemId)
                    if not any(found_items):
                        #add item to database
                        try:
                            item = Item(request.json['name'], request.json['cost'], request.json['description'], request.json['category'])
                            dbs.add(item)
                            dbs.commit()
                            print("got to after commit")
                            return jsonify({
                                'status': 'success',
                                'message': 'item added successfully.',
                                'data': {
                                    'added item': serialize(item)
                                }
                            }), 201
                        except:
                            dbs.rollback()
                            return jsonify({
                                'status': 'error',
                                'message': 'there was an error adding the item',
                                'error': {
                                    'key': ['errors here']
                                }
                            }), 400

                    else:
                        message, duplicate_item, same_named_items, same_descriptioned_items = construct_return_package(found_items)

                        return jsonify({
                            'status': 'error',
                            'message': message,
                            'data': {
                                'duplicate items': serialize_found(duplicate_item),
                                'items with same': {
                                    'name': serialize_found(same_named_items),
                                    'description': serialize_found(same_descriptioned_items)
                                }
                            }
                        }), 400
                    return jsonify({
                    'status': 'error',
                    'message': 'there was an error with form validation',
                    'error': form.errors
                    }), 400
        else:
            return jsonify({
                'status': 'error',
                'message': 'You are not authorized to update items.',
                'error': 'Forbidden Access'
            })

@itemMod.route('/<int:itemId>', methods=['GET', 'PUT', 'DELETE'])
def update(itemId):
    # authorized status based on login informatoin
    authorizedUser = g.user.role >= USER.MANAGER

    # retrieve and verify the existence of the Item from the database
    if itemId:
        item = get(itemId)
        if not item:
            return jsonify({
                'status': 'error',
                'message': 'item %d not found in database.' % itemId
            }), 400

    # view a single Item
    if request.method == 'GET':
        item = serialize(item)
        return jsonify({
            'status': 'success',
            'message': 'found item successfully',
            'data': {
                'item': item
            }
        }), 200

    # update a single Item
    if request.method == 'PUT':
        if authorizedUser:
            form = ItemValidator(data=request.json)
            if form.validate():
                name = request.json['name']
                cost = request.json['cost']
                description = request.json['description']

                found_items = items_with_same(name, description, cost, itemId)
                print(found_items)
                # If no items were found in the database containing the same
                # description and/or name, then update the item accordingly.
                # Otherwise, keep the Item intact as is, i.e. do not modify Item
                #TODO add any()
                if not any(found_items):
                    try:
                        item.name = name
                        item.cost = cost
                        item.description = description
                        dbs.commit()
                        item = serialize(item)

                        return jsonify({
                            'status': 'success',
                            'message': 'updated item',
                            'data': item
                        }), 200
                    except:
                        dbs.rollback()
                        return jsonify({
                            'status': 'error',
                            'message': 'error occured when updating item',
                            'error': {
                                'key': ['errors']
                            }
                        }), 400
                else:
                    # Item is potentially duplicating an item that already
                    # exists in the database.
                    message, duplicate_item, same_named_items, same_descriptioned_items = construct_return_package(found_items)

                    return jsonify({
                        'status': 'error',
                        'message': message,
                        'data': {
                            'duplicate items': serialize_found(duplicate_item),
                            'items with same': {
                                'name': serialize_found(same_named_items),
                                'description': serialize_found(same_descriptioned_items)
                            }
                        }
                    }), 400
            return jsonify({
                'status': 'error',
                'message': 'there was an error with form validation',
                'error': form.errors
            }), 400
        else:
            return jsonify({
                'status': 'error',
                'message': 'You are not authorized to update information',
                'error': 'Forbidden Access'
            })

    # delete a single item
    if request.method == 'DELETE':
        if authorizedUser:
            if itemId == 0:
                try:
                    numDeleted = Item.query.delete()
                    dbs.commit()
                    return jsonify({
                        'status': 'success',
                        'message': '%d items successfully removed from the data base.' % numDeleted,
                    }), 202
                except:
                    dbs.rollback()
                    return jsonify({
                        'status': 'error',
                        'message': 'there was an error deleting all items from the data base'
                    }), 500

            try:
                dbs.delete(item)
                dbs.commit()
                return jsonify({
                    'status': 'success',
                    'message': '%d deleted from the database.' % itemId,
                }), 200
            except:
                dbs.rollback()
                return jsonify({
                    'status': 'error',
                    'message': '%r not deleted.',
                    'errors': {
                        'key': ['errors here']
                    }
                }), 400
        else:
            return jsonify({
                'status': 'error',
                'message': 'You are not authorized to update information',
                'error': 'Forbidden Access'
            })

## helper functions
# Query itemId and return the item to the caller.
# if an item with `itemId` is not found in the database, return False
def get(arg):
    if arg == 'all_items':
        item = Item.query.all()
    elif type(arg) is str:
        item = Item.query.filter_by(name=arg).first()
    elif type(arg) is int:
        item = Item.query.filter_by(id=arg).first()
    if not item:
        return False
    return item

# Wrapper for .to_dict() from Items
def serialize(item):
    return item.to_dict()

#TODO move this to front end?
def items_with_same(name, description, cost, *iid):
    print("enter items_with_same()")
    count = 0 # Number of potential duplicates

    #TODO rename variables
    same_name_item_list = Item.query.filter_by(name=name).all()
    same_desc_item_list = Item.query.filter_by(description=description).all()
    all_items = same_name_item_list + same_desc_item_list

    duplicate_item = {}
    same_name_dict = {} # empty dictionary to add any item that might be duplicates
    same_description_dict = {}
    if iid:
        id = iid[0]
        mapped_ids = []
        for item in all_items:
            item_id = item.id
            if not item_id == id:
                # items should be unique
                if item.id not in mapped_ids:
                    equals = item.name == name and item.cost == cost and item.description == description

                    if equals:
                        count += 1
                        duplicate_item[count] = serialize(item)
                    elif item.name == name:
                        count += 1
                        same_name_dict[count] = serialize(item)
                    else:
                        count += 1
                        same_description_dict[count] = serialize(item)
                    mapped_ids.append(item.id)

    #return both lists to the caller.
    return duplicate_item, same_name_dict, same_description_dict
    #TODO update 'PUT' found_items
    #TODO ensureif not any() still operates accurately

def serialize_found(items):
    list_of_items = []
    for key, value in items.items():
        list_of_items.append({
            'found item #' : key,
            'id': value['id'],
            'name': value['name'],
            'cost': value['cost'],
            'description': value['description']
        })
    return list_of_items

def construct_return_package(found_items):
    duplicate_item, same_named_items, same_descriptioned_items = found_items
    num_duplicates = len(duplicate_item)
    num_same_name_items = len(same_named_items)
    num_same_description_items = len(same_descriptioned_items)

    message = ""

    # put together same named items message
    if duplicate_item:
        if num_duplicates > 1:
            message += "%d duplicate items" % num_duplicates
        else:
            message += "1 duplicate item"

    if same_named_items:
        if duplicate_item:
            # add pluralized version of name message
            if num_same_name_items > 1:
                message += ', %d items with the same name' % num_same_name_items
            message += ', 1 item with the same name'
            # add singular version of name message
        message = '1 item with the same name'

    # put together same descriptioned items message
    if same_descriptioned_items:
        # add pluralized version of description message
        if duplicate_item or same_named_items:
            if num_same_description_items > 1:
                message += ' and %d items with the same description' % num_same_description_items
            message += ' and %d item with the same description' % num_same_description_items
        # add singular version of description message
        else:
            message += '1 item with the same description'
    message += ' exists.'

    # message will NOT be None
    return message, duplicate_item, same_named_items, same_descriptioned_items

def delete_all():
    itemSet = dbs.query().all()
    for item in itemSet:
        try:
            dbs.delete()
        except:
            dbs.rollback()
            return False
        dbs.commit()
        return True
