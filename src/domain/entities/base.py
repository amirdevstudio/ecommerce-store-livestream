from dataclasses import dataclass
from typing import Optional

from src.domain.entities.abstract import AbstractEntity


@dataclass
class BaseEntity(AbstractEntity):
    id: Optional[int]


@dataclass(frozen=True)
class BaseValueObject:
    ...
