from abc import ABC, abstractmethod
from typing import Generic, TypeVar

from src.domain.models.product import Product as ProductDomainModel
from src.infrastructure.orm.postgresql.models import Product as ProductOrmModel

_DomainEntity = TypeVar("_DomainEntity")
_OrmEntity = TypeVar("_OrmEntity")


class AbstractOrmMapper(ABC, Generic[_DomainEntity, _OrmEntity]):
    @abstractmethod
    def map_domain_entity_to_orm_entity(self, domain_entity: _DomainEntity) -> _OrmEntity:
        ...

    @abstractmethod
    def map_orm_entity_to_domain_entity(self, orm_entity: _OrmEntity) -> _DomainEntity:
        ...


class ProductOrmMapper(AbstractOrmMapper[ProductDomainModel, ProductOrmModel]):
    def map_domain_entity_to_orm_entity(self, domain_entity: ProductDomainModel) -> ProductOrmModel:
        return ProductOrmModel()

    def map_orm_entity_to_domain_entity(self, orm_entity: ProductOrmModel) -> ProductDomainModel:
        pass
