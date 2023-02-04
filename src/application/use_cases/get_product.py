from amir_dev_studio.dependency_injection import get_service

from src.application.interfaces.functions import AbstractUseCase
from src.application.interfaces.repositories import AbstractProductRepository


class GetProduct(AbstractUseCase):
    def __init__(self):
        self.repository = get_service(AbstractProductRepository)
        
    def call(self, product_id: int):
        return self.repository.get_by_id(product_id)
