from abc import abstractmethod
from typing import TypeVar, List, Generic, Type

from src.application.interfaces.repositories import AbstractRepository
from src.infrastructure.orm.postgresql.mappers import AbstractOrmMapper

_EntityType = TypeVar("_EntityType")
_EntityIdType = TypeVar("_EntityIdType")


class BasePostgresqlRepository(
    AbstractRepository[_EntityType, _EntityIdType],
    Generic[_EntityType, _EntityIdType]
):
    @abstractmethod
    def get_orm_class(self) -> Type:
        ...

    @abstractmethod
    def get_orm_mapper(self) -> AbstractOrmMapper:
        ...

    def get(self, *args, **kwargs) -> List[_EntityType]:
        pass

    def get_by_id(self, entity_id: _EntityIdType, *args, **kwargs) -> _EntityType:
        pass

    def add(self, entity: _EntityType, *args, **kwargs):
        pass

    def update(self, entity: _EntityType, *args, **kwargs):
        pass

    def delete(self, entity_id: _EntityIdType, *args, **kwargs):
        pass
