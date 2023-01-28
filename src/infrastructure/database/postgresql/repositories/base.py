from abc import abstractmethod
from typing import TypeVar, List, Generic, Type

from src.application.interfaces.repositories import AbstractRepository
from src.application.pagination import PaginationOptions, PaginatedResults
from src.application.query_filters import QueryFilters
from src.application.sorting import SortingOptions
from src.infrastructure.database.postgresql.mappers.base import AbstractOrmMapper
from src.infrastructure.database.postgresql.orm.adapters.peewee import PeeweeSelectQueryAdapter
from src.infrastructure.database.postgresql.orm.configs import BaseModel as BaseDbModel
from src.domain.models.abstract import AbstractModel as AbstractDomainModel

_EntityType = TypeVar("_EntityType", bound=AbstractDomainModel)
_EntityIdType = TypeVar("_EntityIdType")


class BasePostgresqlRepository(
    AbstractRepository[_EntityType, _EntityIdType],
    Generic[_EntityType, _EntityIdType]
):
    @abstractmethod
    def _get_orm_class(self) -> Type[BaseDbModel]:
        ...

    @abstractmethod
    def _get_orm_mapper(self) -> AbstractOrmMapper[_EntityType, BaseDbModel]:
        ...

    def _apply_filter_to_query(self):
        ...

    def get(
            self,
            filters: QueryFilters,
            pagination_options: PaginationOptions,
            sorting_options: SortingOptions
    ) -> PaginatedResults[_EntityType]:
        orm_class = self._get_orm_class()
        orm_mapper = self._get_orm_mapper()

        query = orm_class.select()

        adapter = PeeweeSelectQueryAdapter(query)

        adapter.apply_filters(filters)
        adapter.apply_pagination(pagination_options)
        adapter.apply_sorting(sorting_options)

        orm_entities = adapter.query.execute()

        entities = [
            orm_mapper.orm_to_domain(orm_entity)
            for orm_entity in orm_entities
        ]

        entities_count = self.count(filters)

        return PaginatedResults(
            total=entities_count,
            items=entities,
            pagination_options=pagination_options,
            sorting_options=sorting_options
        )

    def get_by_id(self, entity_id: _EntityIdType, *args, **kwargs) -> _EntityType:
        orm_class = self._get_orm_class()
        orm_mapper = self._get_orm_mapper()

        orm_entity = orm_class.select().where(orm_class.id == entity_id).execute()

        if isinstance(orm_entity, list):
            orm_entity = orm_entity[0]

        return orm_mapper.orm_to_domain(orm_entity)

    def add(self, entity: _EntityType, *args, **kwargs):
        orm_mapper = self._get_orm_mapper()
        orm_entity = orm_mapper.domain_to_orm(entity)
        orm_entity.save()

        return orm_mapper.orm_to_domain(orm_entity)

    def update(self, entity: _EntityType, *args, **kwargs):
        orm_mapper = self._get_orm_mapper()
        orm_entity = orm_mapper.domain_to_orm(entity)
        orm_entity.save()

        return orm_mapper.orm_to_domain(orm_entity)

    def delete(self, entity_id: _EntityIdType, *args, **kwargs):
        orm_class = self._get_orm_class()
        orm_class.delete().where(orm_class.id == entity_id).execute()

    def count(self, filters: QueryFilters) -> int:
        orm_class = self._get_orm_class()
        query = orm_class.select()

        adapter = PeeweeSelectQueryAdapter(query)
        adapter.apply_filters(filters)

        return adapter.query.count()
