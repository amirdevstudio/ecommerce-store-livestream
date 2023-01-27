from peewee import CharField, DecimalField

from src.infrastructure.database.postgresql.orm.configs import BaseModel


class Product(BaseModel):
    name = CharField()
    price = DecimalField()
    description = CharField()


class ProductCategory(BaseModel):
    name = CharField()


class ProductTag(BaseModel):
    name = CharField()
