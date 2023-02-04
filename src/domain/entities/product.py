from dataclasses import dataclass, field
from typing import List

from src.domain.entities.base import BaseEntity


@dataclass
class ProductCategory(BaseEntity):
    name: str


@dataclass
class ProductTag(BaseEntity):
    name: str


@dataclass
class Product(BaseEntity):
    name: str
    description: str
    price: float
    categories: List[ProductCategory] = field(default_factory=list)
    tags: List[ProductTag] = field(default_factory=list)
