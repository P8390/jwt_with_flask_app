from flask_restful import Resource, marshal_with, fields

from functionality.users import get_all_users, delete_all_users
from utils import handle_exception, get_current_jwt_identity
from database import session

get_all_user_response_format = dict(list_of_user=fields.List(fields.String))


class Users(Resource):
    decorators = [get_current_jwt_identity, handle_exception]

    @marshal_with(get_all_user_response_format)
    def get(self, current_identity):
        print(current_identity.__dict__)
        response = get_all_users()
        return response

    @staticmethod
    def delete():
        response = delete_all_users()
        session.commit()
        return response
