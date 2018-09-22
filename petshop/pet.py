from flask.views import MethodView

from flask import (
        request,
        jsonify
        )

from sqlalchemy.exc import IntegrityError
from marshmallow import Schema, fields, ValidationError
from petshop.pet_model import insert_pet


class PetSchema(Schema):
    name = fields.Str(required=True)
    type = fields.Str(required=True)


class PetAPI(MethodView):
    def post(self):
        try:
            pet = PetSchema().load(request.form)
            insert_pet(pet)
            return jsonify({
                'data': pet
                }), 201
        except ValidationError as err:
            return jsonify({
                'error': err.messages
                }), 400
