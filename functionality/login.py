from models.users import User
from flask_jwt_extended import create_access_token, create_refresh_token


def user_login(**kwargs):
    user_name = kwargs.get('username')
    password = kwargs.get('password')
    user_info = User.get_user_info_from_username(user_name)
    if not user_info:
        raise ValueError('USER-DOES-NOT-EXISTS')
    # verify password
    if not User.verify_password(password, user_info.password):
        raise ValueError('INVALID-PASSWORD')
    access_token = create_access_token(identity=user_name)
    refresh_token = create_refresh_token(identity=user_name)
    return dict(access_token=access_token, refresh_token=refresh_token)
