from peewee import ForeignKeyField

from src.infrastructure.database.postgresql.orm.models.product import Product, ProductCategory, ProductTag
from src.infrastructure.database.postgresql.orm.configs import BaseAssociation


class ProductToTag(BaseAssociation):
    product_id = ForeignKeyField(Product, backref='tags')
    tag_id = ForeignKeyField(ProductTag, backref='products')


class ProductToCategory(BaseAssociation):
    product_id = ForeignKeyField(Product, backref='categories')
    category_id = ForeignKeyField(ProductCategory, backref='products')
