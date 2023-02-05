from unittest import TestCase

from amir_dev_studio.dependency_injection import add_transient_service

from src.infrastructure.database.postgresql.repositories.products import ProductRepository
from src.infrastructure.mappers.product import ProductMapper
from src.infrastructure.mappers.product_category import ProductCategoryMapper
from src.infrastructure.mappers.product_tag import ProductTagMapper


class TestBaseRepository(TestCase):
    def test_get(self):
        add_transient_service(ProductMapper)
        add_transient_service(ProductTagMapper)
        add_transient_service(ProductCategoryMapper)

        repository = ProductRepository()
        result = repository.get()

        print(result)
