from peewee import ForeignKeyField

from src.infrastructure.orm.postgresql.models import Product, ProductCategory, ProductTag
from src.infrastructure.orm.postgresql.configs import BaseAssociation


class ProductsTags(BaseAssociation):
    product_id = ForeignKeyField(Product, backref='tags')
    tag_id = ForeignKeyField(ProductTag, backref='products')


class ProductsCategories(BaseAssociation):
    product_id = ForeignKeyField(Product, backref='categories')
    category_id = ForeignKeyField(ProductCategory, backref='products')
