from flask import Blueprint, request, g, jsonify

from app import app, db

billMod = Blueprint('bills', __name__, url_prefix='/bills')


@billMod.route('/')
def bill_index():
    
