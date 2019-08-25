from flask_restful import Resource

from utils import handle_exception
from flask_jwt_extended import jwt_refresh_token_required, get_jwt_identity, create_access_token


class TokenRefresh(Resource):
    decorators = [jwt_refresh_token_required, handle_exception]

    @staticmethod
    def post():
        current_user = get_jwt_identity()
        access_token = create_access_token(current_user)
        return dict(access_token=access_token)
