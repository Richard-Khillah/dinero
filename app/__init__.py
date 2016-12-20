from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import config

def create_app(envrionment):
    app = Flask(__name__)
    app.config.from_object(config[envrionment])

    from .root import root
    app.register_blueprint(root)

    db = SQLAlchemy(app)
    db.create_all()
    return app
