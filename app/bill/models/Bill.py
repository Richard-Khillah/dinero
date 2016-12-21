class Bill(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    paid = db.Column(db.Boolean, default=False)
    reciept_number = db.Column(db.String(120))
    customer = db.Column(db.Integer, db.ForeignKey('user.id'))
    message = db.Column(db.String(120), default=None)
    created_at = db.Column(db.DateTime)
    # resturant id
    # items

    def __init__():



    def to_dict():
