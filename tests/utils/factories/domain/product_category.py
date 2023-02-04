from src.domain.entities.product import ProductCategory
from tests.utils.factories.abstract import AbstractFactory


class ProductCategoryFactory(AbstractFactory):
    def create(self, __id: int = None):
        return ProductCategory(
            id=__id,
            name='Product Category Name'
        )
