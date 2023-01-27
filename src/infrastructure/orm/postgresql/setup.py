from src.infrastructure.orm.postgresql.configs import database
from src.infrastructure.orm.postgresql.models import Product, ProductCategory, ProductTag
from src.infrastructure.orm.postgresql.associations import ProductsTags, ProductsCategories

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
