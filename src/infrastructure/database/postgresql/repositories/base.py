from threading import Lock
from typing import TypeVar, Generic, Type, Optional, List

from peewee import BaseQuery

from src.application.interfaces.repositories import AbstractRepository
from src.application.pagination import PaginationOptions, PaginatedResults
from src.application.query_filters import QueryFilters, QueryFilterTemplates
from src.application.sorting import SortingOptions
from src.application.interfaces.mapper import IEntityMapper
from src.infrastructure.database.postgresql.orm.extensions.peewee import PeeweeSelectQueryExtension
from src.infrastructure.database.postgresql.orm.configs import BaseEntity as BaseDbModel, database
from src.domain.entities.abstract import AbstractEntity as AbstractDomainModel

_EntityType = TypeVar("_EntityType", bound=AbstractDomainModel)
_EntityIdType = TypeVar("_EntityIdType")


class BasePostgresqlRepository(
    AbstractRepository[_EntityType, _EntityIdType],
    Generic[_EntityType, _EntityIdType]
):
    def __init__(
            self,
            orm_class: Type[BaseDbModel],
            auto_mapper: IEntityMapper[_EntityType, BaseDbModel]
    ):
        self._thread_lock = Lock()
        self.orm_class = orm_class
        self.auto_mapper = auto_mapper

    def _get_query(
            self,
            filters: Optional[QueryFilters] = None,
            pagination_options: Optional[PaginationOptions] = None,
            sorting_options: Optional[SortingOptions] = None
    ) -> BaseQuery:
        query = self.orm_class.select()

        extension = PeeweeSelectQueryExtension(query)

        if filters:
            extension.apply_filters(filters)

        if pagination_options:
            extension.apply_pagination(pagination_options)

        if sorting_options:
            extension.apply_sorting(sorting_options)

        return extension.query

    def get(
            self,
            filters: Optional[QueryFilters] = None,
            pagination_options: Optional[PaginationOptions] = None,
            sorting_options: Optional[SortingOptions] = None
    ) -> PaginatedResults[_EntityType]:
        query = self._get_query(
            filters=filters,
            pagination_options=pagination_options,
            sorting_options=sorting_options
        )

        entities = query.execute()
        entities = self.auto_mapper.orms_to_domains(entities)
        entities_count = self.count(filters)

        return PaginatedResults(
            total=entities_count,
            items=entities,
            pagination_options=pagination_options,
            sorting_options=sorting_options
        )

    def get_by_id(self, entity_id: _EntityIdType, *args, **kwargs) -> Optional[_EntityType]:
        filters = QueryFilterTemplates.where_id_equals_value(entity_id)
        results = self.get(filters=filters)

        if results.total > 0:
            return results.items[0]

    def add(self, entity: _EntityType, *args, **kwargs):
        orm_entity = self.auto_mapper.domain_to_orm(entity)
        orm_entity.save()

        return self.auto_mapper.orm_to_domain(orm_entity)

    def add_many(self, entities: List[_EntityType], *args, **kwargs) -> List[_EntityType]:
        if not entities:
            return entities

        entities = self.auto_mapper.domains_to_orms(entities)
        self.orm_class.bulk_create(entities)
        entities = self.auto_mapper.orms_to_domains(entities)

        return entities

    def update(self, entity: _EntityType, *args, **kwargs):
        orm_entity = self.auto_mapper.domain_to_orm(entity)
        orm_entity.save()

        return self.auto_mapper.orm_to_domain(orm_entity)

    def delete(self, entity_id: _EntityIdType, *args, **kwargs):
        self.orm_class.delete().where(self.orm_class.id == entity_id).load()

    def count(self, filters: QueryFilters) -> int:
        query = self.orm_class.select()

        adapter = PeeweeSelectQueryExtension(query)

        if filters:
            adapter.apply_filters(filters)

        return adapter.query.count()
