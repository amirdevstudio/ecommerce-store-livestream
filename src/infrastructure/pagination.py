from dataclasses import dataclass

from src.application.interfaces.pagination import AbstractPaginationOptions, AbstractPaginatedResults


@dataclass
class PaginationOptions(AbstractPaginationOptions):

    @classmethod
    def create_default(cls):
        return cls(
            page=1,
            per_page=10
        )


@dataclass
class PaginatedResults(AbstractPaginatedResults):
    ...
