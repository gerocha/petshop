from flask.views import MethodView

from flask import (
        request,
        jsonify
        )

from marshmallow import Schema, fields, ValidationError


class UserSchema(Schema):
    username = fields.Str(required=True)
    email = fields.Email()
    created_at = fields.DateTime()


class UserAPI(MethodView):
    def post(self):
        try:
            UserSchema().load(request.form)
            return jsonify({
                'data': 'OK'
                }), 201
        except ValidationError as err:
            return jsonify({
                'error': err.messages
                }), 400
