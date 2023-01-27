from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class AbstractPaginationOptions(ABC):
    page: int
    per_page: int

    @classmethod
    @abstractmethod
    def create_default(cls):
        ...


@dataclass
class AbstractPaginatedResults(ABC):
    total: int
    items: list
    options: AbstractPaginationOptions
