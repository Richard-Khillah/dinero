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

config = {
    'DEFAULT': Default,
    'DEVELOPMENT': Development
}



"""
DATABASE = os.path.abspath(os.path.dirname(__file__)) + '/data/'

#app config
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(DATABASE, 'app.sqlite')
SQLALCHEMY_MIGRATE_REPO = os.path.join(DATABASE, 'db_repository')
DEBUG =  True
SECRET_KEY = 'asdfljk23piorj9032rjidafjd90sfasfds0fiasd'
"""
