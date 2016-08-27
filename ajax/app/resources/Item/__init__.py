from flask import abort
from flask_restful import Resource, reqparse

from sqlalchemy.exc import IntegrityError

from app import db
from app.utils import build_object, build_objects, update_model
from .models import ItemModel


# Resource Collection
class Items(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('id', type=str)
        # removed the type because for python2.7 (docker)
        # default is 'unicode'
        # TODO: add type after upgrading to python3.4 inside docker
        self.reqparse.add_argument('name', default=None)
        self.reqparse.add_argument('order', type=int, default=0)
        self.args = self.reqparse.parse_args()
        super(Items, self).__init__()

    def get(self):
        items = _build_query({
            'id': self.args['id'],
            'name': self.args['name'],
        })
        return build_objects(items), 200

    def post(self):
        try:
            assert self.args['name']
        except AssertionError:
            abort(404)
        try:
            new_item = ItemModel(name=self.args['name'],
                                 order=self.args['order'])
            db.session.add(new_item)
            db.session.commit()
        except:
            raise IntegrityError
        return build_object(new_item)


# Resource Detail
class Item(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        # Add default value `None` for all cols except for id
        # TODO: add type after upgrading to python3.4 inside docker
        self.reqparse.add_argument('name', default=None)
        self.reqparse.add_argument('order', type=int, default=0)
        self.args = self.reqparse.parse_args()
        super(Item, self).__init__()

    def get(self, id):
        item = ItemModel.query.filter_by(id=id).first()
        return build_object(item)

    def patch(self, id):
        item = ItemModel.query.filter_by(id=id).first()
        update_model(self.args, item)
        db.session.commit()
        return build_object(item)

    def delete(self, id):
        item = ItemModel.query.filter_by(id=id).first()
        db.session.delete(item)
        db.session.commit()
        return build_object(item)


def _build_query(params):
    q = ItemModel.query
    if params['id']:
        q = q.filter_by(id=params['id'])
    if params['name']:
        q = q.filter_by(name=params['name'])
    return q
