from peewee import CharField, DecimalField

from src.infrastructure.orm.configs import BaseModel


class Product(BaseModel):
    name = CharField()
    price = DecimalField()
    description = CharField()

    class Meta(BaseModel.Meta):
        table_name = 'products'


class ProductCategory(BaseModel):
    name = CharField()

    class Meta(BaseModel.Meta):
        table_name = 'product_categories'


class ProductTag(BaseModel):
    name = CharField()

    class Meta(BaseModel.Meta):
        table_name = 'product_tags'
