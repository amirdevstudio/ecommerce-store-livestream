from collections import defaultdict

from amir_dev_studio.dependency_injection import get_service

from src.application.interfaces.repositories import (
    AbstractProductRepository,
    AbstractProductCategoriesRepository,
    AbstractProductTagsRepository
)
from src.application.pagination import PaginationOptions
from src.application.query_filters import QueryFilters, QueryFilterRecipes
from src.application.sorting import SortingOptions
from src.domain.models.product import Product
from src.infrastructure.database.postgresql.orm.associations import ProductsTags
from src.infrastructure.database.postgresql.orm.models.product import Product as ProductDbModel
from src.infrastructure.database.postgresql.repositories.base import BasePostgresqlRepository
from src.infrastructure.mappers.product import ProductOrmMapper


class ProductRepository(
    BasePostgresqlRepository[Product, int],
    AbstractProductRepository
):
    def _get_orm_class(self) -> type:
        return ProductDbModel

    def _get_entity_mapper(self) -> ProductOrmMapper:
        return get_service(ProductOrmMapper)

    def get(
            self,
            filters: QueryFilters = None,
            pagination_options: PaginationOptions = None,
            sorting_options: SortingOptions = None
    ):
        # using thread lock because peewee is thread safe but
        with self._thread_lock:
            paginated_results = super().get(filters, pagination_options, sorting_options)
            products = paginated_results.items
            product_ids = [product.id for product in paginated_results.items]

            query_filters = QueryFilterRecipes.where_field_in_values('product_id', product_ids)

            categories_repository = get_service(AbstractProductCategoriesRepository)
            categories_lookup = defaultdict(list)

            categories = categories_repository.get(filters=query_filters)
            for category in categories.items:
                categories_lookup[category.product_id].append(category)

            tags_repository = get_service(AbstractProductTagsRepository)
            tags_lookup = defaultdict(list)

            tags = tags_repository.get(filters=query_filters)
            for tag in tags.items:
                tags_lookup[tag.product_id].append(tag)

            for product in products:
                product.tags = tags_lookup.get(product.id, [])
                product.categories = categories_lookup.get(product.id, [])

            return paginated_results

    def add(self, product: Product, *args, **kwargs):
        categories_repository = get_service(AbstractProductCategoriesRepository)
        tags_repository = get_service(AbstractProductTagsRepository)

        # add tags and categories

        categories_repository.add_many(product.categories)
        tags_repository.add_many(product.tags)

        # add tag_associations and category_associations

        tags_query_filters = QueryFilterRecipes.where_field_in_values('name', [tag.name for tag in product.tags])
        tags = tags_repository.get(filters=tags_query_filters)

        categories_query = QueryFilterRecipes.where_field_in_values('name', [category.name for category in product.categories])
        categories = categories_repository.get(filters=categories_query)

        products_tags = [ProductsTags(product_id=product.id, tag_id=tag.id) for tag in tags.items]
        products_categories = [ProductsTags(product_id=product.id, tag_id=category.id) for category in categories.items]

        # add product

        super().add(product)
