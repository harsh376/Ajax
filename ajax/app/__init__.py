from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api

MYSQL_SERVER = 'mysql+pymysql://root:testpass@localhost/db_harsh'

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = MYSQL_SERVER
db = SQLAlchemy(app)
api = Api(app)

from app.resources.User import Users, User
from app.resources.Item import Items, Item

# Mapping resources to routes

api.add_resource(Users, '/users')
api.add_resource(User, '/users/<string:id>')

api.add_resource(Items, '/items')
api.add_resource(Item, '/items/<string:id>')
