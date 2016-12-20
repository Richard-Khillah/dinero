import os


DATABASE = os.path.abspath(os.path.dirname(__file__)) + '/data/'

#app config
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(DATABASE, 'app.sqlite')
SQLALCHEMY_MIGRATE_REPO = os.path.join(DATABASE, 'db_repository')
DEBUG =  True
SECRET_KEY = 'asdfljk23piorj9032rjidafjd90sfasfds0fiasd'
