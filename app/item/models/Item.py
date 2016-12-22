from app import db

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    resturant_id = ()
    name = db.Column(db.String(50))
    cost = db.Column(db.Float)
    description = db.Column(db.String(100))

    def __init__(self, name, cost, description):
        self.name = name
        self.cost = cost
        self.description = description

    def to_dict(self):
        item = {
            'id' = self.id,
            'name' = self.name,
            'cost' = self.cost
            'description' = self.description
        }

    def __repr__(self):
        return 'id: %d \tname: %s \tcost: %f' % (self.id, self.name, self.cost)
