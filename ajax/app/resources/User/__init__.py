from flask import abort
from flask_restful import Resource, reqparse

from sqlalchemy.exc import IntegrityError

from app import db
from app.utils import build_object, build_objects, update_model
from .models import UserModel


# Resource Collection
class Users(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('id', type=int, default=None)
        self.reqparse.add_argument('name', type=str, default=None)
        self.reqparse.add_argument('email', type=str, default=None)
        self.args = self.reqparse.parse_args()
        super(Users, self).__init__()

    def get(self):
        users = _build_query({
            'id': self.args['id'],
            'name': self.args['name'],
            'email': self.args['email'],
        })
        return build_objects(users), 200

    def post(self):
        try:
            assert self.args['name']
            assert self.args['email']
        except AssertionError:
            abort(400)
        try:
            new_user = UserModel(
                name=self.args['name'],
                email=self.args['email'],
            )
            db.session.add(new_user)
            db.session.commit()
        except:
            raise IntegrityError
        return build_object(new_user)


# Resource Detail
class User(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        # Add default value `None` for all cols except for id
        self.reqparse.add_argument('name', type=str, default=None)
        self.reqparse.add_argument('email', type=str, default=None)
        self.args = self.reqparse.parse_args()
        super(User, self).__init__()

    def get(self, id):
        user = UserModel.query.filter_by(id=id).first()
        return build_object(user)

    def patch(self, id):
        user = UserModel.query.filter_by(id=id).first()
        update_model(self.args, user)
        db.session.commit()
        return build_object(user)

    def delete(self, id):
        user = UserModel.query.filter_by(id=id).first()
        db.session.delete(user)
        db.session.commit()
        return build_object(user)


def _build_query(params):
    q = UserModel.query
    if params['id']:
        q = q.filter_by(id=params['id'])
    if params['name']:
        q = q.filter_by(name=params['name'])
    if params['email']:
        q = q.filter_by(email=params['email'])
    return q
