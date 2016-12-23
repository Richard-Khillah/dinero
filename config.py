import os

"""include the base path, in this case ??"""
_basedir = os.path.abspath(os.path.dirname(__file__))  #+ '/data/'
#wrt to +'/data', we might be able to @app.route

class Default:
    PORT = 5050

class Development(Default):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(_basedir, 'app.sqlite')
    SQLALCHEMY_MIGRATE_REPO = os.path.join(_basedir, 'db_repository')
    DEBUG = True
    SECRET_KEY = 'asdfljk23piorj9032rjidafjd90sfasfds0fiasd'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

config = {
    'DEFAULT': Default,
    'DEVELOPMENT': Development
}
