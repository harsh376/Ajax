from flask import make_response
from flask_restful import Resource
from app.utils import row_to_dict
from .models import User


class UserResource(Resource):
    def get(self):
        user = row_to_dict(User.query.first())
        return make_response(user['name'])
