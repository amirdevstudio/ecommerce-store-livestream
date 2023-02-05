from amir_dev_studio.dependency_injection import get_service
from peewee import prefetch

from src.application.interfaces.repositories import AbstractProductRepository
from src.application.pagination import PaginationOptions, PaginatedResults
from src.application.query_filters import QueryFilters
from src.application.sorting import SortingOptions
from src.domain.entities.product import Product
from src.infrastructure.database.postgresql.orm.relations import ProductTagRelation, ProductCategoryRelation
from src.infrastructure.database.postgresql.orm.models.product import (
    Product as ProductOrm,
    ProductCategory,
    ProductTag
)
from src.infrastructure.database.postgresql.repositories.base import BasePostgresqlRepository
from src.infrastructure.mappers.product import ProductMapper


class ProductRepository(
    BasePostgresqlRepository[Product, int],
    AbstractProductRepository
):
    def __init__(self):
        super().__init__(
            orm_class=ProductOrm,
            auto_mapper=get_service(ProductMapper)
        )

    def get(
            self,
            filters: QueryFilters = None,
            pagination_options: PaginationOptions = None,
            sorting_options: SortingOptions = None
    ):
        query = self._get_query(
            filters,
            pagination_options,
            sorting_options
        )

        products = prefetch(
            query,
            ProductTagRelation,
            ProductTag,
            ProductCategoryRelation,
            ProductCategory
        )

        products = self.auto_mapper.orms_to_domains(products)
        products_count = self.count(filters=filters)

        return PaginatedResults(
            items=products,
            total=products_count,
            pagination_options=pagination_options,
            sorting_options=sorting_options
        )

    def add(self, product: Product, *args, **kwargs):
        return super().add(product, *args, **kwargs)
