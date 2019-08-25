from app import create_flask_app
from common_constants.constants import FLASK_CONFIG_MODULE
from database import session
from restful_apis import create_restful_api
from utils import config_logger
from flask_jwt_extended import JWTManager

app = create_flask_app('Flask Jwt')
app.config.from_object(FLASK_CONFIG_MODULE)
app.config['JWT_SECRET_KEY'] = 'demo_app'
jwt = JWTManager(app)
app.config['JWT_HEADER_TYPE'] = 'JWT'

config_logger(app)
create_restful_api(app)


def close_session(resp):
    session.close()  # used to remove actual session
    # session.remove() https://groups.google.com/forum/#!msg/sqlalchemy/twoHzgXcR60/nZqMKkCz9UwJ
    return resp

app.teardown_request(close_session)
app.teardown_appcontext(close_session)


if __name__ == '__main__':
    app.run()
