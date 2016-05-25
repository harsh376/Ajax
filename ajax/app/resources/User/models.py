from uuid import uuid4
from app.utils.alchemy import UUID
from app import db


class UserModel(db.Model):
    __tablename__ = 'users'

    id = db.Column(UUID, primary_key=True, nullable=False, default=uuid4)
    name = db.Column(db.String(191), nullable=False)
    email = db.Column(db.String(128), nullable=False)
