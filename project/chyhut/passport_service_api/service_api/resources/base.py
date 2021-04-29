from typing import Dict

from flask_restful import Resource


class SmokeResource(Resource):

    @staticmethod
    def get() -> Dict[str, str]:
        return {'hello': 'world'}