from src.infrastructure.mappers.product import ProductMapper
from tests.utils.factories.domain.product import ProductFactory
from tests.utils.factories.orm.factory import OrmFactory
from tests.utils.loaders.abstract import AbstractDataLoader


class ProductLoader(AbstractDataLoader):
    def __init__(self):
        super().__init__(
            factory=OrmFactory(
                factory=ProductFactory(),
                mapper=ProductMapper(),
            )
        )
