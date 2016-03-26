from uuid import uuid4
from app.utils.alchemy import UUID
from app import db


class ItemModel(db.Model):
    __tablename__ = 'items'

    id = db.Column(UUID, primary_key=True, nullable=False, default=uuid4)
    name = db.Column(db.String(191), nullable=False)
    order = db.Column(db.Integer, nullable=False)
