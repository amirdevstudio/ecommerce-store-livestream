from src.infrastructure.orm.configs import database
from src.infrastructure.orm.models import Product, ProductCategory, ProductTag
from src.infrastructure.orm.associations import ProductsTags, ProductsCategories

_models = [
    Product,
    ProductCategory,
    ProductTag,
    ProductsTags,
    ProductsCategories
]

def reset_tables() -> None:
    database.connect()
    database.drop_tables(_models)
    database.create_tables(_models)
    database.close()
