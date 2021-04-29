from flask import Blueprint, Flask
from flask_restful import Api
from werkzeug.exceptions import HTTPException

from service_api.exceptions import ApiError


class PassportServiceApi(Api):

    def handle_error(self, e):
        if not isinstance(e, HTTPException):
            if isinstance(e, ApiError):
                message = str(e)
            else:
                message = repr(e)

            error_code = getattr(e, 'status_code', 500)
            error_data = getattr(e, 'data', None)

            e = HTTPException(message)
            e.code = error_code
            if error_data:
                e.data = error_data

        return super().handle_error(e)


def load_api_v1(app: Flask) -> None:
    from service_api.resources.base import SmokeResource
    from service_api.resources.clients import ClientsResource
    from service_api.resources.clients import ClientResource
    from service_api.resources.orders import OrderResource
    from service_api.resources.orders import OrderProductsResource
    from service_api.resources.orders import OrderDocumentTypes
    from service_api.resources.documents import DocumentsResource
    from service_api.resources.documents import DocumentResource
    from service_api.resources.products import ProductsResource
    from service_api.resources.payment import PaymentResource

    api_prefix = f"/{app.config.get('SERVICE_NAME')}/v1"
    api_blueprint = Blueprint('v1', 'v1', url_prefix=api_prefix)
    api = PassportServiceApi(api_blueprint)

    api.add_resource(SmokeResource, '/smoke')
    api.add_resource(ClientsResource, '/clients')
    api.add_resource(ClientResource, '/client')
    api.add_resource(OrderResource, '/order')
    api.add_resource(OrderProductsResource, '/order-products')
    api.add_resource(OrderDocumentTypes, '/order-document-types')
    api.add_resource(DocumentsResource, '/documents')
    api.add_resource(DocumentResource, '/document-download')
    api.add_resource(ProductsResource, '/products')
    api.add_resource(PaymentResource, '/payment')

    app.register_blueprint(api_blueprint)
