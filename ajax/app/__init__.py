from flask import Flask
from flask_sqlalchemy import SQLAlchemy

MYSQL_SERVER = 'mysql+pymysql://root:testpass@localhost/db_harsh'

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = MYSQL_SERVER
db = SQLAlchemy(app)

from app.models import User


@app.route('/')
def test():
    user_name = User.query.first().name
    return user_name
