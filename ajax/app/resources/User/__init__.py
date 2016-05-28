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
        self.reqparse.add_argument('id', type=str, default=None)
        self.reqparse.add_argument('first_name', type=str, default=None)
        self.reqparse.add_argument('last_name', type=str, default=None)
        self.reqparse.add_argument('email', type=str, default=None)
        self.reqparse.add_argument('photo_url', type=str, default=None)
        self.reqparse.add_argument('external_auth_type', type=str,
                                   default=None)
        self.reqparse.add_argument('external_auth_id', type=str, default=None)
        self.args = self.reqparse.parse_args()
        super(Users, self).__init__()

    def get(self):
        users = _build_query({
            'id': self.args['id'],
            'first_name': self.args['first_name'],
            'last_name': self.args['last_name'],
            'email': self.args['email'],
            'external_auth_type': self.args['external_auth_type'],
        })
        return build_objects(users), 200

    def post(self):
        try:
            assert self.args['first_name']
            assert self.args['email']
            assert self.args['external_auth_type']
            assert self.args['external_auth_id']
        except AssertionError:
            abort(400)
        try:
            new_user = UserModel(
                first_name=self.args['first_name'],
                last_name=self.args['last_name'],
                email=self.args['email'],
                photo_url=self.args['photo_url'],
                external_auth_type=self.args['external_auth_type'],
                external_auth_id=self.args['external_auth_id'],
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
        self.reqparse.add_argument('first_name', type=str, default=None)
        self.reqparse.add_argument('last_name', type=str, default=None)
        self.reqparse.add_argument('email', type=str, default=None)
        self.reqparse.add_argument('photo_url', type=str, default=None)
        self.reqparse.add_argument('external_auth_type', type=str,
                                   default=None)
        self.reqparse.add_argument('external_auth_id', type=str, default=None)
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
    if params['first_name']:
        q = q.filter_by(first_name=params['first_name'])
    if params['last_name']:
        q = q.filter_by(last_name=params['last_name'])
    if params['email']:
        q = q.filter_by(email=params['email'])
    if params['external_auth_type']:
        q = q.filter_by(external_auth_type=params['external_auth_type'])
    return q
