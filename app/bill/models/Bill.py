from app import db
from datetime import datetime
from app.bill.models.BillItems import BillItems

class Bill(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    paid = db.Column(db.Boolean, default=False)
    receipt_number = db.Column(db.String(120))
    customer_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    message = db.Column(db.String(120), default=None)
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)

    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurant.id'))
    items = db.relationship('Item', secondary=BillItems, backref=db.backref('bills', lazy='dynamic'))
    customer = db.relationship('User', back_populates='bills')

    def __init__(self, customer, paid=False, receipt_number=None, message=None, created_at=None):
        self.paid = paid
        self.receipt_number = receipt_number
        self.customer = customer
        self.message = message
        self.created_at = created_at
        self.updated_at = datetime.now()
        if created_at is None:
            self.created_at = datetime.now()



    def to_dict(self):
        return {
            'id' : self.id,
            'paid' : self.paid,
            'receipt_number' : self.receipt_number,
            'message' : self.message,
            'created_at' : self.created_at,
            'updated_at' : self.updated_at
        }

    def __repr__(self):
        return '<Bill id:%r paid:%r>' % (self.id, self.paid)
