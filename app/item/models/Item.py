from app import db

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    #resturant_id = ()
    name = db.Column(db.String(50))
    cost = db.Column(db.Float)
    description = db.Column(db.String(100))

    def __init__(self, name=None, cost=None, description=None):
        self.name = name
        self.cost = cost
        self.description = description

    def to_dict(self):
        item = {
            'id': self.id,
            'name': self.name,
            'cost': self.cost,
            'description': self.description
        }
        return item

    def __repr__(self):
        return '<Item %r $%f %r>' % (self.name, self.cost, self.description)
        #'id: %d \tname: %s \tcost: %f' % (self.id, self.name, self.cost)
