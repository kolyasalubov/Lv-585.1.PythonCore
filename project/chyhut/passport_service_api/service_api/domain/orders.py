from typing import Dict, List

from sqlalchemy.orm import Session

from service_api.domain.db import db_session
from service_api.models import Order, OrderProduct, Product, DocumentType, ProductDocumentType


def insert_order(data: dict, session: Session) -> Order:
    order = Order(**data)
    session.add(order)
    session.flush()
    return order


def get_order(**kwargs) -> Order:
    return Order.query.filter_by(**kwargs).first()


@db_session
def update_order(order: Order, data: dict, session: Session = None):
    if data['status'] and order.status != data['status']:
        order.status = data['status']
    if data['payment_method'] and order.payment_method != data['payment_method']:
        order.payment_method = data['payment_method']
    if data['total'] is not None and order.total != data['total']:
        order.total = data['total']
    return order


@db_session
def insert_order_products(products: List[Dict], session: Session = None) -> None:
    session.get_bind().execute(OrderProduct.__table__.insert(), products)


def get_order_products(order: Order) -> List[Product]:
    return Product.query \
        .join(OrderProduct, Product.id == OrderProduct.product_id) \
        .join(Order, OrderProduct.order_id == Order.id) \
        .filter(Order.id == order.id).all()


def get_order_document_types(order: Order) -> List[DocumentType]:
    return DocumentType.query \
        .join(ProductDocumentType, DocumentType.id == ProductDocumentType.document_type_id) \
        .join(Product, ProductDocumentType.product_id == Product.id)\
        .join(OrderProduct, Product.id == OrderProduct.product_id) \
        .join(Order, OrderProduct.order_id == Order.id) \
        .filter(Order.id == order.id).all()
