from flask import request, g
from flask_mail import Message
from flask_restful import Resource

from service_api.app import mail
from service_api.domain.clients import create_client
from service_api.services.decorators import authenticate
from service_api.services.forms import ClientSchema


class ClientsResource(Resource):
    method_decorators = []

    def post(self):
        client_data = ClientSchema().load(request.get_json(force=True))
        client = create_client(client_data)
        msg = Message(
            subject='Authorization Token',
            body=f'Hi,\nYour authorization token: {client.client_code}',
            recipients=[client.email]
        )
        mail.send(msg)
        return {
            'message': 'Client was successfully created'
        }


class ClientResource(Resource):
    method_decorators = [authenticate]

    def get(self):
        client = g.client
        return {
            'first_name': client.first_name,
            'last_name': client.last_name,
            'middle_name': client.middle_name,
            'phone_number': client.phone_number,
            'email': client.email,
            'passport_number': client.passport_number,
            'itn': client.itn
        }
