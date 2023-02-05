from amir_dev_studio.dependency_injection import get_service
from peewee import prefetch

from src.application.interfaces.repositories import (
    AbstractProductRepository,
    AbstractProductCategoriesRepository,
    AbstractProductTagsRepository,
    AbstractProductCategoryRelationRepository
)
from src.application.pagination import PaginationOptions, PaginatedResults
from src.application.query_filters import QueryFilters, QueryFilterTemplates
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
        categories_repository = get_service(AbstractProductCategoriesRepository)
        products_categories_repository = get_service(AbstractProductCategoryRelationRepository)
        products_tags_repository = get_service(AbstractProductTagsRepository)
        tags_repository = get_service(AbstractProductTagsRepository)

        # add tags and categories

        categories_repository.add_many(product.categories)
        tags_repository.add_many(product.tags)

        # add tag_associations and category_associations

        tags_query_filters = QueryFilterTemplates.where_field_in_values('name', [tag.name for tag in product.tags])
        tags = tags_repository.get(filters=tags_query_filters)

        categories_query = QueryFilterTemplates.where_field_in_values('name', [category.name for category in product.categories])
        categories = categories_repository.get(filters=categories_query)

        products_tags = [ProductTagRelation(product_id=product.id, tag_id=tag.id) for tag in tags.items]
        products_categories = [ProductCategoryRelation(product_id=product.id, tag_id=category.id) for category in categories.items]

        products_tags_repository.add_many(products_tags)
        products_categories_repository.add_many(products_categories)
        # add product

        super().add(product)
