from flask import abort
from flask_restful import Resource, reqparse

from sqlalchemy.exc import IntegrityError

from app import db
from app.utils import build_object, build_objects
from .models import User


class Users(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('id', type=int, default=None)
        self.reqparse.add_argument('name', type=str, default=None)
        self.args = self.reqparse.parse_args()
        super(Users, self).__init__()

    def get(self):
        users = self._build_query({
            'id': self.args['id'],
            'name': self.args['name'],
        })
        return build_objects(users), 200

    def post(self):
        try:
            assert self.args['name']
        except AssertionError:
            abort(404)
        try:
            new_user = User(name=self.args['name'])
            db.session.add(new_user)
            db.session.commit()
        except:
            raise IntegrityError
        return build_object(new_user)

    @staticmethod
    def _build_query(params):
        q = User.query
        if params['id']:
            q = q.filter_by(id=params['id'])
        if params['name']:
            q = q.filter_by(name=params['name'])
        return q
