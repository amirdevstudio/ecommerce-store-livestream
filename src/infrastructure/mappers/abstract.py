from abc import ABC
from typing import TypeVar, Generic

from src.application.interfaces.mapper import IEntityMapper


_DomainEntity = TypeVar("_DomainEntity")
_OrmEntity = TypeVar("_OrmEntity")


class AbstractEntityMapper(
    IEntityMapper[_DomainEntity, _OrmEntity],
    ABC,
    Generic[_DomainEntity, _OrmEntity],
):
    def domains_to_dicts(self, domain_entities: list[_DomainEntity]) -> list[dict]:
        return [self.domain_to_dict(domain_entity) for domain_entity in domain_entities]

    def domains_to_orms(self, domain_entities: list[_DomainEntity]) -> list[_OrmEntity]:
        return [self.domain_to_orm(domain_entity) for domain_entity in domain_entities]

    def orms_to_domains(self, orm_entities: list[_OrmEntity]) -> list[_DomainEntity]:
        return [self.orm_to_domain(orm_entity) for orm_entity in orm_entities]
