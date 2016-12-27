from app import db
from datetime import datetime

from app.item.constants import Category

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    #resturant_id = ()
    name = db.Column(db.String(50))
    cost = db.Column(db.Float)
    description = db.Column(db.String(100)) #can be a db.Text() field
    category = db.Column(db.String(25))

    #created_by = db.Column(db.Integer)
    #modified_by = db.Column(db.Integer)
    #date_created = db.Column(db.DateTime)
    #date_modified = db.Column(db.DateTime)


    def __init__(self, name=None, cost=None, description=None, category=None, **kwargs):
        self.name = name
        self.cost = cost
        self.description = description
        self.category = Category(category)


        # Admin details
        #self.created_by = kwargs['created_by']
        #self.modified_by = kwargs['modified_by']
        #self.date_created = datetime.utcnow()
        #self.date_created = datetime.utcnow()


    def to_dict(self):
        item = {
            'id': self.id,
            'name': self.name,
            'cost': self.cost,
            'description': self.description
            'category': self.category

            # Admin details
            #'created_by':self.created_by
            #'modified_by': self.modified_by
            #'date_created': self.date_created
            #'date_created': self.date_created

        }
        return item

    def __str__(self):
        return '<Item %d %r>' % (self.id, self.name)
        #return '<Item %r $%f %r>' % (self.name, self.cost, self.description)
    def __repr__(self):
        return '<Item %d %r %f %r>' % \
               (self.id, self.name, self.cost, self.description)
