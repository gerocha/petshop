from petshop import db
from typing import Dict


class UserModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), unique=True, nullable=False)


def get_user(username: str) -> Dict:
    return UserModel.query.filter_by(username=username).first()


def insert_user(user: Dict[str, str]) -> Dict:
    user_obj = UserModel(**user)
    db.session.add(user_obj)
    db.session.commit()

    return user_obj
