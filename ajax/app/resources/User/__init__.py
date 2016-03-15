from flask import make_response, jsonify
from flask_restful import Resource, reqparse

from sqlalchemy.exc import IntegrityError

from app import db
from app.utils import row_to_dict
from .models import User

parser = reqparse.RequestParser()
parser.add_argument('name')


class UserResource(Resource):
    def get(self):
        user = row_to_dict(User.query.first())
        data = {'id': user['id'], 'name': user['name']}
        return make_response(jsonify(data))

    def post(self):
        args = parser.parse_args()
        try:
            new_user = User(name=args['name'])
            db.session.add(new_user)
            db.session.commit()
        except:
            raise IntegrityError
        data = {'id': new_user.id, 'name': new_user.name}
        return make_response(jsonify(data))
