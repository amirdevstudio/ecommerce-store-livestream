from dataclasses import dataclass, field
from typing import List

from src.domain.models.base import BaseModel


@dataclass
class ProductCategory(BaseModel):
    name: str


@dataclass
class ProductTag(BaseModel):
    name: str


@dataclass
class Product(BaseModel):
    name: str
    price: float
    description: str
    categories: List[ProductCategory] = field(default_factory=list)
    tags: List[ProductTag] = field(default_factory=list)
