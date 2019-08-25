from passlib.hash import pbkdf2_sha256 as sha256

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from database import session

Base = declarative_base()
metadata = Base.metadata


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(120), nullable=False, unique=True)
    password = Column(String(120), nullable=False)

    @staticmethod
    def save_to_db(**kwargs):
        user_obj = User(**kwargs)
        session.add(user_obj)
        session.flush()

    @staticmethod
    def get_user_info_from_username(username):
        user_obj = session.query(User).filter(User.username == username).first()
        return user_obj

    @staticmethod
    def generate_password_hash(password):
        return sha256.hash(password)

    @staticmethod
    def verify_password(password, hash):
        return sha256.verify(password, hash)
