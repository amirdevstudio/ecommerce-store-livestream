from abc import ABC
from dataclasses import dataclass


@dataclass
class AbstractPaginationOptions(ABC):
    page: int
    per_page: int
    is_zero_based: bool = False

    @classmethod
    def create_default(cls):
        return cls(1, 10)


@dataclass
class AbstractPaginationResult(ABC):
    total: int
    items: list
    options: AbstractPaginationOptions
