from datetime import datetime

from amir_dev_studio.dependency_injection import get_service

from src.application.interfaces.functions import AbstractFunction
from src.application.interfaces.repositories import AbstractProductRepository


class SoftDeleteProduct(AbstractFunction):
    def __init__(self):
        self.repository = get_service(AbstractProductRepository)

    def call(self, product_id: int):
        product = self.repository.get_by_id(product_id)

        if not product:
            raise ValueError(f"Product not found for ID: {product_id}")

        product.deleted_at = datetime.utcnow()
        product = self.repository.update(product)

        return product
