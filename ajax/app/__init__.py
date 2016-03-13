from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api

MYSQL_SERVER = 'mysql+pymysql://root:testpass@localhost/db_harsh'

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = MYSQL_SERVER
db = SQLAlchemy(app)
api = Api(app)

from app.resources.User import UserResource

# Mapping resources to routes
api.add_resource(UserResource, '/users')
