from uuid import uuid4
from app.utils.alchemy import UUID
from app import db


class UserModel(db.Model):
    __tablename__ = 'users'

    id = db.Column(UUID, primary_key=True, nullable=False, default=uuid4)
    first_name = db.Column(db.String(128), nullable=False)
    last_name = db.Column(db.String(128))
    email = db.Column(db.String(128), nullable=False)
    photo_url = db.Column(db.String(1024))
    external_auth_type = db.Column(db.String(128), nullable=False)
    external_auth_id = db.Column(db.String(128), nullable=False)
