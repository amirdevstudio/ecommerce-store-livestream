from logging import getLogger

from tests.utils.factories.orm.factory import ProductTagsLoader
from tests.utils.factories.orm.peewee.products_to_tags import ProductsLoader


class DataLoader:
    def __init__(self):
        self.logger = getLogger(__name__)

    def execute(self):
        base_loaders = {
            'products': ProductsLoader(),
            'product_tags': ProductTagsLoader()
        }

        for loader in base_loaders.values():
            loader.load()
            self.logger.info(f'Loaded {loader.__class__.__name__} data')

        many_to_many_loaders = [
            ProductsToTagsLoader(
                products=base_loaders['products'].loaded_data,
                tags=base_loaders['product_tags'].loaded_data
            ),
        ]

        for loader in many_to_many_loaders:
            loader.load()
            self.logger.info(f'Loaded {loader.__class__.__name__} data')
