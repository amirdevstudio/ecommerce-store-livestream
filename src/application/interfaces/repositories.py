from abc import ABC, abstractmethod
from typing import Generic, TypeVar, Optional, List

from src.application.pagination import PaginatedResults, PaginationOptions
from src.application.query_filters import QueryFilters
from src.application.sorting import SortingOptions
from src.domain.entities.product import Product, ProductCategory, ProductTag

_ModelType = TypeVar("_ModelType")
_ModelIdType = TypeVar("_ModelIdType")


class AbstractRepository(ABC, Generic[_ModelType, _ModelIdType]):
    @abstractmethod
    def get(
            self,
            filters: Optional[QueryFilters] = None,
            sorting_options: Optional[SortingOptions] = None,
            pagination_options: Optional[PaginationOptions] = None
    ) -> PaginatedResults[_ModelType]:
        ...

    @abstractmethod
    def get_by_id(self, entity_id: _ModelIdType, *args, **kwargs) -> Optional[_ModelType]:
        ...

    @abstractmethod
    def add(self, entity: _ModelType, *args, **kwargs) -> _ModelType:
        ...

    @abstractmethod
    def add_many(self, entities: List[_ModelType], *args, **kwargs) -> List[int]:
        ...

    @abstractmethod
    def update(self, entity: _ModelType, *args, **kwargs) -> _ModelType:
        ...

    @abstractmethod
    def delete(self, entity_id: _ModelIdType, *args, **kwargs) -> bool:
        ...


class AbstractProductRepository(AbstractRepository[Product, int], ABC):
    ...


class AbstractProductCategoriesRepository(AbstractRepository[ProductCategory, int], ABC):
    ...


class AbstractProductTagsRepository(AbstractRepository[ProductTag, int], ABC):
    ...


class AbstractProductCategoryRelationRepository(AbstractRepository[ProductCategory, int], ABC):
    ...


class AbstractProductTagRelationRepository(AbstractRepository[ProductTag, int], ABC):
    ...
