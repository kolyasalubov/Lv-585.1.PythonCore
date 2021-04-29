import os

from service_api.constants import DEFAULT_SERVICE_NAME


class Config:
    DEBUG = False
    TESTING = False
    SERVICE_NAME = os.environ.get('SERVICE_NAME', DEFAULT_SERVICE_NAME)
    LOG_FORMAT = '[%(asctime)s] - (%(name)s)[%(levelname)s]: %(message)s'
    LOG_LEVEL = 'DEBUG'
    LOG_DATEFMT = '%Y-%m-%d %H:%M:%S %z'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 465
    MAIL_USE_SSL = True
    MAIL_DEFAULT_SENDER = 'yaroch137@gmail.com'
    UPLOAD_FOLDER = os.environ.get('UPLOAD_FOLDER', os.path.join(os.getcwd(), 'uploads'))
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024
    API_LOGIN_NAME = os.environ.get('API_LOGIN_NAME')
    TRANSACTION_KEY = os.environ.get('TRANSACTION_KEY')


class ProductionConfig(Config):
    ENV = 'production'
    LOG_FORMAT = (
        '[%(asctime)s] - (%(name)s)[%(levelname)s] - (%(filename)s:%(lineno)d): %(message)s'
    )
    LOG_LEVEL = 'INFO'


class DevelopmentConfig(Config):
    ENV = 'development'
    DEBUG = True
    SQLALCHEMY_ECHO = True


class TestingConfig(Config):
    ENV = 'development'
    TESTING = True


ENV_CONFIG = {'development': DevelopmentConfig, 'test': TestingConfig, 'production': ProductionConfig}


def runtime_config(config=None):
    if config is None:
        env = os.environ.get('APP_ENV', 'development')
        assert env in ENV_CONFIG, f'Unknown APP_ENV value: {env}'
        config = ENV_CONFIG[env]

    return config
