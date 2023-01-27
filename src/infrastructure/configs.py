from amir_dev_studio.dependency_injection import (
    add_abstract_singleton_service,
    add_singleton_service
)

from src.application.interfaces.repositories import AbstractProductRepository
from src.application.interfaces.functions import AbstractFunctionExecutor
from src.infrastructure.database.postgresql.mappers.product import ProductOrmMapper
from src.infrastructure.database.postgresql.repositories.product import ProductRepository
from src.infrastructure.functions.base import FunctionExecutor


def configure_dependencies():
    add_abstract_singleton_service(AbstractProductRepository, ProductRepository)
    add_abstract_singleton_service(AbstractFunctionExecutor, FunctionExecutor)
    add_singleton_service(ProductOrmMapper)
