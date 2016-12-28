from flask import Blueprint, request, g, jsonify

from app import app, db
from app.bill.models.Bill import Bill
from app.auth.decorators import requires_login, requires_admin
from app.auth.models.User import User
from app.auth import constants as USER

billMod = Blueprint('bills', __name__, url_prefix='/bills')


@billMod.route('/')
@requires_login
@requires_admin
def bill_index():
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

        bill_query = None

        bill_query = Bill.query.paginate(page,25,False)

        bills = []

        for b in bill_query.items:
            bill = b.to_dict()
            print(bill)

            bills.append(bill)

        return jsonify({
            'status' : 'success',
            'meta' : {
                'page' : bill_query.page,
                'pages' : bill_query.pages,
                'total' : bill_query.total
            },
            'data' : {
                'bills' : bills
            }
        })
    else:
        pass

@billMod.route('/<int:billId>', methods=['GET', 'PUT', 'DELETE'])
@requires_login
def bill_single(billId):
    pass
