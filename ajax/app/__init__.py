import logging
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api

USER = 'root'
# PASSWORD = 'testpass'
PASSWORD = 'my-secret-pw'
# HOSTNAME = 'localhost' # local mac
HOSTNAME = '192.168.99.100' # docker-machine
DATABASE = 'db_harsh'

MYSQL_SERVER = 'mysql+pymysql://%s:%s@%s/%s?charset=utf8mb4'%(
    USER,
    PASSWORD,
    HOSTNAME,
    DATABASE,
)

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = MYSQL_SERVER
db = SQLAlchemy(app)
api = Api(app)

# Configure logging
app.logger.addHandler(logging.StreamHandler())
app.logger.setLevel(logging.INFO)

from app.resources.User import Users, User
from app.resources.Item import Items, Item

# Mapping resources to routes

api.add_resource(Users, '/users')
api.add_resource(User, '/users/<string:id>')

api.add_resource(Items, '/items')
api.add_resource(Item, '/items/<string:id>')
