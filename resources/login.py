from flask_restful import Resource, marshal_with, fields
from webargs.flaskparser import use_kwargs
from marshmallow import Schema, fields as field

from functionality.login import user_login
from utils import handle_exception


class LoginRequestFormat(Schema):
    username = field.Email(required=True)
    password = field.Str(required=True)

    class Meta:
        strict = True


return_response = dict(access_token=fields.String, refresh_token=fields.String)


class Login(Resource):

    decorators = [handle_exception]

    @use_kwargs(LoginRequestFormat)
    @marshal_with(return_response)
    def post(self, **kwargs):
        response = user_login(**kwargs)
        return response
