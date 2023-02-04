from logging import getLogger

from tests.utils.loaders.base.product_tag import ProductTagsLoader
from tests.utils.loaders.base.product import ProductLoader
from tests.utils.loaders.base.product_category import ProductCategoriesLoader
from tests.utils.loaders.many_to_many.products_categories import ProductsToCategoriesLoader
from tests.utils.loaders.many_to_many.products_tags import ProductsToTagsLoader


class DataLoader:
    def __init__(self):
        self.logger = getLogger(__name__)

    def load(self):
        base_loaders = {
            'products': ProductLoader(),
            'product_tags': ProductTagsLoader(),
            'product_categories': ProductCategoriesLoader()
        }

        for loader in base_loaders.values():
            loader.load()
            self.logger.info(f'Loaded {loader.__class__.__name__} data')

        many_to_many_loaders = {
            'products_tags': ProductsToTagsLoader(
                products=base_loaders['products'].loaded_orm_entities,
                tags=base_loaders['product_tags'].loaded_orm_entities
            ),
            'products_categories': ProductsToCategoriesLoader(
                products=base_loaders['products'].loaded_orm_entities,
                categories=base_loaders['product_categories'].loaded_orm_entities
            )
        }

        for loader in many_to_many_loaders.values():
            loader.load()
            self.logger.info(f'Loaded {loader.__class__.__name__} data')
