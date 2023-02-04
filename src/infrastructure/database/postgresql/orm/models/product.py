from peewee import CharField, DecimalField

from src.infrastructure.database.postgresql.orm.configs import BaseEntity


class Product(BaseEntity):
    name = CharField()
    price = DecimalField()
    description = CharField()


class ProductCategory(BaseEntity):
    name = CharField()


class ProductTag(BaseEntity):
    name = CharField()
