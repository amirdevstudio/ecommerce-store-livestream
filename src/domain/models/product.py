from dataclasses import dataclass
from typing import List


@dataclass
class ProductCategory:
    name: str


@dataclass
class ProductTag:
    name: str


@dataclass
class Product:
    name: str
    categories: List[ProductCategory]
    price: float
    description: str
    tags: List[ProductTag]
