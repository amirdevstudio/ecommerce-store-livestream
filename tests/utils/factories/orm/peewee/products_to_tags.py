from src.infrastructure.database.postgresql.orm.associations import ProductToTag
from tests.utils.factories.abstract import AbstractFactory


class ProductsToTagsFactory(AbstractFactory):
    def create(self, product_id: int, tag_id: int):
        return ProductToTag(
            product_id=product_id,
            tag_id=tag_id,
        )
