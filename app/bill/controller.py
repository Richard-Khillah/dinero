from flask import Blueprint, request, g, jsonify

from app import app, db
from app.auth.decorators import requires_login


billMod = Blueprint('bills', __name__, url_prefix='/bills')


@billMod.route('/')
@requires_login
def bill_index():
    pass

@billMod.route('/<int:billId>')
@requires_login
def bill_single(billId):
    pass
