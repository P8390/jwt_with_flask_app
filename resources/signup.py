from flask_restful import Resource, marshal_with, fields
from webargs.flaskparser import use_kwargs
from marshmallow import Schema, fields as field

from functionality.signup import user_signup
from utils import handle_exception
from database import session


class SignUpRequestFormat(Schema):
    username = field.Email(required=True)
    password = field.Str(required=True)

    class Meta:
        strict = True


return_response = dict(status=fields.String)


class SignUp(Resource):

    decorators = [handle_exception]

    @use_kwargs(SignUpRequestFormat)
    @marshal_with(return_response)
    def post(self, **kwargs):
        response = user_signup(**kwargs)
        session.commit()
        return response
