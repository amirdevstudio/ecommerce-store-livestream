from amir_dev_studio.dependency_injection import get_service

from src.application.interfaces.repositories import AbstractProductRepository
from src.domain.models.product import Product
from src.infrastructure.orm.postgresql.mappers import ProductOrmMapper
from src.infrastructure.orm.postgresql.models import Product as ProductDbModel
from src.infrastructure.repositories.postgresql.base import BasePostgresqlRepository


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
