from app import db
from app.restaurant.models.RestaurantOwner import restaurant_owner


class Restaurant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    restaurant_number = db.Column(db.Integer)
    address = db.Column(db.String(128))

    owner = db.relationship('User', secondary=restaurant_owner, backref=db.backref('owner', lazy='dynamic'), uselist=False)
    bills = db.relationship('Bill', backref=db.backref('restaurant'), lazy='dynamic')

    workers = db.relationship('User')

    def __init__(self, owner=None, name=None, restaurant_number=None, address=None):
        self.owner = owner
        self.name = name
        self.restaurant_number = restaurant_number
        self.address = address

    def to_dict(self):
        restaurant = {
            'id' : self.id,
            'name' : self.name,
            'restaurant_number' : self.restaurant_number,
            'address' : self.address
        }

        return restaurant

    def __repr__(self):
        return '<Restaurant %r #%r>' % (self.name, self.restaurant_number)
