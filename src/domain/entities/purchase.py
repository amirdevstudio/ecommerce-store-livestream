from dataclasses import dataclass

from src.domain.entities.base import BaseEntity


@dataclass
class Purchase(BaseEntity):
    items: list['PurchaseItem']
    total_price: float


@dataclass
class PurchaseItem(BaseEntity):
    product_id: int
    quantity: int
    price: float
