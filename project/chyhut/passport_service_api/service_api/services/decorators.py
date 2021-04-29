from functools import wraps

from flask import request, g

from service_api.domain.clients import get_client
from service_api.exceptions import AuthorizationError


def authenticate(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        token = request.headers.get('Authorization')
        if not token:
            raise AuthorizationError('Not authorized')

        client = get_client(client_code=token)
        if not client:
            raise AuthorizationError('Not authorized')
        g.client = client
        return func(*args, **kwargs)

    return wrapper
