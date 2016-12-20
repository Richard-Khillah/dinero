from flask import Flask, jsonify
from flask import render_template
#from flask_sqlalchemy import SQLAlchemy
from . import root

"""#The below commented code is found in /dinero/app/__init__.py
app = xFlask(__name__)
app.config.from_pyfile('config.py')

db = SQLAlchemy(app) ##this should prolly go somewhere else
#db.create_all()
"""

@root.route('/')
def index():
    return render_template('index.html')

@root.app_errorhandler(404)
def not_found(error):
    return jsonify(dict( messsage='Page not found'))
