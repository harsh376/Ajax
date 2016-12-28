import bcrypt
from flask import abort
from flask_restful import Resource, reqparse

from sqlalchemy.exc import IntegrityError

from app import db
from app.utils import build_objects
from .models import UserV2Model


# Resource Collection
class UsersV2(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('email', type=str, default=None)
        self.reqparse.add_argument('password', type=str, default=None)
        self.args = self.reqparse.parse_args()
        super(UsersV2, self).__init__()

    def get(self):
        if not self.args['email']:
            abort(400)
        users = UserV2Model.query.filter_by(email=self.args['email'])
        resp = build_objects(users)
        result = []
        if resp:
            resp[0].pop('password')
            result = resp
        return result, 200

    def post(self):
        try:
            assert self.args['email']
            assert self.args['password']
        except AssertionError:
            abort(400)
        try:
            password = self.args['password'].encode('utf-8')
            hashed = bcrypt.hashpw(password, bcrypt.gensalt())
            new_user = UserV2Model(
                email=self.args['email'],
                password=hashed,
            )
            db.session.add(new_user)
            db.session.commit()
            return {'email': self.args['email']}, 201
        except IntegrityError:
            abort(409)
