from amir_dev_studio.dependency_injection import get_service

from src.application.interfaces.repositories import AbstractProductTagsRepository
from src.domain.models.product import ProductTag
from src.infrastructure.database.postgresql.orm.models.product import ProductTag as ProductTagDbModel
from src.infrastructure.database.postgresql.repositories.base import BasePostgresqlRepository
from src.infrastructure.mappers.product_tag import ProductTagOrmMapper


class ProductTagsRepository(
    BasePostgresqlRepository[ProductTag, int],
    AbstractProductTagsRepository
):
    def _get_orm_class(self) -> type:
        return ProductTagDbModel

    def _get_entity_mapper(self) -> ProductTagOrmMapper:
        return get_service(ProductTagOrmMapper)
