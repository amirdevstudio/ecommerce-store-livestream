from amir_dev_studio.dependency_injection import get_service

from src.application.interfaces.functions import AbstractUseCase
from src.application.interfaces.repositories import AbstractProductRepository
from src.domain.entities.product import Product


class CreateProduct(AbstractUseCase):
    def __init__(self):
        self.repository = get_service(AbstractProductRepository)
        
    def call(self, product: Product):
        return self.repository.add(product)
