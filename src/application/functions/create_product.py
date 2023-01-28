from amir_dev_studio.dependency_injection import get_service

from src.application.interfaces.functions import AbstractFunction
from src.application.interfaces.repositories import AbstractProductRepository
from src.domain.models.product import Product


class CreateProduct(AbstractFunction):
    def call(self, product: Product):
        repository = get_service(AbstractProductRepository)
        return repository.add(product)
