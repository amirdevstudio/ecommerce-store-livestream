from amir_dev_studio.dependency_injection import get_service

from src.application.interfaces.repositories import AbstractProductCategoriesRepository
from src.domain.models.product import ProductCategory
from src.infrastructure.mappers.product_category import ProductCategoryOrmMapper
from src.infrastructure.database.postgresql.orm.models.product import ProductCategory as ProductCategoryDbModel
from src.infrastructure.database.postgresql.repositories.base import BasePostgresqlRepository


class ProductCategoriesRepository(
    BasePostgresqlRepository[ProductCategory, int],
    AbstractProductCategoriesRepository
):
    def _get_orm_class(self) -> type:
        return ProductCategoryDbModel

    def _get_entity_mapper(self) -> ProductCategoryOrmMapper:
        return get_service(ProductCategoryOrmMapper)
