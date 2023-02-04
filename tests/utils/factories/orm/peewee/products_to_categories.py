from src.infrastructure.database.postgresql.orm.associations import ProductToCategory
from tests.utils.factories.abstract import AbstractFactory


class ProductsToCategoriesFactory(AbstractFactory):
    def create(self, product_id: int, category_id: int):
        return ProductToCategory(
            product_id=product_id,
            category_id=category_id,
        )
