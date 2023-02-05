from abc import ABC, abstractmethod
from typing import Generic, TypeVar

_DomainEntity = TypeVar("_DomainEntity")
_OrmEntity = TypeVar("_OrmEntity")


class IEntityMapper(ABC, Generic[_DomainEntity, _OrmEntity]):
    @abstractmethod
    def domain_to_dict(self, domain_entity: _DomainEntity) -> dict:
        ...

    @abstractmethod
    def domains_to_dicts(self, domain_entities: list[_DomainEntity]) -> list[dict]:
        ...
    
    @abstractmethod
    def domain_to_orm(self, domain_entity: _DomainEntity) -> _OrmEntity:
        ...

    @abstractmethod
    def domains_to_orms(self, domain_entities: list[_DomainEntity]) -> list[_OrmEntity]:
        ...

    @abstractmethod
    def orm_to_domain(self, orm_entity: _OrmEntity) -> _DomainEntity:
        ...

    @abstractmethod
    def orms_to_domains(self, orm_entities: list[_OrmEntity]) -> list[_DomainEntity]:
        ...
