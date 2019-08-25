from models.users import User


def user_signup(**kwargs):
    response = dict(status='failed')
    username = kwargs.get('username')
    user_obj = User.get_user_info_from_username(username)
    if user_obj:
        raise ValueError('USER-ALREADY-EXISTS')
    password = kwargs.get('password')
    password_hash = User.generate_password_hash(password)
    kwargs.update(password=password_hash)
    User.save_to_db(**kwargs)
    response.update(status='success')
    return response
