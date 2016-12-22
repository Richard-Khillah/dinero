from app import db
from app import bcrypt
from sqlalchemy.ext.hybrid import hybrid_property

from app.auth import constants as USER

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    username = db.Column(db.String(20), unique=True)
    email = db.Column(db.String(120), unique=True)
    role = db.Column(db.SmallInteger, default=USER.CUSTOMER)
    _password = db.Column(db.String(120))

    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurant.id'))


    def __init__(self, name=None, username=None, email=None, password=None):
      self.name = name
      self.email = email
      self.username = username
      self.password = password
      self.restaurant = None

    @hybrid_property
    def password(self):
        return self._password

    @password.setter
    def _set_password(self, password):
        # store hash not plain text password
        self._password = bcrypt.generate_password_hash(password).decode('utf-8')

    def check_password(self, password):
        return bcrypt.check_password_hash(self._password, password)

    def get_role(self):
        return USER.ROLE[self.role]


    # this function is required in all models!!!
    def to_dict(self):
        user = {
            'id': self.id,
            'username' : self.username,
            'name': self.name,
            'email': self.email,
            'role' : self.get_role()
        }

        return user

    def __repr__(self):
        return '<User %r>' % (self.email)
