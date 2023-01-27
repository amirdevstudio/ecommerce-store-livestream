from abc import ABC, abstractmethod
from typing import Generic, TypeVar

_DomainEntity = TypeVar("_DomainEntity")
_OrmEntity = TypeVar("_OrmEntity")


class AbstractOrmMapper(ABC, Generic[_DomainEntity, _OrmEntity]):
    @abstractmethod
    def domain_to_orm(self, domain_entity: _DomainEntity) -> _OrmEntity:
        ...

    @abstractmethod
    def orm_to_domain(self, orm_entity: _OrmEntity) -> _DomainEntity:
        ...
