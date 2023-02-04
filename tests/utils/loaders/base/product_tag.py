from src.infrastructure.mappers.product_tag import ProductTagMapper
from tests.utils.factories.domain.product_tag import ProductTagFactory
from tests.utils.factories.orm.factory import OrmFactory
from tests.utils.loaders.abstract import AbstractDataLoader


class ProductTagsLoader(AbstractDataLoader):
    def __init__(self):
        super().__init__(
            factory=OrmFactory(
                factory=ProductTagFactory(),
                mapper=ProductTagMapper(),
            )
        )
