from src.domain.entities.product import Product
from tests.utils.factories.abstract import AbstractFactory
from tests.utils.factories.domain.product_category import ProductCategoryFactory
from tests.utils.factories.domain.product_tag import ProductTagFactory


class ProductFactory(AbstractFactory):
    def create(self, __id: int = None):
        if self.load_dependencies:
            categories = ProductCategoryFactory().create_many(10)
            tags = ProductTagFactory().create_many(10)

        else:
            categories = []
            tags = []

        return Product(
            id=__id,
            name='Product Name',
            description='Product Description',
            price=100.0,
            categories=categories,
            tags=tags
        )
