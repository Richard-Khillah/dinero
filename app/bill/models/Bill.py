from app import db
from datetime import datetime
from app.bil.models.Billitem import BillItems

class Bill(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    paid = db.Column(db.Boolean, default=False)
    reciept_number = db.Column(db.String(120))
    customer = db.Column(db.Integer, db.ForeignKey('user.id'))
    message = db.Column(db.String(120), default=None)
    created_at = db.Column(db.DateTime)
    # resturant id

    items = db.relationship('Item', secondary=BillItems, backref=db.backref('bills', lazy='dynamic'))

    def __init__(self, paid=False, reciept_number=None, customer, message, created_at=datetime.now()):
        self.paid = paid
        self.reciept_number = reciept_number
        self.customer = customer
        self.message = message
        self. created_at = created_at



    def to_dict(self):
        return {
            'id' : self.id,
            'paid' : self.paid,
            'reciept_number' : self.reciept_number,
            'message' : self.message,
            'created_at' : self.created_at
        }

    def __repr__(self):
        return '<Bill %r %r>' % (self.id, self.paid)
