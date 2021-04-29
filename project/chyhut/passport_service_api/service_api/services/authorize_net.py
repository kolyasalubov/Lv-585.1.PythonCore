from authorizenet import apicontractsv1
from flask import current_app


class AuthorizeNET:

    def __init__(self, app=None) -> None:
        self.app = app
        self.merchant_auth = None
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        with app.app_context():
            self.merchant_auth = self._create_merchant_auth()

    @staticmethod
    def _create_merchant_auth():
        merchant_auth = apicontractsv1.merchantAuthenticationType()
        merchant_auth.name = current_app.config['API_LOGIN_NAME']
        merchant_auth.transactionKey = current_app.config['TRANSACTION_KEY']
        return merchant_auth