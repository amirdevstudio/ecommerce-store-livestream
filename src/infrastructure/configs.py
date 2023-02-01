from amir_dev_studio.dependency_injection import (
    add_abstract_singleton_service,
    add_singleton_service
)

from src.application.interfaces.functions import AbstractFunctionExecutor
from src.application.interfaces.repositories import (
    AbstractProductRepository,
    AbstractProductCategoriesRepository,
    AbstractProductTagsRepository
)
from src.infrastructure.mappers.product import ProductOrmMapper
from src.infrastructure.mappers.product_category import ProductCategoryOrmMapper
from src.infrastructure.mappers.product_tag import ProductTagOrmMapper
from src.infrastructure.database.postgresql.repositories.product_categories import ProductCategoriesRepository
from src.infrastructure.database.postgresql.repositories.product_tags import ProductTagsRepository
from src.infrastructure.database.postgresql.repositories.products import ProductRepository
from src.infrastructure.functions.base import FunctionExecutor


def configure_dependencies():
    add_abstract_singleton_service(AbstractFunctionExecutor, FunctionExecutor)
    add_abstract_singleton_service(AbstractProductRepository, ProductRepository)
    add_abstract_singleton_service(AbstractProductCategoriesRepository, ProductCategoriesRepository)
    add_abstract_singleton_service(AbstractProductTagsRepository, ProductTagsRepository)
    add_singleton_service(ProductOrmMapper)
    add_singleton_service(ProductCategoryOrmMapper)
    add_singleton_service(ProductTagOrmMapper)
