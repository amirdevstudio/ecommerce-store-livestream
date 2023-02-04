from random import random, choices
from typing import List

from src.infrastructure.database.postgresql.orm.associations import ProductCategoryRelation
from src.infrastructure.database.postgresql.orm.models.product import Product, ProductCategory
from tests.utils.loaders.many_to_many.abstract import AbstractManyToManyDataLoader


class ProductsToCategoriesLoader(AbstractManyToManyDataLoader):
    def __init__(self, products: List[Product], categories: List[ProductCategory]):
        super().__init__()
        self.products = products
        self.categories = categories

    def load(self, *args, **kwargs):
        for product in self.products:
            product_categories = choices(self.categories, k=5)
            for category in product_categories:
                entity = ProductCategoryRelation(
                    product_id=product.id,
                    category_id=category.id,
                )
                entity.save()
                self.loaded_entities.append(entity)
