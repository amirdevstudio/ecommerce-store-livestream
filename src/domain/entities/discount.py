from dataclasses import dataclass
from datetime import datetime

from src.domain.entities.base import BaseValueObject


@dataclass(frozen=True)
class BaseDiscount(BaseValueObject):
    expires_at: datetime


@dataclass(frozen=True)
class FixedDollarDiscount(BaseDiscount):
    amount: float


@dataclass(frozen=True)
class PercentageDiscount(BaseDiscount):
    percentage: float


@dataclass(frozen=True)
class TieredDollarDiscount(BaseDiscount):
    ...


@dataclass(frozen=True)
class BuyXGetYDiscount(BaseDiscount):
    ...


@dataclass(frozen=True)
class FreeShippingDiscount(BaseDiscount):
    ...


@dataclass(frozen=True)
class FreeShippingAfterCriteriaMetDiscount(BaseDiscount):
    ...
