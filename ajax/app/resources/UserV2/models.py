import bcrypt
from uuid import uuid4
from app.utils.alchemy import UUID
from app import db


class UserV2Model(db.Model):
    __tablename__ = 'users_v2'

    id = db.Column(UUID, primary_key=True, nullable=False, default=uuid4)
    email = db.Column(db.String(128), nullable=False, unique=True)
    password = db.Column(db.String(1024), nullable=False)

    def verify_user(self, email, password):
        password = password.encode()

        if isinstance(self.password, str):
            self.password = self.password.encode()

        pwhash = bcrypt.hashpw(password, self.password)
        if self.email == email and self.password == pwhash:
            return self.id
        else:
            return None
