from flask import request
from flask_restful import Resource

from service_api.domain.products import get_products


class ProductsResource(Resource):

    def get(self):
        data = request.args.to_dict()
        products = get_products(**data)
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
