from dataclasses import dataclass
from typing import List

from src.domain.models.abstract import AbstractModel


@dataclass
class ProductCategory(AbstractModel):
    name: str


@dataclass
class ProductTag(AbstractModel):
    name: str


@dataclass
class Product(AbstractModel):
    name: str
    categories: List[ProductCategory]
    price: float
    description: str
    tags: List[ProductTag]
