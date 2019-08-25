from flask_jwt_extended import jwt_required, get_jwt_identity

import logging
import logging.config
from database import session

from functools import wraps
from flask_restful import abort
from werkzeug.exceptions import UnprocessableEntity
from flask_jwt_extended.exceptions import NoAuthorizationError, InvalidHeaderError, WrongTokenError
from jwt.exceptions import ExpiredSignatureError

from models.users import User


def config_logger(app):
    logging.config.dictConfig(app.config.get('LOGGING_CONFIG'))
    logger = logging.getLogger(app.config.get("DEFAULT_LOGGER_NAME"))
    app.logger.addHandler(logger)
    app.logger.info("logger configured")


def handle_exception(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        try:
            return fn(*args, **kwargs)
        except UnprocessableEntity as exc:
            session.rollback()
            return abort(422, message=str(exc))
        except ValueError as exc:
            session.rollback()
            return abort(400, message=str(exc))
        except NoAuthorizationError as exc:
            session.rollback()
            return abort(401, message=str(exc))
        except InvalidHeaderError as exc:
            session.rollback()
            return abort(400, message=str(exc))
        except WrongTokenError as exc:
            session.rollback()
            return abort(400, message=str(exc))
        except ExpiredSignatureError as e:
            session.rollback()
            abort(400, message=str(e))
        except Exception:
            session.rollback()
            return abort(500, message='Something Went Wrong')
    return wrapper


def get_current_jwt_identity(fn):
    @wraps(fn)
    @jwt_required
    def wrapper(*args, **kwargs):
        current_user = get_jwt_identity()
        user_info = session.query(User).filter(User.username == current_user).first()
        return fn(user_info, *args, **kwargs)
    return wrapper
