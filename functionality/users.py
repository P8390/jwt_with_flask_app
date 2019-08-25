from database import session
from models.users import User


def get_all_users():
    users = session.query(User).all()
    return dict(list_of_user=[user.username for user in users])


def delete_all_users():
    response = dict(message='No user found to delete')
    users = session.query(User).all()
    if users:
        users.delete()
        session.flush()
        response.update(message='deleted all users successfully')
    return response
