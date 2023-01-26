from peewee import ForeignKeyField

from src.infrastructure.orm.models import Product, ProductCategory, ProductTag
from src.infrastructure.orm.configs import BaseAssociation


class ProductsTags(BaseAssociation):
    product_id = ForeignKeyField(Product, backref='tags')
    tag_id = ForeignKeyField(ProductTag, backref='products')

    class Meta(BaseAssociation.Meta):
        table_name = 'products_tags'


class ProductsCategories(BaseAssociation):
    product_id = ForeignKeyField(Product, backref='categories')
    category_id = ForeignKeyField(ProductCategory, backref='products')

    class Meta(BaseAssociation.Meta):
        table_name = 'products_categories'
