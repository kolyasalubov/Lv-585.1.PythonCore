import os
from dataclasses import dataclass
from decimal import Decimal
from typing import List

from authorizenet import apicontractsv1
from authorizenet.apicontrollers import createTransactionController
from flask_mail import Message
from mako.template import Template

from service_api.app import authorize_net, mail
from service_api.exceptions import UnprocessableEntityError
from service_api.models import Client, Order, Product


@dataclass
class CreditCard:
    card_number: str
    expiration_date: str
    merchant_id: str


class Payment:

    def charge(self, **kwargs) -> None:
        raise NotImplementedError

    @staticmethod
    def send_email(**kwargs) -> None:
        client: Client = kwargs.get('client')
        order: Order = kwargs.get('order')
        products: List[Product] = kwargs.get('products')
        order_template = Template(filename=os.path.join(os.getcwd(), 'service_api', 'templates', 'order.html'))
        order_html = order_template.render(order=order, products=products)
        msg = Message(
            subject='Order Confirmation',
            html=order_html,
            recipients=[client.email]
        )
        mail.send(msg)


class CreditCardPayment(Payment):

    def __init__(self, credit_card: CreditCard) -> None:
        self._credit_card = credit_card

    def charge(self, **kwargs) -> None:
        client: Client = kwargs.get('client')
        order: Order = kwargs.get('order')
        products: List[Product] = kwargs.get('products')

        payment = self._get_payment_info()

        order_info = apicontractsv1.orderType()
        order_info.invoiceNumber = str(order.id)

        customer_address = self._get_customer_address_info(client)
        customer_data = self._get_customer_identity_info(client)
        line_items = self._get_line_items_info(products)

        transaction_request = apicontractsv1.transactionRequestType()
        transaction_request.transactionType = 'authCaptureTransaction'
        transaction_request.amount = Decimal(order.total / 24.5).quantize(Decimal(10) ** -2)
        transaction_request.payment = payment
        transaction_request.order = order_info
        transaction_request.billTo = customer_address
        transaction_request.customer = customer_data
        transaction_request.lineItems = line_items

        create_transaction_request = apicontractsv1.createTransactionRequest()
        create_transaction_request.merchantAuthentication = authorize_net.merchant_auth
        create_transaction_request.refId = self._credit_card.merchant_id

        create_transaction_request.transactionRequest = transaction_request
        create_transaction_controller = createTransactionController(create_transaction_request)
        create_transaction_controller.execute()

        response = create_transaction_controller.getresponse()
        if response is not None:
            error_message_template = 'Credit card payment error. {}'
            if response.messages.resultCode == 'Ok':
                if hasattr(response.transactionResponse, 'errors'):
                    # str(response.transactionResponse.errors.error[0].errorCode)
                    raise UnprocessableEntityError(
                        error_message_template.format(response.transactionResponse.errors.error[0].errorText)
                    )
            else:
                if hasattr(response, 'transactionResponse') and hasattr(response.transactionResponse, 'errors'):
                    # str(response.transactionResponse.errors.error[0].errorCode)
                    raise UnprocessableEntityError(
                        error_message_template.format(response.transactionResponse.errors.error[0].errorText)
                    )
                else:
                    # response.messages.message[0]['code'].text
                    raise UnprocessableEntityError(
                        error_message_template.format(response.messages.message[0]['text'].text)
                    )
        else:
            raise UnprocessableEntityError('Credit card payment error.')

    def _get_payment_info(self):
        credit_card = apicontractsv1.creditCardType()
        credit_card.cardNumber = self._credit_card.card_number
        credit_card.expirationDate = self._credit_card.expiration_date

        payment = apicontractsv1.paymentType()
        payment.creditCard = credit_card

        return payment

    @staticmethod
    def _get_customer_address_info(client: Client):
        customer_address = apicontractsv1.customerAddressType()
        customer_address.firstName = client.first_name
        customer_address.lastName = client.last_name

        return customer_address

    @staticmethod
    def _get_customer_identity_info(client: Client):
        customer_data = apicontractsv1.customerDataType()
        customer_data.type = 'individual'
        customer_data.id = str(client.id)
        customer_data.email = client.email

        return customer_data

    @staticmethod
    def _get_line_items_info(products: List[Product]):
        line_items = apicontractsv1.ArrayOfLineItem()
        for product in products:
            line_item = apicontractsv1.lineItemType()
            line_item.itemId = str(product.id)
            line_item.name = 'Product'
            line_item.description = product.name
            line_item.quantity = "1"
            line_item.unitPrice = Decimal(product.price / 24.5).quantize(Decimal(10) ** -2)
            line_items.lineItem.append(line_item)
        return line_items
