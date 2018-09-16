from flask.views import MethodView

from flask import (
        request,
        jsonify
        )

from sqlalchemy.exc import IntegrityError
from marshmallow import Schema, fields, ValidationError
from petshop.user_model import insert_user


class UserSchema(Schema):
    username = fields.Str(required=True)
    password = fields.Str(required=True)
    email = fields.Email(required=True)
    created_at = fields.DateTime()


class UserAPI(MethodView):
    def post(self):
        try:
            user = UserSchema().load(request.form)
            insert_user(user)
            return jsonify({
                'data': user
                }), 201
        except ValidationError as err:
            return jsonify({
                'error': err.messages
                }), 400
        except IntegrityError as err:
            return jsonify({
                'error': 'User already exist'
                }), 409
