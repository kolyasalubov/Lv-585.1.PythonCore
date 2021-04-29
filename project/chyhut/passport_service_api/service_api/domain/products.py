from typing import List

from service_api.models import Product


def get_products(**kwargs) -> List[Product]:
    return Product.query.filter_by(**kwargs).all()
