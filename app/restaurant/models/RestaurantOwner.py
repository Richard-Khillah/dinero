from app import db

restaurant_owner= db.Table('restaurant_owner',
    db.Column('restaurant_id', db.Integer, db.ForeignKey('restaurant.id')),
    db.Column('owner_id', db.Integer, db.ForeignKey('user.id'))
)
