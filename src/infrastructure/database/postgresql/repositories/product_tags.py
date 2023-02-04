from amir_dev_studio.dependency_injection import get_service

from src.application.interfaces.repositories import AbstractProductTagsRepository
from src.domain.entities.product import ProductTag
from src.infrastructure.database.postgresql.orm.models.product import ProductTag as ProductTagDbModel
from src.infrastructure.database.postgresql.repositories.base import BasePostgresqlRepository
from src.infrastructure.mappers.product_tag import ProductTagMapper


class ProductTagsRepository(
    BasePostgresqlRepository[ProductTag, int],
    AbstractProductTagsRepository
):
    def __init__(self):
        super().__init__(
            orm_class=ProductTagDbModel,
            auto_mapper=get_service(ProductTagMapper)
        )
