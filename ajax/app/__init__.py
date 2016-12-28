import os
import logging
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api


USER = os.environ.get('MYSQL_USER', 'root')
PASSWORD = os.environ.get('MYSQL_PASSWORD', 'testpass')
HOSTNAME = os.environ.get('MYSQL_HOST', 'localhost')
DATABASE = os.environ.get('MYSQL_DATABASE', 'db_harsh')

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
from app.resources.UserV2 import UsersV2
from app.resources.Auth import Auth


# Mapping resources to routes

api.add_resource(Users, '/users')
api.add_resource(User, '/users/<string:id>')

api.add_resource(Items, '/items')
api.add_resource(Item, '/items/<string:id>')

api.add_resource(UsersV2, '/users/v2')

api.add_resource(Auth, '/token')

