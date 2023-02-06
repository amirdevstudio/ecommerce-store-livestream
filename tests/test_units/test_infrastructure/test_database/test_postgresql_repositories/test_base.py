from unittest import TestCase

from src.domain.entities.product import ProductCategory
from src.infrastructure.database.postgresql.repositories.base import BasePostgresqlRepository
from src.infrastructure.database.postgresql.orm.models.product import ProductCategory as ProductCategoryOrm
from src.infrastructure.mappers.product_category import ProductCategoryMapper


class TestBaseRepository(TestCase):
    def test_get(self):
        repository = BasePostgresqlRepository(
            orm_class=ProductCategoryOrm,
            auto_mapper=ProductCategoryMapper()
        )

        entities = [
            ProductCategory(id=None, name='test'),
            ProductCategory(id=None, name='test-2')
        ]

        result = repository.add_many(entities)

        assert result[0].id is not None
        assert result[1].id is not None
