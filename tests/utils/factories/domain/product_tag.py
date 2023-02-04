from src.domain.entities.product import ProductTag
from tests.utils.factories.abstract import AbstractFactory


class ProductTagFactory(AbstractFactory):
    def create(self, __id: int = None):
        return ProductTag(
            id=__id,
            name='Product Tag Name'
        )
