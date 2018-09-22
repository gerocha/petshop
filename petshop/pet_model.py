from petshop import db
from typing import Dict


class Pet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    type = db.Column(db.String(120), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)


def get_pet_by_name(username: str) -> Dict:
    return Pet.query.filter_by(username=username).first()


def insert_pet(pet: Dict[str, str]) -> Dict:
    pet_obj = Pet(**pet)
    db.session.add(pet_obj)
    db.session.commit()

    return pet_obj


def get_pet_by_id(id: int):
    return Pet.query.get(id)
