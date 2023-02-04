from amir_dev_studio.dependency_injection import (
    add_abstract_singleton_service,
    add_singleton_service
)

from src.application.interfaces.functions import AbstractUseCaseExecutor
from src.application.interfaces.repositories import (
    AbstractProductRepository,
    AbstractProductCategoriesRepository,
    AbstractProductTagsRepository
)
from src.infrastructure.mappers.product import ProductMapper
from src.infrastructure.mappers.product_category import ProductCategoryMapper
from src.infrastructure.mappers.product_tag import ProductTagMapper
from src.infrastructure.database.postgresql.repositories.product_categories import ProductCategoriesRepository
from src.infrastructure.database.postgresql.repositories.product_tags import ProductTagsRepository
from src.infrastructure.database.postgresql.repositories.products import ProductRepository
from src.infrastructure.functions.base import FunctionExecutor


def configure_dependencies():
    add_abstract_singleton_service(AbstractUseCaseExecutor, FunctionExecutor)
    add_abstract_singleton_service(AbstractProductRepository, ProductRepository)
    add_abstract_singleton_service(AbstractProductCategoriesRepository, ProductCategoriesRepository)
    add_abstract_singleton_service(AbstractProductTagsRepository, ProductTagsRepository)
    add_singleton_service(ProductMapper)
    add_singleton_service(ProductCategoryMapper)
    add_singleton_service(ProductTagMapper)
