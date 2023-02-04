from amir_dev_studio.dependency_injection import get_service

from src.application.interfaces.repositories import AbstractProductCategoriesRepository
from src.domain.entities.product import ProductCategory
from src.infrastructure.mappers.product_category import ProductCategoryMapper
from src.infrastructure.database.postgresql.orm.models.product import ProductCategory as ProductCategoryDbModel
from src.infrastructure.database.postgresql.repositories.base import BasePostgresqlRepository


class ProductCategoriesRepository(
    BasePostgresqlRepository[ProductCategory, int],
    AbstractProductCategoriesRepository
):
    def __init__(self):
        super().__init__(
            orm_class=ProductCategoryDbModel,
            auto_mapper=get_service(ProductCategoryMapper)
        )
