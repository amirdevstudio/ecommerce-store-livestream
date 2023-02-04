from src.infrastructure.database.postgresql.orm.configs import database
from src.infrastructure.database.postgresql.orm.models.product import Product, ProductCategory, ProductTag
from src.infrastructure.database.postgresql.orm.associations import ProductTagRelation, ProductCategoryRelation

_models = [
    Product,
    ProductCategory,
    ProductTag,
    ProductTagRelation,
    ProductCategoryRelation
]

def reset_tables() -> None:
    database.connect()
    database.drop_tables(_models, cascade=True)
    database.create_tables(_models)
    database.close()
