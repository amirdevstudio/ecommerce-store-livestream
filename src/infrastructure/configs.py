from amir_dev_studio.dependency_injection import (
    add_abstract_singleton_service,
    add_singleton_service
)

from src.application.interfaces.repositories import AbstractProductRepository
from src.infrastructure.database.postgresql.mappers.product import ProductOrmMapper
from src.infrastructure.database.postgresql.repositories.product import ProductRepository


def configure_dependencies():
    add_abstract_singleton_service(AbstractProductRepository, ProductRepository)
    add_singleton_service(ProductOrmMapper)
