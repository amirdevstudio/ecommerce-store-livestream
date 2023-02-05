from random import choices
from typing import List

from src.infrastructure.database.postgresql.orm.relations import ProductTagRelation
from src.infrastructure.database.postgresql.orm.models.product import Product, ProductTag
from tests.utils.loaders.many_to_many.abstract import AbstractManyToManyDataLoader


class ProductsToTagsLoader(AbstractManyToManyDataLoader):
    def __init__(self, products: List[Product], tags: List[ProductTag]):
        super().__init__()
        self.products = products
        self.tags = tags

    def load(self, *args, **kwargs):
        for product in self.products:
            tags = choices(self.tags, k=5)
            for tag in tags:
                entity = ProductTagRelation(
                    product_id=product.id,
                    tag_id=tag.id,
                )
                entity.save()
                self.loaded_entities.append(entity)
