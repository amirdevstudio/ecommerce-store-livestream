from peewee import ForeignKeyField

from src.infrastructure.database.postgresql.orm.models.product import Product, ProductCategory, ProductTag
from src.infrastructure.database.postgresql.orm.configs import BaseAssociation


class ProductTagRelation(BaseAssociation):
    product = ForeignKeyField(Product, backref='tag_relations', on_delete='CASCADE')
    tag = ForeignKeyField(ProductTag, backref='product_relations', on_delete='CASCADE')


class ProductCategoryRelation(BaseAssociation):
    product = ForeignKeyField(Product, backref='category_relations', on_delete='CASCADE')
    category = ForeignKeyField(ProductCategory, backref='product_relations', on_delete='CASCADE')
