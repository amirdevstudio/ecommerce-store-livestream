from src.infrastructure.database.postgresql.orm.relations import ProductTagRelation
from tests.utils.factories.abstract import AbstractFactory


class ProductsToTagsFactory(AbstractFactory):
    def create(self, product_id: int, tag_id: int):
        return ProductTagRelation(
            product_id=product_id,
            tag_id=tag_id,
        )
