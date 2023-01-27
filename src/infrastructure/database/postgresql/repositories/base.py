from abc import abstractmethod
from typing import TypeVar, List, Generic, Type

from src.application.interfaces.repositories import AbstractRepository
from src.infrastructure.database.postgresql.mappers.base import AbstractOrmMapper
from src.infrastructure.database.postgresql.orm.configs import BaseModel as BaseDbModel
from src.domain.models.abstract import AbstractModel as AbstractDomainModel

_EntityType = TypeVar("_EntityType", bound=AbstractDomainModel)
_EntityIdType = TypeVar("_EntityIdType")


class BasePostgresqlRepository(
    AbstractRepository[_EntityType, _EntityIdType],
    Generic[_EntityType, _EntityIdType]
):
    @abstractmethod
    def get_orm_class(self) -> Type[BaseDbModel]:
        ...

    @abstractmethod
    def get_orm_mapper(self) -> AbstractOrmMapper[_EntityType, BaseDbModel]:
        ...

    def get(self, *args, **kwargs) -> List[_EntityType]:
        orm_class = self.get_orm_class()
        orm_mapper = self.get_orm_mapper()

        orm_entities = orm_class.select().execute()

        return [
            orm_mapper.orm_to_domain(orm_entity)
            for orm_entity in orm_entities
        ]

    def get_by_id(self, entity_id: _EntityIdType, *args, **kwargs) -> _EntityType:
        orm_class = self.get_orm_class()
        orm_mapper = self.get_orm_mapper()

        orm_entity = orm_class.select().where(orm_class.id == entity_id).execute()

        if isinstance(orm_entity, list):
            orm_entity = orm_entity[0]

        return orm_mapper.orm_to_domain(orm_entity)

    def add(self, entity: _EntityType, *args, **kwargs):
        orm_mapper = self.get_orm_mapper()
        orm_entity = orm_mapper.domain_to_orm(entity)
        orm_entity.save()

        return orm_mapper.orm_to_domain(orm_entity)

    def update(self, entity: _EntityType, *args, **kwargs):
        orm_mapper = self.get_orm_mapper()
        orm_entity = orm_mapper.domain_to_orm(entity)
        orm_entity.save()

        return orm_mapper.orm_to_domain(orm_entity)

    def delete(self, entity_id: _EntityIdType, *args, **kwargs):
        orm_class = self.get_orm_class()
        orm_class.delete().where(orm_class.id == entity_id).execute()
