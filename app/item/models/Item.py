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

    def __str__(self):
        return '<Item %d %r>' % (self.id, self.name)
        #return '<Item %r $%f %r>' % (self.name, self.cost, self.description)
    def __repr__(self):
        return '<Item %d %r %f %r>' % \
               (self.id, self.name, self.cost, self.description)

    def __eq__(self, other):
        other = Item(other)
        name = self.name == other.name
        cost = self.cost == other.cost
        description = self.description == other.description

        return id and name and cost and description
