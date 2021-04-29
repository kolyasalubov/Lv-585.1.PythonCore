from flask import request, g
from flask_restful import Resource

from service_api.domain.orders import get_order, get_order_products
from service_api.domain.payment import CreditCardPayment, CreditCard, Payment
from service_api.services.decorators import authenticate
from service_api.services.forms import CreditCardSchema


class PaymentResource(Resource):
    method_decorators = [authenticate]

    def post(self):
        client = g.client
        order = get_order(client_id=client.id, active=True)
        order_products = get_order_products(order)
        payment = Payment()
        if order.payment_method == 'credit_card':
            data = CreditCardSchema().load(request.get_json(force=True))
            payment = CreditCardPayment(CreditCard(**data))
            payment.charge(client=client, order=order, products=order_products)
        payment.send_email(client=client, order=order, products=order_products)
        return {
            'message': 'You have been successfully charged'
        }
