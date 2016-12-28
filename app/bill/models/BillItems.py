from app import db

BillItems = db.Table('bill_items',
    db.Column('item_id', db.Integer, db.ForeignKey('item.id')),
    db.Column('bill_id', db.Integer, db.ForeignKey('bill.id'))
)
