from abc import ABC, abstractmethod
from typing import Generic, TypeVar, Optional, List

from src.application.pagination import PaginatedResults, PaginationOptions
from src.application.query_filters import QueryFilters
from src.application.sorting import SortingOptions
from src.domain.models.product import Product, ProductCategory, ProductTag

_EntityType = TypeVar("_EntityType")
_EntityIdType = TypeVar("_EntityIdType")


class AbstractRepository(ABC, Generic[_EntityType, _EntityIdType]):
    @abstractmethod
    def get(
            self,
            filters: Optional[QueryFilters] = None,
            sorting_options: Optional[SortingOptions] = None,
            pagination_options: Optional[PaginationOptions] = None
    ) -> PaginatedResults[_EntityType]:
        ...

    @abstractmethod
    def get_by_id(self, entity_id: _EntityIdType, *args, **kwargs) -> Optional[_EntityType]:
        ...

    @abstractmethod
    def add(self, entity: _EntityType, *args, **kwargs) -> _EntityType:
        ...

    @abstractmethod
    def add_many(self, entities: List[_EntityType], *args, **kwargs) -> List[_EntityType]:
        ...

    @abstractmethod
    def update(self, entity: _EntityType, *args, **kwargs) -> _EntityType:
        ...

    @abstractmethod
    def delete(self, entity_id: _EntityIdType, *args, **kwargs) -> None:
        ...


class AbstractProductRepository(AbstractRepository[Product, int], ABC):
    ...


class AbstractProductCategoriesRepository(AbstractRepository[ProductCategory, int], ABC):
    ...


class AbstractProductTagsRepository(AbstractRepository[ProductTag, int], ABC):
    ...
