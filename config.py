import os
import sys

SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")

# logging
DEFAULT_LOGGER_NAME = os.environ.get("DEFAULT_LOGGER_NAME")
LOGGING_CONFIG = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': '%(asctime)s - [%(levelname)s] - %(module)s - '
                      '%(filename)s - %(funcName)s - %(lineno)d - %(message)s'
        }
    },
    'handlers': {
        DEFAULT_LOGGER_NAME: {
            'class': 'logging.StreamHandler',
            'level': "INFO",
            'formatter': 'standard',
            'stream': sys.stdout
        }
    },
    'loggers': {
        DEFAULT_LOGGER_NAME: {
            'handlers': [DEFAULT_LOGGER_NAME],
            'level': 'INFO'
        }
    }
}
