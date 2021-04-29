from functools import wraps

from service_api.app import db


def db_session(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs, session=db.session)
        db.session.commit()
        return result

    return wrapper
