from amir_dev_studio.dependency_injection import get_service
from peewee import prefetch

from src.application.interfaces.repositories import (
    AbstractProductRepository,
    AbstractProductCategoriesRepository,
    AbstractProductTagsRepository
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
        tags = []
        categories = []

        tag_repository = get_service(AbstractProductTagsRepository)
        category_repository = get_service(AbstractProductCategoriesRepository)

        def _filter_by_name(items):
            return QueryFilterTemplates.where_field_in_values('name', items)

        if product.tags:
            tag_names = set(tag.name for tag in product.tags)

            existing_tags = tag_repository.get(filters=_filter_by_name(tag_names)).items
            existing_tag_names = {tag.name for tag in existing_tags}

            tags_to_create = [
                ProductTag(name=tag_name)
                for tag_name in tag_names - existing_tag_names
            ]

            tags_created = tag_repository.add_many(tags_to_create)
            tags.extend(existing_tags + tags_created)

        if product.categories:
            category_names = set(category.name for category in product.categories)

            existing_categories = category_repository.get(filters=_filter_by_name(category_names)).items
            existing_category_names = {category.name for category in existing_categories}

            categories_to_create = [
                ProductCategory(name=category_name)
                for category_name in category_names - existing_category_names
            ]

            categories_created = category_repository.add_many(categories_to_create)
            categories.extend(existing_categories + categories_created)

        product = super().add(product, *args, **kwargs)

        tag_relations = []

        for tag in tags:
            tag_relations.append(
                ProductTagRelation(
                    product=product.id,
                    tag=tag.id
                )
            )

        category_relations = []
        for category in categories:
            category_relations.append(
                ProductCategoryRelation(
                    product=product.id,
                    category=category.id
                )
            )

        ProductTagRelation.bulk_create(tag_relations)
        ProductCategoryRelation.bulk_create(category_relations)

        return product
