from flask import Blueprint, request, g, redirect, url_for, jsonify
from datetime import datetime, timedelta
import pprint

from app.auth.models.User import User
from app.auth.decorators import requires_login, requres_status_manager

#@{what}.route('/add_item_to_db', methods=['POST'])
@requires_login
@requres_status_manager
def add_item_to_db():
    #depth=5? what does this do?
    print(pprint.pformat(request.values, depth=5))

    # Check whether item exists
    item = Item.query.fileter(Item.name==request.json['name']).all()
    
