from flask import Flask
from flask_cors import CORS
from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy

from service_api import api
from service_api.config import runtime_config
from service_api.constants import DEFAULT_SERVICE_NAME
from service_api.services import logger
from service_api.services.authorize_net import AuthorizeNET

db = SQLAlchemy()
mail = Mail()
authorize_net = AuthorizeNET()


def create_app() -> Flask:
    flask_app = Flask(DEFAULT_SERVICE_NAME)
    flask_app.config.from_object(runtime_config())
    CORS(
        flask_app,
        resources={r'*': {'origin': '*'}},
        expose_headers=[
            'Content-Type'
        ]
    )

    from service_api.models import models
    db.init_app(flask_app)
    mail.init_app(flask_app)
    logger.setup_logging(flask_app)
    authorize_net.init_app(flask_app)

    api.load_api_v1(flask_app)

    return flask_app
