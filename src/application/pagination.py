from dataclasses import dataclass


@dataclass
class PaginationOptions:
    page: int
    per_page: int

    @classmethod
    def create_default(cls):
        return cls(
            page=1,
            per_page=10
        )


@dataclass
class PaginatedResults:
    total: int
    items: list
    options: PaginationOptions
