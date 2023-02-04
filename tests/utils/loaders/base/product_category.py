from src.infrastructure.mappers.product_category import ProductCategoryMapper
from tests.utils.factories.domain.product_category import ProductCategoryFactory
from tests.utils.factories.orm.factory import OrmFactory
from tests.utils.loaders.abstract import AbstractDataLoader


class ProductCategoriesLoader(AbstractDataLoader):
    def __init__(self):
        super().__init__(
            factory=OrmFactory(
                factory=ProductCategoryFactory(),
                mapper=ProductCategoryMapper(),
            )
        )
