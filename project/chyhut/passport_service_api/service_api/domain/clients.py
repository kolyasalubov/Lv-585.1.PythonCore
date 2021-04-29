import logging
from datetime import date

from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from service_api.domain.db import db_session
from service_api.domain.orders import insert_order
from service_api.exceptions import UnprocessableEntityError
from service_api.models import Client
from service_api.services.utils import generate_unique_identifier

logger = logging.getLogger(__name__)


def insert_client(data: dict, session: Session) -> Client:
    data['client_code'] = generate_unique_identifier().upper()
    client = Client(**data)
    try:
        session.add(client)
        session.flush()
    except IntegrityError as e:
        logger.error(e)
        raise UnprocessableEntityError(e.orig.args[1])
    return client


def get_client(**kwargs) -> Client:
    return Client.query.filter_by(**kwargs).first()


@db_session
def create_client(data: dict, session: Session = None) -> Client:
    client = insert_client(data, session)
    order_data = {
        'status': 'products_selection',
        'client_id': client.id,
        'created_at': date.today().strftime('%Y-%m-%d'),
        'active': True
    }
    insert_order(order_data, session)
    return client
