from amir_dev_studio.dependency_injection import get_service

from src.application.interfaces.functions import AbstractUseCase
from src.application.interfaces.repositories import AbstractProductRepository


class HardDeleteProduct(AbstractUseCase):
    def __init__(self):
        self.repository = get_service(AbstractProductRepository)

    def call(self, product_id: int):
        if not self.repository.delete(product_id):
            raise ValueError(f"Product not deleted for ID: {product_id}")
