from typing import List

from sqlalchemy.orm import Session

from service_api.domain.db import db_session
from service_api.models import Document


@db_session
def insert_document(data: dict, session: Session = None) -> Document:
    document = Document(**data)
    session.add(document)
    session.flush()
    return document


def get_document(**kwargs) -> Document:
    return Document.query.filter_by(**kwargs).first()


def get_documents(**kwargs) -> List[Document]:
    return Document.query.filter_by(**kwargs).all()
