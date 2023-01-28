from dataclasses import dataclass
from typing import Callable, TypeVar, Generic

from src.application.sorting import SortingOptions


@dataclass
class PaginationOptions:
    page: int
    per_page: int


_PaginatedResultsItemType = TypeVar('_PaginatedResultsItemType')
_PaginatedResultsItemMappedType = TypeVar('_PaginatedResultsItemMappedType')

@dataclass
class PaginatedResults(Generic[_PaginatedResultsItemType]):
    total: int
    items: list
    pagination_options: PaginationOptions
    sorting_options: SortingOptions

    def map_items(
            self,
            map_function: Callable[
                [_PaginatedResultsItemType],
                _PaginatedResultsItemMappedType
            ]
    ) -> 'PaginatedResults[_PaginatedResultsItemMappedType]':
        return PaginatedResults(
            total=self.total,
            items=[map_function(item) for item in self.items],
            pagination_options=self.pagination_options,
            sorting_options=self.sorting_options
        )
