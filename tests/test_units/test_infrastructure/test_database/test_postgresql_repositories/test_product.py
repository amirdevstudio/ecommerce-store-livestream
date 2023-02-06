from unittest import TestCase

from amir_dev_studio.dependency_injection import add_transient_service, add_abstract_singleton_service

from src.application.interfaces.repositories import AbstractProductTagsRepository, AbstractProductCategoriesRepository
from src.domain.entities.product import Product, ProductTag, ProductCategory
from src.infrastructure.database.postgresql.repositories.product_categories import ProductCategoriesRepository
from src.infrastructure.database.postgresql.repositories.product_tags import ProductTagsRepository
from src.infrastructure.database.postgresql.repositories.products import ProductRepository
from src.infrastructure.mappers.product import ProductMapper
from src.infrastructure.mappers.product_category import ProductCategoryMapper
from src.infrastructure.mappers.product_tag import ProductTagMapper


class TestBaseRepository(TestCase):
    def _add_dependencies(self):
        add_transient_service(ProductMapper)
        add_transient_service(ProductTagMapper)
        add_transient_service(ProductCategoryMapper)
        add_abstract_singleton_service(AbstractProductTagsRepository, ProductTagsRepository)
        add_abstract_singleton_service(AbstractProductCategoriesRepository, ProductCategoriesRepository)

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
            tags=[
                ProductTag(id=None, name='test'),
                ProductTag(id=None, name='test-2'),
                ProductTag(id=None, name='test-3')
            ],
            categories=[
                ProductCategory(id=None, name='test'),
                ProductCategory(id=None, name='test-2'),
            ]
        )
        repository = ProductRepository()
        result = repository.add(product)
        print(result)

        assert result.id is not None
