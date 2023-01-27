from peewee import CharField, DecimalField

from src.infrastructure.orm.postgresql.configs import BaseModel


class Product(BaseModel):
    name = CharField()
    price = DecimalField()
    description = CharField()


class ProductCategory(BaseModel):
    name = CharField()


class ProductTag(BaseModel):
    name = CharField()
