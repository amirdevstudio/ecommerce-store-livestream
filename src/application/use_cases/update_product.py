from amir_dev_studio.dependency_injection import get_service

from src.application.interfaces.functions import AbstractUseCase
from src.application.interfaces.repositories import AbstractProductRepository
from src.domain.entities.product import Product


class UpdateProduct(AbstractUseCase):
    def __init__(self):
        self.repository = get_service(AbstractProductRepository)
        
    def call(self, product_id: int, product: Product):
        if not product.id:
            product.id = product_id

        if product.id != product_id:
            raise ValueError("Product ID does not match the given ID")

        return self.repository.update(product)
