from abc import ABC, abstractmethod
from typing import Generic, TypeVar, List

from src.application.query_filters import QueryFilters
from src.application.sorting import SortingOptions
from src.domain.models.product import Product

_EntityType = TypeVar("_EntityType")
_EntityIdType = TypeVar("_EntityIdType")


class AbstractRepository(ABC, Generic[_EntityType, _EntityIdType]):
    @abstractmethod
    def get(
            self,
            filters: QueryFilters,
            sorting_options: SortingOptions,
            pagination_options
    ) -> List[_EntityType]:
        ...

    @abstractmethod
    def get_by_id(self, entity_id: _EntityIdType, *args, **kwargs) -> _EntityType:
        ...

    @abstractmethod
    def add(self, entity: _EntityType, *args, **kwargs) -> _EntityType:
        ...

    @abstractmethod
    def update(self, entity: _EntityType, *args, **kwargs) -> _EntityType:
        ...

    @abstractmethod
    def delete(self, entity_id: _EntityIdType, *args, **kwargs) -> None:
        ...


class AbstractProductRepository(AbstractRepository[Product, int], ABC):
    ...
