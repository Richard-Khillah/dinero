from '../dinero' import db
from datetime import datetime


class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Float)
    description = db.Column(db.String(120))
    name = db.Column(db.String(50))
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)

    def __init__(self, price, description, name):
        self.price = price
        self.description = description
        self.name = name
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __repr(self):
        return '<User %r>' % (self.name)
