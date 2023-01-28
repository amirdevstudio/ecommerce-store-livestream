from amir_dev_studio.dependency_injection import get_service

from src.application.interfaces.functions import AbstractFunction
from src.application.interfaces.repositories import AbstractProductRepository
from src.domain.models.product import Product


class UpdateProduct(AbstractFunction):
    def call(self, product_id: int, product: Product):
        if not product.id:
            product.id = product_id

        if product.id != product_id:
            raise ValueError("Product ID does not match the given ID")

        repository = get_service(AbstractProductRepository)
        return repository.update(product)
