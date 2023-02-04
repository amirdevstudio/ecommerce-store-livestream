from src.infrastructure.database.postgresql.orm.configs import database
from src.infrastructure.database.postgresql.orm.models.product import Product, ProductCategory, ProductTag
from src.infrastructure.database.postgresql.orm.associations import ProductToTag, ProductToCategory

_models = [
    Product,
    ProductCategory,
    ProductTag,
    ProductToTag,
    ProductToCategory
]

def reset_tables() -> None:
    database.connect()
    database.drop_tables(_models)
    database.create_tables(_models)
    database.close()
