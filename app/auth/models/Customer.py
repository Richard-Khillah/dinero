from app import db
from app import bcrypt
from sqlalchemy.ext.hybrid import hybrid_property

class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    username = db.Column(db.String(20), unique=True)
    email = db.Column(db.String(120), unique=True)
    _password = db.Column(db.String(120))

    def __init__(self, name=None, username=None, email=None, password=None):
      self.name = name
      self.email = email
      self.username = username
      self.password = password

    @hybrid_property
    def password(self):
        return self._password

    @password.setter
    def _set_password(self, password):
        # store hash not plain text password
        self._password = bcrypt.generate_password_hash(password).decode('utf-8')

    def check_password(self, password):
        return bcrypt.check_password_hash(self._password, password)


    # this function is required in all models!!!
    def to_dict(self):
        customer = {
            'id': self.id,
            'username' : self.username,
            'name': self.name,
            'email': self.email,
        }

        return customer

    def __repr__(self):
        return '<Customer %r>' % (self.email)
