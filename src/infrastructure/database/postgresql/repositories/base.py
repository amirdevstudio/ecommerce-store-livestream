from abc import abstractmethod
from threading import Lock
from typing import TypeVar, Generic, Type, Optional, List

from src.application.interfaces.repositories import AbstractRepository
from src.application.pagination import PaginationOptions, PaginatedResults
from src.application.query_filters import QueryFilters, QueryFilterRecipes
from src.application.sorting import SortingOptions
from src.application.interfaces.mapper import AbstractEntityMapper
from src.infrastructure.database.postgresql.orm.extensions.peewee import PeeweeSelectQueryExtension
from src.infrastructure.database.postgresql.orm.configs import BaseModel as BaseDbModel, database
from src.domain.models.abstract import AbstractModel as AbstractDomainModel

_EntityType = TypeVar("_EntityType", bound=AbstractDomainModel)
_EntityIdType = TypeVar("_EntityIdType")


class BasePostgresqlRepository(
    AbstractRepository[_EntityType, _EntityIdType],
    Generic[_EntityType, _EntityIdType]
):
    def __init__(self):
        self._thread_lock = Lock()

    @abstractmethod
    def _get_orm_class(self) -> Type[BaseDbModel]:
        ...

    @abstractmethod
    def _get_entity_mapper(self) -> AbstractEntityMapper[_EntityType, BaseDbModel]:
        ...

    def get(
            self,
            filters: Optional[QueryFilters] = None,
            pagination_options: Optional[PaginationOptions] = None,
            sorting_options: Optional[SortingOptions] = None
    ) -> PaginatedResults[_EntityType]:
        orm_class = self._get_orm_class()
        orm_mapper = self._get_entity_mapper()

        query = orm_class.select()
        extension = PeeweeSelectQueryExtension(query)

        if filters:
            extension.apply_filters(filters)

        if pagination_options:
            extension.apply_pagination(pagination_options)

        if sorting_options:
            extension.apply_sorting(sorting_options)

        orm_entities = extension.query.execute()

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

    def get_by_id(self, entity_id: _EntityIdType, *args, **kwargs) -> Optional[_EntityType]:
        filters = QueryFilterRecipes.where_id_equals_value(entity_id)
        results = self.get(filters=filters)

        if results.total > 0:
            return results.items[0]

    def add(self, entity: _EntityType, *args, **kwargs):
        orm_mapper = self._get_entity_mapper()
        orm_entity = orm_mapper.domain_to_orm(entity)
        orm_entity.save()

        return orm_mapper.orm_to_domain(orm_entity)

    def add_many(self, entities: List[_EntityType], *args, **kwargs) -> List[_EntityType]:
        orm_class = self._get_orm_class()
        orm_mapper = self._get_entity_mapper()

        entities_as_dicts = []

        for entity in entities:
            entity_as_dict = orm_mapper.domain_to_dict(entity)
            entity_as_dict.pop('id')
            entities_as_dicts.append(entity_as_dict)

        with database.atomic():
            inserted_ids = orm_class.insert_many(entities_as_dicts).execute()
            inserted_ids = [id_[0] for id_ in inserted_ids.row_cache]
            inserted_records = self.get(
                filters=QueryFilterRecipes.where_field_in_values('id', inserted_ids)
            )

        return inserted_records.items

    def update(self, entity: _EntityType, *args, **kwargs):
        orm_mapper = self._get_entity_mapper()
        orm_entity = orm_mapper.domain_to_orm(entity)
        orm_entity.save()

        return orm_mapper.orm_to_domain(orm_entity)

    def delete(self, entity_id: _EntityIdType, *args, **kwargs):
        orm_class = self._get_orm_class()
        orm_class.delete().where(orm_class.id == entity_id).execute()

    def count(self, filters: QueryFilters) -> int:
        orm_class = self._get_orm_class()
        query = orm_class.select()

        adapter = PeeweeSelectQueryExtension(query)
        adapter.apply_filters(filters)

        return adapter.query.count()
