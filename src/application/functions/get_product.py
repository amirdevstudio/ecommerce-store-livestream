from amir_dev_studio.dependency_injection import get_service

from src.application.interfaces.functions import AbstractFunction
from src.application.interfaces.repositories import AbstractProductRepository


class GetProduct(AbstractFunction):
    def call(self, product_id: int):
        repository = get_service(AbstractProductRepository)
        return repository.get_by_id(product_id)
