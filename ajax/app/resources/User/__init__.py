from flask import make_response
from flask_restful import Resource, reqparse
from app.utils import row_to_dict
from .models import User

parser = reqparse.RequestParser()
parser.add_argument('some')


class UserResource(Resource):
    def get(self):
        user = row_to_dict(User.query.first())
        return make_response(user['name'])

    def post(self):
        args = parser.parse_args()
        return make_response(args['some'] + 'wooo')
