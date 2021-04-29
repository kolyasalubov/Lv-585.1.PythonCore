from flask import g, request
from flask_restful import Resource

from service_api.domain.orders import get_order, update_order, insert_order_products, get_order_document_types, \
    get_order_products
from service_api.services.decorators import authenticate
from service_api.services.forms import OrderPutSchema


class OrderResource(Resource):
    method_decorators = [authenticate]

    def get(self):
        client = g.client
        order = get_order(client_id=client.id, active=True)
        return {
            'id': order.id,
            'status': order.status,
            'total': order.total,
            'payment_method': order.payment_method,
            'created_at': order.created_at.strftime('%Y-%m-%d')
        }

    def put(self):
        client = g.client
        order_data = OrderPutSchema().load(request.get_json(force=True))
        order = get_order(client_id=client.id, active=True)
        order = update_order(order, order_data)
        return {
            'id': order.id,
            'status': order.status,
            'total': order.total,
            'payment_method': order.payment_method,
            'created_at': order.created_at.strftime('%Y-%m-%d')
        }


class OrderProductsResource(Resource):
    method_decorators = [authenticate]

    def post(self):
        client = g.client
        data = request.get_json(force=True)
        order = get_order(client_id=client.id, active=True)
        insert_order_products([{'order_id': order.id, 'product_id': product['id']} for product in data['products']])
        return {
            'message': 'Products were added to order'
        }

    def get(self):
        client = g.client
        order = get_order(client_id=client.id, active=True)
        products = get_order_products(order)
        return [
            {
                'id': product.id,
                'name': product.name,
                'price': product.price,
                'currency': product.currency,
                'type': product.type,
                'eta': product.eta,
                'eta_type': product.eta_type
            } for product in products
        ]


class OrderDocumentTypes(Resource):
    method_decorators = [authenticate]

    def get(self):
        client = g.client
        order = get_order(client_id=client.id, active=True)
        document_types = get_order_document_types(order)
        return [
            {
                'id': doc_type.id,
                'type': doc_type.type,
                'title': doc_type.title
            } for doc_type in document_types
        ]
