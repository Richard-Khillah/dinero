from app import db
from app import bcrypt
from sqlalchemy.ext.hybrid import hybrid_property

class Resturant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(120), unique=True)
    address = db.Column(db.String(120))
    username = db.Column(db.String(25), unique=True)
    _password = db.Column(db.String(120))

    def __init__(self, name=None, username=None,email=None, password=None, address=None):
      self.name = name
      self.email = email
      self.username = username
      self.password = password
      self.address = address

    @hybrid_property
    def password(self):
        return self._password

    @password.setter
    def _set_password(self, password):
        # store hash not plain text password
        self._password = bcrypt.generate_password_hash(password).decode('utf-8')

    def check_password(self, password):
        return bcrypt.check_password_hash(password, self._password)


    # this function is required in all models!!!
    def to_dict(self):
        resturant = {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'username': self.username,
            'address' : self.address
        }

        return resturant

    def __repr__(self):
        return '<Resturant %r>' % (self.email)
