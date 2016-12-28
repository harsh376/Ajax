from flask import abort
from flask_restful import Resource, reqparse
from app.resources.UserV2 import UserV2Model
from uuid import uuid4


class Auth(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('email', type=str, default=None)
        self.reqparse.add_argument('password', type=str, default=None)
        self.args = self.reqparse.parse_args()
        super(Auth, self).__init__()

    def post(self):
        try:
            assert self.args['email']
            assert self.args['password']
        except AssertionError:
            abort(400)

        user_id = self._verify_credentials(
            self.args['email'],
            self.args['password'],
        )
        if user_id:
            token = self._generate_token(user_id)
            return {'token': token}, 201
        else:
            abort(401)

    @staticmethod
    def _verify_credentials(email, password):
        """
        :return: if valid credentials, then returns user id else None
        """
        user = UserV2Model.query.filter_by(email=email).first()
        if not user:
            return None
        result = user.verify_user(email, password)
        return result

    @staticmethod
    def _generate_token(user_id):
        """
        Read or Create token
        """
        # TODO: use a stronger token generation method
        token = uuid4().hex
        return token
