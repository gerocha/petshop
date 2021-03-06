from flask.views import MethodView

from flask import (
        request,
        jsonify
        )

from sqlalchemy.exc import IntegrityError
from marshmallow import Schema, fields, ValidationError
from petshop.pet_model import insert_pet
from flask_jwt import jwt_required, current_identity


class PetSchema(Schema):
    name = fields.Str(required=True)
    type = fields.Str(required=True)


class PetAPI(MethodView):
    decorators = [jwt_required()]

    def post(self):
        try:
            pet = PetSchema().load(request.form)
            payload = pet.copy()
            payload['user_id'] = current_identity.id
            insert_pet(payload)
            return jsonify({
                'data': pet
                }), 201
        except ValidationError as err:
            return jsonify({
                'error': err.messages
                }), 400
