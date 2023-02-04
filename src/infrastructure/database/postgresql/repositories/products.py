from collections import defaultdict

from amir_dev_studio.dependency_injection import get_service

from src.application.interfaces.repositories import (
    AbstractProductRepository,
    AbstractProductCategoriesRepository,
    AbstractProductTagsRepository, AbstractProductToCategoryRepository
)
from src.application.pagination import PaginationOptions
from src.application.query_filters import QueryFilters, QueryFilterTemplates
from src.application.sorting import SortingOptions
from src.domain.entities.product import Product, ProductCategory, ProductTag
from src.infrastructure.database.postgresql.orm.associations import ProductToTag, ProductToCategory
from src.infrastructure.database.postgresql.orm.extensions.peewee import PeeweeSelectQueryExtension
from src.infrastructure.database.postgresql.orm.models.product import Product as ProductDbModel, ProductCategory as ProductCategoryDbModel
from src.infrastructure.database.postgresql.repositories.base import BasePostgresqlRepository
from src.infrastructure.database.postgresql.repositories.product_categories import ProductCategoriesRepository
from src.infrastructure.database.postgresql.repositories.product_tags import ProductTagsRepository
from src.infrastructure.mappers.product import ProductMapper


class ProductRepository(
    BasePostgresqlRepository[Product, int],
    AbstractProductRepository
):
    def __init__(self):
        super().__init__(
            orm_class=ProductDbModel,
            auto_mapper=get_service(ProductMapper)
        )
        self.categories_repository = get_service(AbstractProductCategoriesRepository)
        self.categories_link_repository = get_service(AbstractProductToCategoryRepository)
        self.tags_repository = get_service(AbstractProductTagsRepository)
        self.tags_link_repository = get_service(AbstractProductToCategoryRepository)

    def get(
            self,
            filters: QueryFilters = None,
            pagination_options: PaginationOptions = None,
            sorting_options: SortingOptions = None
    ):
        products = super().get(filters, pagination_options, sorting_options)
        product_ids = [product.id for product in products.items]

        query = ProductCategoryDbModel.select().join(ProductToCategory).where(
            ProductToCategory.product_id.in_(product_ids)
        )

        for repository, link_model in [
            (self.categories_repository, ProductToCategory),
            (self.tags_repository, ProductToTag)
        ]:
            query_filters = QueryFilterTemplates.where_field_in_values(
                field_='product_id',
                value=product_ids
            )

            query = link_model.select()
            query_extended = PeeweeSelectQueryExtension(query)
            query_extended.apply_filters(query_filters)
            query_result = query_extended.query.execute()

        product_category_links = self.categories_link_repository.get(filters=query_filters)
        product_tag_links = self.tags_link_repository.get(filters=query_filters)

        categories_lookup = defaultdict(list)
        categories = self.categories_repository.get(filters=query_filters)

        for category in categories.items:
            categories_lookup[category.product_id].append(category)

        tags_lookup = defaultdict(list)
        tags = self.tags_repository.get(filters=query_filters)

        for tag in tags.items:
            tags_lookup[tag.product_id].append(tag)

        for product in products:
            product.tags = tags_lookup.get(product.id, [])
            product.categories = categories_lookup.get(product.id, [])

        return paginated_results

    def add(self, product: Product, *args, **kwargs):
        categories_repository = get_service(AbstractProductCategoriesRepository)
        products_categories_repository = get_service(AbstractProductToCategoryRepository)
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

        products_tags = [ProductToTag(product_id=product.id, tag_id=tag.id) for tag in tags.items]
        products_categories = [ProductToCategory(product_id=product.id, tag_id=category.id) for category in categories.items]

        products_tags_repository.add_many(products_tags)
        products_categories_repository.add_many(products_categories)
        # add product

        super().add(product)
