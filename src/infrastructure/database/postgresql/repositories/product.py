from amir_dev_studio.dependency_injection import get_service

from src.application.interfaces.repositories import AbstractProductRepository
from src.domain.models.product import Product
from src.infrastructure.database.postgresql.mappers.product import ProductOrmMapper
from src.infrastructure.database.postgresql.orm.models import Product as ProductDbModel
from src.infrastructure.database.postgresql.repositories.base import BasePostgresqlRepository


class ProductRepository(
    BasePostgresqlRepository[Product, int],
    AbstractProductRepository
):
    def __init__(self):
        self.orm_mapper = get_service(ProductOrmMapper)

    def get_orm_class(self) -> type:
        return ProductDbModel

    def get_orm_mapper(self) -> ProductOrmMapper:
        return self.orm_mapper
