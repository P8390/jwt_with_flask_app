from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import os


def create_db_engine(database_url):
    engine = create_engine(database_url)
    return engine


def get_session():
    database_url = os.environ.get('DATABASE_URL')
    if not database_url:
        raise ValueError('DATABASE-URL-NOT-FOUND')

    engine = create_db_engine(database_url)
    session_factory = sessionmaker(bind=engine)
    session_obj = scoped_session(session_factory)()
    return session_obj

session = get_session()
