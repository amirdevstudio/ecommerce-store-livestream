from unittest import TestCase

from amir_dev_studio.dependency_injection import add_transient_service

from src.domain.entities.product import Product
from src.infrastructure.database.postgresql.repositories.products import ProductRepository
from src.infrastructure.mappers.product import ProductMapper
from src.infrastructure.mappers.product_category import ProductCategoryMapper
from src.infrastructure.mappers.product_tag import ProductTagMapper


class TestBaseRepository(TestCase):
    def _add_dependencies(self):
        add_transient_service(ProductMapper)
        add_transient_service(ProductTagMapper)
        add_transient_service(ProductCategoryMapper)

    def test_get(self):
        self._add_dependencies()
        repository = ProductRepository()
        result = repository.get()

        print(result)

    def test_add(self):
        self._add_dependencies()
        product = Product(
            id=None,
            name='test',
            description='test',
            price=100,
            tags=[],
            categories=[]
        )
        repository = ProductRepository()
        result = repository.add(product)
