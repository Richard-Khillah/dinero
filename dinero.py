from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_pyfile('config.py')


db = SQLAlchemy(app)

@app.route('/')
def index():
    return "test"


@app.errorhandler(404)
def not_found(error):
    return jsonify(dict( messsage='Page not found'))


db.create_all()
