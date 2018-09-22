from werkzeug.security import generate_password_hash, \
     check_password_hash
from sqlalchemy.ext.hybrid import hybrid_property, hybrid_method

from petshop import db
from typing import Dict


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    _password = db.Column(db.String(250), unique=True, nullable=False)
    pets = db.relationship('Pet', backref='user', lazy=True)

    def __init__(self, **kwargs):
        self.username = kwargs['username']
        self.password = kwargs['password']
        self.email = kwargs['email']

    @hybrid_property
    def password(self):
        return self._password

    @password.setter
    def password(self, password):
        self._password = generate_password_hash(password)

    @hybrid_method
    def is_correct_password(self, plaintext_password):
        return check_password_hash(self._password, plaintext_password)


def get_user(username: str) -> Dict:
    return User.query.filter_by(username=username).first()


def insert_user(user_payload: Dict[str, str]) -> Dict:
    user = user_payload.copy()
    user['password'] = generate_password_hash(user['password'])
    user_obj = User(**user)
    db.session.add(user_obj)
    db.session.commit()

    return user_obj


def get_user_by_id(id: int):
    return User.query.get(id)


def authenticate(username, password):
    user = get_user(username)
    if user and user.is_correct_password(password):
        return user


def identity(payload):
    user_id = payload['identity']
    return get_user_by_id(user_id)
