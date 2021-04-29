import os

from flask import request, current_app as app, g, send_from_directory
from flask_restful import Resource
from werkzeug.utils import secure_filename

from service_api.domain.documents import insert_document, get_document, get_documents
from service_api.exceptions import NotFoundError
from service_api.services.decorators import authenticate
from service_api.services.utils import generate_unique_identifier


DOCUMENT_TITLE = {
    'passport': 'Passport',
    'itn': 'Individual Tax Number'
}


class DocumentsResource(Resource):
    method_decorators = [authenticate]

    def post(self):
        client = g.client
        for document_type, file in request.files.items():
            filename = secure_filename(file.filename)
            prefix = generate_unique_identifier()[:12]
            path = os.path.join(app.config['UPLOAD_FOLDER'], f'{prefix}_{filename}')
            insert_document({
                'name': filename,
                'title': DOCUMENT_TITLE[document_type],
                'prefix': prefix,
                'type': document_type,
                'path': path,
                'client_id': client.id
            })
            file.save(path)
        return {
            'message': 'Documents were uploaded successfully'
        }

    def get(self):
        client = g.client
        documents = get_documents(client_id=client.id)
        return [
            {
                'id': document.id,
                'name': document.name,
                'type': document.type,
                'title': document.title
            } for document in documents
        ]


class DocumentResource(Resource):
    method_decorators = [authenticate]

    def get(self):
        client = g.client
        data = request.args.to_dict()
        data['client_id'] = client.id
        document = get_document(**data)
        if not document:
            raise NotFoundError('No such document')
        try:
            return send_from_directory(
                app.config['UPLOAD_FOLDER'], f'{document.prefix}_{document.name}',
                as_attachment=True, attachment_filename=document.name
            )
        except FileNotFoundError:
            raise NotFoundError('No such document')
